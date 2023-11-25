"""toplearn_eshop URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

from franc import settings
from .views import home_page , Header , Footer,about_us

urlpatterns = [
    path('', home_page),
    path('', include('franc_account.urls')),
    path('', include('franc_products.urls')),
    path('', include('france_contact.urls')),
    path('', include('franc_order.urls')),
    path('about-us',about_us),
    path('Header',Header, name="header"),
    path('Footer',Footer, name="Footer"),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
