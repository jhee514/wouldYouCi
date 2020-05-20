from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'accounts/view/', views.AccountViewSet, basename='test')
# router.register(r'admin', views.AdminUserViewSet)

urlpatterns = [
    # path('', views.signup),
    path('login/', obtain_jwt_token),
    path('', views.AccountView.as_view()),
    # path(r'^/test/', include(router.urls)),
] + [
    # Mixin
    # path('mixin/post/', views.PostListMixins.as_view()),
    # path('mixin/post/<int:pk>/', views.PostDetailMixins.as_view()),
]
