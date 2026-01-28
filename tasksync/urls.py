from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Portfolio as main page
    path('tasksync/', include('core.urls')),  # Old app moved to /tasksync/
    
    # Media files for Render production (WhiteNoise handles static)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
