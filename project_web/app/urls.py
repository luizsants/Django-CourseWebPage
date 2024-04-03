from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='home'),  # Define a view named 'home'
    path('admin/', admin.site.urls),
    # Add other URL patterns as needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)