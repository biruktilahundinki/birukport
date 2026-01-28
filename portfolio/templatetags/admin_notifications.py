from django import template
from portfolio.models import ContactMessage

register = template.Library()

@register.simple_tag
def get_unread_messages_count():
    """Returns the count of unread contact messages"""
    return ContactMessage.objects.filter(is_read=False).count()
