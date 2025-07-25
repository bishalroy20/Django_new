"""
URL configuration for ecom project.

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
from django.urls import path , include
from core.views import home , CarDetailView , search_products , filter_by_category , productlist , contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('contact/', contact , name='contact'),
    path('productlist/', productlist , name='productlist'),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),
    path('',include('payment.urls')),
    path('category/<slug:category_slug>/', filter_by_category, name='brand_wise'),
    path('details/<int:id>/', CarDetailView.as_view() , name='detailview'),
    path('search/', search_products, name='search_products'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

