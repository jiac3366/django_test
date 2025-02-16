from django.shortcuts import render
from rest_framework import viewsets, views
from creatify_jwt.models import User
from creatify_jwt.serializers import UserSerializer, JWTSerializer
from rest_framework.routers import BaseRouter
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"], url_path="signup")
    def create_user(self, request):
        return super().create(request)


class JWTViewSet(TokenViewBase):  # generics.GenericAPIView
    serializer_class = JWTSerializer



def register_routes(router: BaseRouter):
    router.register("", UserViewSet, basename="user")


class SelfUserView(views.APIView):
    permission_classes = []

    def get(self, request):
        # get header from request
        serializer = UserSerializer(request.user)
        return Response({
            "id": serializer.data["id"],
            "email": serializer.data["email"]
        })