from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, Project, Experience, Service, Testimonial
import os

class Command(BaseCommand):
    help = 'Loads initial portfolio data and creates admin'

    def handle(self, *args, **kwargs):
        # Create Superuser if it doesn't exist
        admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS(f'Created Superuser: {admin_username}'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))

        # Create Profile if it doesn't exist
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name="Biruk Tilahun",
                title="Full Stack Developer",
                email="biruktilahundinki@gmail.com",
                phone="+251 your-phone",
                location="Addis Ababa, Ethiopia",
                hero_greeting="Hello, I'm",
                about_description="I am a passionate full-stack developer...",
                contact_description="Get in touch with me",
                linkedin_url="https://linkedin.com/in/yourprofile",
                github_url="https://github.com/biruktilahundinki",
                twitter_url="https://twitter.com/yourhandle"
            )
            self.stdout.write(self.style.SUCCESS('Created Profile'))

        # Add sample skills
        skills_data = [
            ("Python", "BACKEND", 90),
            ("Django", "BACKEND", 85),
            ("JavaScript", "FRONTEND", 80),
            ("React", "FRONTEND", 75),
        ]
        
        for name, category, proficiency in skills_data:
            Skill.objects.get_or_create(
                name=name,
                defaults={'category': category, 'proficiency': proficiency}
            )
        self.stdout.write(self.style.SUCCESS(f'Created {len(skills_data)} skills'))

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully!'))
