from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Only if you're using views from this root-level file

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Example static pages or function-based views
    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('contact/', views.contact, name="contact"),

    path('intro/', views.intro, name="intro"),
    path('django/', include('hellotodjango.urls')),  # Delegates routing to app-level urls.py
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)