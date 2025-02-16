from rest_framework import serializers
from creatify_jwt.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "created_at", "updated_at"]



class JWTSerializer(TokenObtainPairSerializer):
    username_field = "email"