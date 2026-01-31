from django.contrib import admin
from .models import (
    Profile, Skill, SkillCategory, Project, Experience, 
    Service, ContactMessage, Testimonial, PortfolioDocument, 
    SiteContent, BudgetOption
)
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.utils.html import format_html
from django.urls import reverse


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    """Admin for editing all visible text on the website"""
    
    fieldsets = (
        ('👁️ Section Visibility', {
            'fields': (
                ('show_hero', 'show_about', 'show_skills'),
                ('show_services', 'show_projects', 'show_experience'),
                ('show_documents', 'show_testimonials', 'show_contact'),
            ),
        }),
        ('🧭 Navigation Text', {
            'fields': (
                ('nav_home_text', 'nav_about_text', 'nav_skills_text'),
                ('nav_services_text', 'nav_projects_text', 'nav_experience_text'),
                ('nav_contact_text', 'nav_hire_button_text'),
            ),
            'classes': ('collapse',),
        }),
        ('🦸 Hero Section', {
            'fields': (
                'hero_description',
                ('hero_view_projects_text', 'hero_get_in_touch_text'),
                ('hero_years_exp_label', 'hero_projects_label', 'hero_clients_label'),
            ),
        }),
        ('🎴 Floating Cards', {
            'fields': (
                ('floating_card1_title', 'floating_card1_subtitle'),
                ('floating_card2_title', 'floating_card2_subtitle'),
                ('floating_card3_title', 'floating_card3_subtitle'),
            ),
            'classes': ('collapse',),
        }),
        ('👤 About Section', {
            'fields': (
                'about_section_title',
                'about_description',
                'about_description2',
                ('about_feature1', 'about_feature2'),
                ('about_feature3', 'about_feature4'),
            ),
        }),
        ('🛠️ Skills Section', {
            'fields': (
                'skills_section_title',
                'skills_section_subtitle',
            ),
            'classes': ('collapse',),
        }),
        ('💼 Services Section', {
            'fields': (
                'services_section_title',
                'services_section_subtitle',
            ),
            'classes': ('collapse',),
        }),
        ('🚀 Projects Section', {
            'fields': (
                'projects_section_title',
                'projects_section_subtitle',
                ('projects_filter_all', 'projects_filter_web', 'projects_filter_mobile'),
                ('projects_filter_api', 'projects_filter_ai'),
                'projects_featured_label',
            ),
            'classes': ('collapse',),
        }),
        ('📅 Experience Section', {
            'fields': (
                'experience_section_title',
                'experience_section_subtitle',
                'experience_present_text',
            ),
            'classes': ('collapse',),
        }),
        ('📄 Documents Section', {
            'fields': (
                'documents_section_title',
                'documents_section_subtitle',
                'documents_view_button',
            ),
            'classes': ('collapse',),
        }),
        ('📬 Contact Form Labels', {
            'fields': (
                ('contact_email_label', 'contact_location_label', 'contact_phone_label'),
                ('contact_form_name_label', 'contact_form_name_placeholder'),
                ('contact_form_email_label', 'contact_form_email_placeholder'),
                ('contact_form_project_label', 'contact_form_project_placeholder'),
                ('contact_form_budget_label', 'contact_form_budget_placeholder'),
                ('contact_form_subject_label', 'contact_form_subject_placeholder'),
                ('contact_form_message_label', 'contact_form_message_placeholder'),
                'contact_form_submit_text',
            ),
            'classes': ('collapse',),
        }),
        ('📋 Project Type Options', {
            'fields': (
                ('project_type_web', 'project_type_mobile'),
                ('project_type_api', 'project_type_other'),
            ),
            'classes': ('collapse',),
        }),
        ('💰 Budget Defaults (Use "Budget Defaults" for initial values)', {
            'fields': (
                ('budget_option1', 'budget_option2', 'budget_option3'),
                ('budget_option4', 'budget_option5'),
            ),
            'classes': ('collapse',),
        }),
        ('🔻 Footer', {
            'fields': (
                'footer_copyright',
                'footer_admin_text',
            ),
            'classes': ('collapse',),
        }),
        ('🔍 SEO', {
            'fields': (
                'meta_description',
            ),
            'classes': ('collapse',),
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteContent.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
        # Redirect to the single instance edit page
        obj = SiteContent.get_instance()
        return super().change_view(request, str(obj.pk), extra_context=extra_context)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'location', 'email', 'phone', 'telegram_url', 'whatsapp_url', 'delete_button']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'hero_greeting', 'bio', 'email', 'phone', 'location')
        }),
        ('Images', {
            'fields': ('profile_image', 'about_image')
        }),
        ('Contact Section Text', {
            'fields': ('contact_title', 'contact_description', 'contact_social_text'),
            'classes': ('collapse',),
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'instagram_url', 'facebook_url', 'telegram_url', 'whatsapp_url'),
            'classes': ('collapse',),
        }),
        ('Stats', {
            'fields': (('years_experience', 'projects_completed', 'happy_clients'),)
        }),
        ('Resume', {
            'fields': ('resume_url',),
            'classes': ('collapse',),
        }),
    )
    
    def delete_button(self, obj):
        url = reverse('admin:portfolio_profile_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'delete_button']
    list_filter = ['category']
    list_editable = ['order', 'proficiency']
    ordering = ['category__order', 'order']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_skill_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(BudgetOption)
class BudgetOptionAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'order']
    list_editable = ['order', 'value']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at', 'delete_button']
    list_filter = ['category', 'featured']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description', 'technologies']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_project_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date', 'is_current', 'delete_button']
    list_filter = ['is_current']
    ordering = ['-start_date']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_experience_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'delete_button']
    list_editable = ['order']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_service_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(PortfolioDocument)
class PortfolioDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'delete_button']
    search_fields = ['title']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_portfoliodocument_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'project_type', 'created_at', 'status_badge', 'is_read', 'has_reply', 'delete_button']
    list_filter = ['status', 'is_read', 'project_type', 'created_at']
    list_editable = []  # Remove editable because it might conflict with the colored badge
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'project_type', 'budget', 'created_at', 'replied_at']
    actions = ['send_reply_email']
    fieldsets = (
        ('Message Info', {
            'fields': (('name', 'email'), 'subject', 'message', ('project_type', 'budget'), 'created_at', 'is_read')
        }),
        ('Admin Reply - Write your reply below and SAVE to send email', {
            'fields': ('status', 'admin_reply', 'replied_at'),
            'description': '⚠️ When you save a reply, it will be automatically emailed to the customer!'
        }),
    )
    
    def has_reply(self, obj):
        return bool(obj.admin_reply)
    has_reply.boolean = True
    has_reply.short_description = 'Replied'

    def status_badge(self, obj):
        status_colors = {
            'pending': 'pending',
            'accepted': 'accepted',
            'completed': 'completed',
            'rejected': 'rejected',
        }
        color_class = status_colors.get(obj.status, 'pending')
        return format_html(
            '<span class="badge badge-{}">{}</span>',
            color_class,
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def delete_button(self, obj):
        url = reverse('admin:portfolio_contactmessage_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'
    
    @admin.action(description='📧 Send Reply Email to Selected Customers')
    def send_reply_email(self, request, queryset):
        sent = 0
        failed = 0
        admin_email = getattr(Profile.objects.first(), 'email', settings.DEFAULT_FROM_EMAIL)
        
        for msg in queryset:
            if msg.admin_reply:
                try:
                    email = EmailMessage(
                        subject=f'Re: {msg.subject}',
                        body=msg.admin_reply,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[msg.email],
                        reply_to=[admin_email],
                    )
                    email.send(fail_silently=False)
                    msg.replied_at = timezone.now()
                    msg.save()
                    sent += 1
                except Exception:
                    failed += 1
            else:
                failed += 1
        self.message_user(request, f'✅ Emails sent: {sent} | ❌ Failed: {failed}')
    
    def save_model(self, request, obj, form, change):
        if change and 'admin_reply' in form.changed_data and obj.admin_reply:
            obj.replied_at = timezone.now()
            # Send email to customer
            admin_email = getattr(Profile.objects.first(), 'email', settings.DEFAULT_FROM_EMAIL)
            try:
                email = EmailMessage(
                    subject=f'Re: {obj.subject}',
                    body=obj.admin_reply,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[obj.email],
                    reply_to=[admin_email],
                )
                email.send(fail_silently=False)
                self.message_user(request, f'✅ Reply sent to {obj.email}', level='SUCCESS')
            except Exception as e:
                self.message_user(request, f'❌ Email failed: {str(e)}', level='ERROR')
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_title', 'rating', 'is_active', 'order', 'delete_button']
    list_filter = ['is_active', 'rating']
    list_editable = ['is_active', 'order']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_testimonial_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'
