"""
Initial data setup script for portfolio
Run this after migrations to populate the database
"""
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience, Service, Testimonial

class Command(BaseCommand):
    help = 'Loads initial portfolio data'

    def handle(self, *args, **kwargs):
        # Create Profile if it doesn't exist
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name="Biruk Tilahun Dinki",
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
