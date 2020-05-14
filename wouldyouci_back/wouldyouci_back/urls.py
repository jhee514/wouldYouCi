from django.contrib import admin
from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('api-token/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
