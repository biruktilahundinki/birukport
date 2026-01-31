from django.db import models

class SkillCategory(models.Model):
    """Admin-managed categories for skills"""
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"
        
    def __str__(self):
        return self.name

class BudgetOption(models.Model):
    """Admin-managed budget options for contact form"""
    label = models.CharField(max_length=100, help_text="Display text (e.g., '$50 - $100')")
    value = models.CharField(max_length=100, help_text="Value sent in email (e.g., '50-100')")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class SiteContent(models.Model):
    """Editable site content - All text visible on pages can be edited here"""
    
    # Singleton pattern - only one record
    class Meta:
        verbose_name = "Site Content"
        verbose_name_plural = "Site Content"
    
    # Visibility Settings
    show_hero = models.BooleanField(default=True, verbose_name="Show Hero Section")
    show_about = models.BooleanField(default=True, verbose_name="Show About Section")
    show_skills = models.BooleanField(default=True, verbose_name="Show Skills Section")
    show_services = models.BooleanField(default=True, verbose_name="Show Services Section")
    show_projects = models.BooleanField(default=True, verbose_name="Show Projects Section")
    show_experience = models.BooleanField(default=True, verbose_name="Show Experience Section")
    show_documents = models.BooleanField(default=True, verbose_name="Show Documents Section")
    show_testimonials = models.BooleanField(default=True, verbose_name="Show Testimonials Section")
    show_contact = models.BooleanField(default=True, verbose_name="Show Contact Section")

    # Navigation
    nav_home_text = models.CharField(max_length=50, default="Home")
    nav_about_text = models.CharField(max_length=50, default="About")
    nav_skills_text = models.CharField(max_length=50, default="Skills")
    nav_services_text = models.CharField(max_length=50, default="Services")
    nav_projects_text = models.CharField(max_length=50, default="Projects")
    nav_experience_text = models.CharField(max_length=50, default="Experience")
    nav_contact_text = models.CharField(max_length=50, default="Contact")
    nav_hire_button_text = models.CharField(max_length=50, default="Hire Me")
    
    # Hero Section
    hero_description = models.TextField(
        default="I build exceptional digital experiences that combine beautiful design with powerful functionality. Let's turn your ideas into reality."
    )
    hero_view_projects_text = models.CharField(max_length=50, default="View Projects")
    hero_get_in_touch_text = models.CharField(max_length=50, default="Get In Touch")
    hero_years_exp_label = models.CharField(max_length=50, default="Years Experience")
    hero_projects_label = models.CharField(max_length=50, default="Projects Completed")
    hero_clients_label = models.CharField(max_length=50, default="Happy Clients")
    
    # Floating Cards
    floating_card1_title = models.CharField(max_length=50, default="Clean Code")
    floating_card1_subtitle = models.CharField(max_length=50, default="Best Practices")
    floating_card2_title = models.CharField(max_length=50, default="Fast Delivery")
    floating_card2_subtitle = models.CharField(max_length=50, default="On Time")
    floating_card3_title = models.CharField(max_length=50, default="5 Star")
    floating_card3_subtitle = models.CharField(max_length=50, default="Reviews")
    
    # About Section
    about_section_title = models.CharField(max_length=100, default="About Me")
    about_description = models.TextField(
        default="I'm a passionate software developer with expertise in building modern web applications. I love turning complex problems into simple, beautiful solutions."
    )
    about_description2 = models.TextField(
        default="With years of experience in full-stack development, I specialize in creating scalable, maintainable, and user-friendly applications that help businesses grow."
    )
    about_feature1 = models.CharField(max_length=100, default="Full Stack Development")
    about_feature2 = models.CharField(max_length=100, default="Clean & Scalable Code")
    about_feature3 = models.CharField(max_length=100, default="Responsive Design")
    about_feature4 = models.CharField(max_length=100, default="API Development")
    
    # Skills Section
    skills_section_title = models.CharField(max_length=100, default="My Skills")
    skills_section_subtitle = models.CharField(max_length=200, default="Technologies and tools I work with")
    
    # Services Section
    services_section_title = models.CharField(max_length=100, default="Services I Offer")
    services_section_subtitle = models.CharField(max_length=200, default="Professional services tailored to your needs")
    
    # Projects Section
    projects_section_title = models.CharField(max_length=100, default="My Projects")
    projects_section_subtitle = models.CharField(max_length=200, default="Explore my recent work and see what I can build for you")
    projects_filter_all = models.CharField(max_length=50, default="All")
    projects_filter_web = models.CharField(max_length=50, default="Web Apps")
    projects_filter_mobile = models.CharField(max_length=50, default="Mobile")
    projects_filter_api = models.CharField(max_length=50, default="API/Backend")
    projects_filter_ai = models.CharField(max_length=50, default="AI/ML")
    projects_featured_label = models.CharField(max_length=50, default="Featured")
    
    # Experience Section
    experience_section_title = models.CharField(max_length=100, default="Work Experience")
    experience_section_subtitle = models.CharField(max_length=200, default="My professional journey")
    experience_present_text = models.CharField(max_length=50, default="Present")
    
    # Documents Section
    documents_section_title = models.CharField(max_length=100, default="Documents & Certifications")
    documents_section_subtitle = models.CharField(max_length=200, default="My professional documents and certifications")
    documents_view_button = models.CharField(max_length=50, default="View Document")
    
    # Contact Section
    contact_email_label = models.CharField(max_length=50, default="Email")
    contact_location_label = models.CharField(max_length=50, default="Location")
    contact_phone_label = models.CharField(max_length=50, default="Phone")
    contact_form_name_label = models.CharField(max_length=50, default="Your Name")
    contact_form_name_placeholder = models.CharField(max_length=100, default="John Doe")
    contact_form_email_label = models.CharField(max_length=50, default="Your Email")
    contact_form_email_placeholder = models.CharField(max_length=100, default="john@example.com")
    contact_form_project_label = models.CharField(max_length=50, default="Project Type")
    contact_form_project_placeholder = models.CharField(max_length=100, default="Select a type")
    contact_form_budget_label = models.CharField(max_length=50, default="Payment Range")
    contact_form_budget_placeholder = models.CharField(max_length=100, default="Select Payment")
    contact_form_subject_label = models.CharField(max_length=50, default="Subject")
    contact_form_subject_placeholder = models.CharField(max_length=100, default="Project Inquiry")
    contact_form_message_label = models.CharField(max_length=50, default="Message")
    contact_form_message_placeholder = models.CharField(max_length=200, default="Tell me about your project...")
    contact_form_submit_text = models.CharField(max_length=50, default="Send Message")
    
    # Project Type Options
    project_type_web = models.CharField(max_length=50, default="Web Application")
    project_type_mobile = models.CharField(max_length=50, default="Mobile App")
    project_type_api = models.CharField(max_length=50, default="API/Backend")
    project_type_other = models.CharField(max_length=50, default="Other")
    
    # Budget Options - DEPRECATED in favor of Dynamic BudgetOption model, but keeping as fallback text defaults
    budget_option1 = models.CharField(max_length=50, default="Less than $50")
    budget_option2 = models.CharField(max_length=50, default="$50 - $80")
    budget_option3 = models.CharField(max_length=50, default="$80 - $100")
    budget_option4 = models.CharField(max_length=50, default="$100+")
    budget_option5 = models.CharField(max_length=50, default="Agreement")
    
    # Footer
    footer_copyright = models.CharField(max_length=200, default="© 2024 All Rights Reserved.")
    footer_admin_text = models.CharField(max_length=50, default="Admin")
    
    # Meta description for SEO
    meta_description = models.CharField(
        max_length=300, 
        default="Professional Software Developer Portfolio - Building Digital Solutions"
    )
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return "Site Content Settings"


class Profile(models.Model):
    """Personal profile information"""
    hero_greeting = models.CharField(max_length=100, default="Hi, I'm")
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Full Stack Developer")
    bio = models.TextField(blank=True, null=True, help_text="Short bio for hero/about section")
    contact_title = models.CharField(max_length=200, default="Let's Work Together")
    contact_description = models.TextField(default="Have a project in mind? I'd love to hear about it. Send me a message and let's create something amazing together.")
    contact_social_text = models.CharField(max_length=100, default="Follow Me")
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    about_image = models.ImageField(upload_to='about_images/', blank=True, null=True, help_text="Image for About section")
    location = models.CharField(max_length=200, blank=True, null=True, default="Available Worldwide (Remote)")
    phone = models.CharField(max_length=20, blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    whatsapp_url = models.URLField(blank=True, null=True)
    email = models.EmailField()
    resume_url = models.URLField(blank=True, null=True, help_text="Link to downloadable resume")
    years_experience = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Profile"


class Skill(models.Model):
    """Technical skills"""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills', null=True)
    proficiency = models.IntegerField(default=100, help_text="Skill level 1-100")
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class name")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    """Portfolio projects to showcase"""
    CATEGORY_CHOICES = [
        ('web', 'Web App'),
        ('mobile', 'Mobile App'),
        ('ai', 'AI/ML'),
        ('api', 'API/Backend'),
        ('desktop', 'Desktop App'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image_url = models.ImageField(upload_to='project_images/', help_text="Project screenshot/thumbnail")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-featured', 'order', '-created_at']


class Experience(models.Model):
    """Work experience timeline"""
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.role} at {self.company}"
    
    class Meta:
        ordering = ['-is_current', '-start_date']
        verbose_name_plural = "Experience"


class Service(models.Model):
    """Services offered to clients"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Icon class name (e.g., 'fas fa-globe' or Google Icon name)")
    icon_image = models.ImageField(upload_to='service_icons/', blank=True, null=True, help_text="Upload a custom icon image")
    icon_url = models.URLField(blank=True, null=True, help_text="Or provide a Google/external icon URL")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']


class PortfolioDocument(models.Model):
    """Documents uploaded by admin (e.g., certifications, resumes, project docs)"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Brief description of the document")
    file = models.FileField(upload_to='portfolio_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']


class ContactMessage(models.Model):
    """Customer inquiries for jobs"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    project_type = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_reply = models.TextField(blank=True, null=True)
    replied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - {self.name}"

    class Meta:
        ordering = ['-created_at']


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=200, blank=True)
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    content = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating 1-5")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Testimonial from {self.client_name}"
    
    class Meta:
        ordering = ['order']
