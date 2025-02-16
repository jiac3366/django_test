from django.db import models

from creatify_jwt.hasher import hashers, make_password, check_password


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def hash_password(password: str) -> str:
        return make_password(password)

    def check_password(self, password: str) -> bool:
        return check_password(password, self.password)


def make_password(password: str, algorithm: str = "pbkdf2_sha256") -> str:
    """Make password hash from password and algorithm."""
    hasher = hashers[algorithm]()
    salt = hasher.salt()
    return hasher.encode(password, salt)
