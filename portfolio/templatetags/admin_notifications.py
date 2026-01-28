from django import template
from portfolio.models import ContactMessage

register = template.Library()

@register.simple_tag
def get_unread_messages_count():
    """Returns the count of unread contact messages"""
    try:
        return ContactMessage.objects.filter(is_read=False).count()
    except Exception:
        # Handle case where database tables don't exist yet
        return 0
