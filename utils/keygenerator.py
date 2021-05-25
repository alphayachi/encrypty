import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
# input password


def passgen(password_provided, passlen):
    password = password_provided.encode()
    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=passlen,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key, salt


def decPassgen(password_provided, passlen, salt):
    password = password_provided.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=passlen,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def chachaPassgen(password_provided, passlen):
    password = password_provided.encode()
    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=passlen,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)
    return key, salt


def chachadecPassgen(password_provided, passlen, salt):
    password = password_provided.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=passlen,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)
    return key


# def aesgcmPassgen(password_provided, passlen):
#     password = password_provided.encode()
#     salt = os.urandom(16)

#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256,
#         length=passlen,
#         salt=salt,
#         iterations=100000,
#     )
#     key = kdf.derive(password)
#     return key, salt


# def aesgcmPassgen(password_provided, passlen, salt):
#     password = password_provided.encode()

#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256,
#         length=passlen,
#         salt=salt,
#         iterations=100000,
#     )
#     key = kdf.derive(password)
#     return key
