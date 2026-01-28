from django.db import models


class Profile(models.Model):
    """Personal profile information"""
    hero_greeting = models.CharField(max_length=100, default="Hi, I'm")
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Full Stack Developer")
    contact_title = models.CharField(max_length=200, default="Let's Work Together")
    contact_description = models.TextField(default="Have a project in mind? I'd love to hear about it. Send me a message and let's create something amazing together.")
    contact_social_text = models.CharField(max_length=100, default="Follow Me")
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
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
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('mobile', 'Mobile'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
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
    client_image = models.URLField(blank=True, null=True)
    content = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating 1-5")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Testimonial from {self.client_name}"
    
    class Meta:
        ordering = ['order']
