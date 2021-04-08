import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import PySimpleGUI as sg
from cryptography.fernet import Fernet


def fernetEncrypt(input_file, key, salt, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    encrypted = salt + encrypted

    with open(output_file, 'wb') as f:
        f.write(encrypted)


def aesEncrypt(input_file, key, salt, output_file):
    print("AES-CBC ENCRYPTION")
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()

    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    encrypted = salt + encrypted + iv

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print("AES-CBC ENCRYPTION SUCCESSFUL")


def chacha20poly1305Encrypt(input_file, key, salt, aad, output_file):
    print("ChaCha20Poly1305 ENCRYPTION")

    with open(input_file, 'rb') as f:
        data = f.read()
    print("creating chacha instance")
    #key = ChaCha20Poly1305.generate_key()
    chacha = ChaCha20Poly1305(key)
    print("generating nonce")
    nonce = os.urandom(12)
    print("encrypting using chacha")
    encrypted = chacha.encrypt(nonce, data, aad)
    print("adding salt and nonce")
    encrypted = salt + encrypted + nonce
    print("writing bytes")
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print("CHACHA20POLY1305 ENCRYPTION SUCCESSFUL")
