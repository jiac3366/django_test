from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from creatify_jwt import views

router = DefaultRouter()
views.register_routes(router)



urlpatterns = [
    path("", include(router.urls)),
    path("token/signin/", views.JWTViewSet.as_view(), name="signin"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
