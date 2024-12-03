"""product_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

"""
This file defines the URL routing for the Django project.

Routes:
- Admin route: Provides access to the admin interface.
- Login route: Redirects unauthenticated users to the login page.
- Logout route: Logs out users and redirects them to the login page.
- Catalog app route: Includes all URLs related to the catalog app.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('catalog/', include('catalog.urls')),
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)