from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Service, ContactMessage, Testimonial, PortfolioDocument
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'location', 'email', 'phone', 'telegram_url', 'whatsapp_url', 'delete_button']
    
    def delete_button(self, obj):
        url = reverse('admin:portfolio_profile_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'delete_button']
    list_filter = ['category']
    list_editable = ['order', 'proficiency']
    ordering = ['order']

    def delete_button(self, obj):
        url = reverse('admin:portfolio_skill_delete', args=[obj.pk])
        return format_html('<a class="deletelink" href="{}">Delete</a>', url)
    delete_button.short_description = 'Action'


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
