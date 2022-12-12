"""config URL Configuration

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
from django.utils.translation import gettext_lazy as _
from config.graphql import CustomAsyncGraphQLView
from config.schema import schema
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from apps.country.views import (
    CountryViewSet,
    ConflictViewSet,
    DisasterViewSet,
    CountryAdditionalInfoViewSet
)

router = DefaultRouter()
router.register("countries", CountryViewSet, "countries-view")
country_router = NestedDefaultRouter(router, "countries", lookup="id")
country_router.register('addtional-info', CountryAdditionalInfoViewSet)
router.register("conflicts", ConflictViewSet, "conflicts-view")
router.register("disasters", DisasterViewSet, "diasters-view")

# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", CustomAsyncGraphQLView.as_view(schema=schema, graphiql=False)),
    path('api/', include(router.urls)),
    path('tinymce/', include('tinymce.urls')),
]
# Enable graphiql in development server only
if settings.DEBUG:
    urlpatterns.append(path("graphiql/", CustomAsyncGraphQLView.as_view(schema=schema)))
admin.site.site_header = _('IDMC Country Profile and Global Repository Admin')

# Static and media file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
