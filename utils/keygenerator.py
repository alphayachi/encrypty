import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# input password


def passgen(password_provided):
    password = password_provided.encode()
    salt = b'\xb0\xc9E\x01\xf7\xfe~\xa4\x15u\x89\x97\x04\x95\xdb8'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key
