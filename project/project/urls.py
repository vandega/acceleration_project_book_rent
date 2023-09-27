from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from django.contrib import admin
from django.urls import path, include


schema_view = swagger_get_schema_view(openapi.Info(
    title="acceleration 2th tour project",
    default_version="0.1",
    description="API for book giveaway, user registration"
), public=True)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/member/', include('member.urls')),
    path('api/giveaway/', include('giveaway.urls'))
]
