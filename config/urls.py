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
from django.utils.translation import gettext_lazy as _
from django.urls import path, include, reverse_lazy
from config.graphql import CustomAsyncGraphQLView
from config.schema import schema
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps.country.views import (
    CountryViewSet,
    CountryAdditionalInfoViewSet
)

from apps.common import views

router = DefaultRouter()
router.register("countries", CountryViewSet, "countries-view")
country_router = NestedDefaultRouter(router, "countries", lookup="id")
country_router.register('addtional-info', CountryAdditionalInfoViewSet)

# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", CustomAsyncGraphQLView.as_view(schema=schema, graphiql=False)),
    path('api/', include(router.urls)),
    path('tinymce/', include('tinymce.urls')),

    path('admin/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        'password/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('login'),
        ),
        name='password_reset_confirm'
    ),
]
# Enable graphiql in development server only
if settings.DEBUG:
    urlpatterns.append(path("graphiql/", CustomAsyncGraphQLView.as_view(schema=schema)))
admin.site.site_header = _('IDMC Country Profile and Global Repository Admin')

# Static and media file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
