from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="WouldYouCi API",
      default_version='v1',
      description="우리 주변 씨네마 API",
      contact=openapi.Contact(email="jay.hyundong@gmail.com"),
      license=openapi.License(name="SSAFY License"),
   ),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('accounts.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
