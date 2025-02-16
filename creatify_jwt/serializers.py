from rest_framework import serializers
from creatify_jwt.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "created_at", "updated_at"]
        read_only_fields = ["id", "email"]


    def create(self, validated_data: dict) -> User:
        validated_data["password"] = User.hash_password(validated_data["password"])
        return super().create(validated_data)


def authenticate(email: str, password: str, **kwargs) -> User:
    user = User.objects.get(email=email)
    if not user.check_password(password):
        raise serializers.ValidationError("Invalid credentials")
    return user



class JWTSerializer(TokenObtainPairSerializer):
    username_field = "email"
    
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    
    
    def validate(self, attrs: dict) -> dict:
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }

        self.user = authenticate(**authenticate_kwargs)

        data = {}
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
