from django.core.mail import send_mail
from django.conf import settings
import sys

print(f"Testing email settings:")
print(f"HOST: {settings.EMAIL_HOST}")
print(f"PORT: {settings.EMAIL_PORT}")
print(f"USER: {settings.EMAIL_HOST_USER}")

try:
    send_mail(
        subject='Test Email from Django',
        message='If you receive this, email configuration is working correctly.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['biruktilahundinki@gmail.com'],
        fail_silently=False,
    )
    print("✅ SUCCESS: Email sent successfully!")
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
