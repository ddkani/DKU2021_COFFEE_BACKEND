"""market_damoa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


openapi_info = openapi.Info(
    title='커피두잔 API',
    default_version='v1',
    description='커피두잔 API Docs',
    contact=openapi.Contact(email='32187345@dankook.ac.kr'),
    license=openapi.License(name='License'),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    path('api/', include('market.urls')),

    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]
