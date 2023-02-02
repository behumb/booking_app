from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view as get_swagger_view
from drf_yasg import openapi

schema_view = get_swagger_view(
    openapi.Info(
        title='Booking API',
        default_version='1.0.0',
        description='API documentation'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/restaurants/', include('apps.restaurants.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),

]
