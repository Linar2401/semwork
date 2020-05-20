"""SemWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from utils.views import *

app_name = 'utils'

urlpatterns = [
    path('sign_up/', RegView.as_view(), name="sign_up"),
    path('sign_in/', SignInView.as_view(), name="sign_in"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('authors_list/', AllUsers.as_view(), name="list"),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    re_path('author/(?P<id>[0-9]+)', AnotherProfileView.as_view(), name="author_profile"),
    path('', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)