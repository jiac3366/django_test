from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from creatify_jwt.views import JWTViewSet

from creatify_jwt import views as creatify_jwt_views

router = DefaultRouter()
creatify_jwt_views.register_routes(router)



urlpatterns = [
    path("", include(router.urls)),
    path('signin/', JWTViewSet.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
