"""donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

from donation.auth.views import UserLoginView, registerView, logoutView, PasswordChangeView, createAdmin
from donation.auth.forms import UserLoginForm, CustomPasswordResetForm, CustomPasswordChangeForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('project.urls')),

    path('accounts/login/', UserLoginView.as_view(redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),
    path('accounts/register/', registerView, name='register'),
    path('accounts/criarAdmin/', createAdmin, name='criarAdmin'),
    path('accounts/logout/', logoutView, name='logout'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='password_reset'),
    path('accounts/password_change/', PasswordChangeView.as_view(form_class=CustomPasswordChangeForm), name='password_change'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
