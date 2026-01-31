from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, SkillCategory, Service, SiteContent, BudgetOption
import os

class Command(BaseCommand):
    help = 'Loads initial portfolio data and creates admin'

    def handle(self, *args, **kwargs):
        # Create Superuser if it doesn't exist
        admin_username = os.environ.get('PORTFOLIO_ADMIN_NAME', 'admin')
        admin_email = os.environ.get('PORTFOLIO_ADMIN_EMAIL', 'admin@example.com')
        admin_password = os.environ.get('PORTFOLIO_ADMIN_PASSWORD', 'admin123')

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS(f'Created Superuser: {admin_username}'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))

        # Create SiteContent singleton
        if not SiteContent.objects.exists():
            SiteContent.objects.create()
            self.stdout.write(self.style.SUCCESS('Created SiteContent'))
        
        # Create Profile if it doesn't exist
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name="Biruk Tilahun",
                title="Full Stack Developer",
                email="biruktilahundinki@gmail.com",
                phone="+251 900 000 000",
                location="Addis Ababa, Ethiopia",
                hero_greeting="Hi, I'm",
                bio="I build exceptional digital experiences that combine beautiful design with powerful functionality. Let's turn your ideas into reality.",
                contact_description="Have a project in mind? I'd love to hear about it.",
                contact_title="Let's Work Together",
                github_url="https://github.com/biruktilahundinki",
                linkedin_url="https://linkedin.com/in/biruktilahun",
                projects_completed=10,
                years_experience=2
            )
            self.stdout.write(self.style.SUCCESS('Created Profile'))

        # Create Budget Options
        if not BudgetOption.objects.exists():
            budget_options = [
                ("Less than $50", "<1k", 1),
                ("$50 - $80", "1k-5k", 2),
                ("$80 - $100", "5k-10k", 3),
                ("$100+", "10k+", 4),
                ("Agreement", "agreement", 5),
            ]
            for label, value, order in budget_options:
                BudgetOption.objects.create(label=label, value=value, order=order)
            self.stdout.write(self.style.SUCCESS('Created Budget Options'))

        # Create Skill Categories and Skills
        skill_categories = {
            "frontend": "Frontend",
            "backend": "Backend",
            "design": "Graphics & Design",
            "database": "Database",
            "devops": "DevOps",
            "mobile": "Mobile",
            "other": "Other",
        }

        # Create categories first
        categories_map = {}
        for code, name in skill_categories.items():
            cat, created = SkillCategory.objects.get_or_create(name=name)
            categories_map[code] = cat

        skills_data = [
            ("Python", "backend", 95),
            ("Django", "backend", 90),
            ("JavaScript", "frontend", 85),
            ("React", "frontend", 80),
            ("PostgreSQL", "database", 85),
            ("Docker", "devops", 75),
            ("AWS", "devops", 70),
            ("Photoshop", "design", 85),
            ("Figma", "design", 90),
        ]
        
        for name, category_code, proficiency in skills_data:
            Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': categories_map.get(category_code),
                    'proficiency': proficiency
                }
            )
        self.stdout.write(self.style.SUCCESS(f'Checked/Created skills'))

        # Add sample services if none exist
        if not Service.objects.exists():
            services_data = [
                ("Web Development", "fas fa-code", "Custom web applications built with Django and React."),
                ("API Development", "fas fa-server", "Scalable RESTful APIs."),
                ("Mobile Apps", "fas fa-mobile-alt", "Cross-platform mobile apps."),
            ]
            for title, icon, desc in services_data:
                Service.objects.create(title=title, icon=icon, description=desc)
            self.stdout.write(self.style.SUCCESS('Created sample services'))

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully!'))
