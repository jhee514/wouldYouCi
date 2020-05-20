from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'admin', views.AdminUserViewSet)

urlpatterns = [
    # path('', views.signup),
    path('', include(router.urls)),
] + [
    # Mixin
    path('mixin/post/', views.PostListMixins.as_view()),
    # path('mixin/post/<int:pk>/', views.PostDetailMixins.as_view()),
]
