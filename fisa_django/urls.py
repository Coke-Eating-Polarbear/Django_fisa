"""
URL configuration for fisa_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# 이미지 업로드 필드를 위한 추가
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),  # locahost:8000/blog/실제blog/urls.py에 적힌 경로
    # path("account/", include('account.urls')),
    path('accounts/', include('allauth.urls')),
    # path("", include('blog.urls')),   # localhost:8000/
] + debug_toolbar_urls()

# django_project/urls.py에 추가
# python -m pip install Pillow



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)