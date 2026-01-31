from .models import SiteContent


def site_content(request):
    """
    Context processor to make site content available in all templates.
    All visible text on the page can be edited by admin through SiteContent model.
    """
    try:
        content = SiteContent.get_instance()
    except Exception:
        content = None
    
    return {
        'site': content
    }
