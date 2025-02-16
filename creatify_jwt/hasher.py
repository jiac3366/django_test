import abc
import base64
import hashlib
import hmac
import secrets
import string
from typing import Dict, Optional

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ALLOWED_SYMBOLS = "!@#$%&*_-"


class BasePasswordHasher(metaclass=abc.ABCMeta):
    salt_length = 22

    @abc.abstractmethod
    def verify(self, password: str, encoded: str) -> bool:
        """Check if the given password is correct."""

    @abc.abstractmethod
    def encode(self, password: str, salt: str) -> str:
        """
        Create an encoded database value.

        The result is normally formatted as "algorithm$salt$hash" and
        must be fewer than 128 characters.
        """

    def salt(self) -> str:
        """Generate a random salt with a fixed length"""
        return "".join(secrets.choice(ALLOWED_CHARS) for _ in range(self.salt_length))


class PBKDF2PasswordHasher(BasePasswordHasher):
    algorithm = "pbkdf2_sha256"
    iterations = 260000
    digest = hashlib.sha256

    def verify(self, password: str, encoded: str) -> bool:
        decoded = self.decode(encoded)
        encoded_2 = self.encode(password, decoded["salt"], decoded["iterations"])
        return hmac.compare_digest(encoded, encoded_2)

    def encode(self, password: str, salt: str, iterations: Optional[int] = None) -> str:
        iterations = iterations or self.iterations
        hash_bytes = hashlib.pbkdf2_hmac(
            self.digest().name, password.encode("utf8"), salt.encode("utf8"), iterations
        )
        hash = base64.b64encode(hash_bytes).decode("ascii").strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)

    def decode(self, encoded: str) -> Dict[str, str]:
        algorithm, iterations, salt, hash = encoded.split("$", 3)
        assert algorithm == self.algorithm
        return {
            "algorithm": algorithm,
            "hash": hash,
            "iterations": int(iterations),
            "salt": salt,
        }


hashers = {PBKDF2PasswordHasher.algorithm: PBKDF2PasswordHasher}


def make_password(password: str, algorithm: str = "pbkdf2_sha256") -> str:
    """Make password hash from password and algorithm."""
    hasher = hashers[algorithm]()
    salt = hasher.salt()
    return hasher.encode(password, salt)


def check_password(password: str, encoded: str) -> bool:
    """Check if password is correct."""
    hasher = hashers[encoded.split("$", 1)[0]]()
    return hasher.verify(password, encoded)


def _validate_password(password: str) -> bool:
    if set(string.digits).isdisjoint(password):
        return False
    if set(string.ascii_lowercase).isdisjoint(password):
        return False
    if set(string.ascii_uppercase).isdisjoint(password):
        return False
    if set(ALLOWED_SYMBOLS).isdisjoint(password):
        return False
    return True


def get_random_password(length: int = 12) -> str:
    """Generate a random password."""
    for _ in range(100):
        password = "".join(
            secrets.choice(ALLOWED_CHARS + ALLOWED_SYMBOLS) for _ in range(length)
        )
        if _validate_password(password):
            return password
    raise RuntimeError("Unable to generate a random password in limited attempts.")
