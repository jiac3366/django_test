from django.urls import path, include
from rest_framework.routers import DefaultRouter
from creatify_jwt import views

router = DefaultRouter()
views.register_routes(router)



urlpatterns = [
    
    path("signin/", views.JWTViewSet.as_view(), name="signin"),
    path("me/", views.SelfUserView.as_view(), name="me"),
    path("", include(router.urls)),
]
