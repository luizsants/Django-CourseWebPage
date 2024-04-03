
from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', include('app.urls')),
    path('', views.home, name='root_home'),  # Define a separate URL pattern for the root URL
    # Add other URL patterns as needed
]