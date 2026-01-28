import os
import zipfile
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.conf import settings

class Command(BaseCommand):
    help = 'Sends a backup of the database and media folder via email'

    def handle(self, *args, **options):
        # Configuration
        recipient = 'biruktilahundinki@gmail.com'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_filename = f'portfolio_backup_{timestamp}.zip'
        zip_path = os.path.join(settings.BASE_DIR, zip_filename)

        self.stdout.write(f'Creating backup: {zip_filename}...')

        try:
            MAX_ZIP_SIZE = 24 * 1024 * 1024  # 24 MB limit
            skipped_files = []
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add Database (Priority)
                db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
                if os.path.exists(db_path):
                    zipf.write(db_path, arcname='db.sqlite3')
                    self.stdout.write('Database added.')
                
                # Add Media
                media_root = settings.MEDIA_ROOT
                if os.path.exists(media_root):
                    current_zip_size = 0 # Initial
                    
                    for root, dirs, files in os.walk(media_root):
                        for file in files:
                            file_path = os.path.join(root, file)
                            file_size = os.path.getsize(file_path)
                            
                            # Check if adding this file might exceed limit (conservative estimate)
                            if (current_zip_size + file_size) > MAX_ZIP_SIZE:
                                skipped_files.append(file)
                                continue
                            
                            rel_path = os.path.relpath(file_path, settings.BASE_DIR)
                            zipf.write(file_path, arcname=rel_path)
                            current_zip_size += file_size
                
                if skipped_files:
                    manifest = f"The following files were skipped due to size limits:\n" + "\n".join(skipped_files)
                    zipf.writestr('skipped_files_manifest.txt', manifest)
                    self.stdout.write(self.style.WARNING(f'Skipped {len(skipped_files)} files to respect 25MB limit.'))

            self.stdout.write(f'Backup file created ({os.path.getsize(zip_path)} bytes). Sending email...')

            # Send Email
            email = EmailMessage(
                subject=f'Project Backup - {timestamp}',
                body=f'Attached is your project backup (Database + selected Media).\n\nDetails: {len(skipped_files)} files were skipped due to Gmail limits.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
            )
            email.attach_file(zip_path)
            email.send()

            self.stdout.write(self.style.SUCCESS(f'Backup sent successfully to {recipient}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
        
        finally:
            # Clean up
            if os.path.exists(zip_path):
                os.remove(zip_path)
                self.stdout.write('Temporary backup file removed.')
