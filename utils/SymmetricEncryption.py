import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def aesEncrypt(input_file, key, salt, output_file):
    #key = b'S\x04\xe5s\x12\xdb\xbac;A%"\x9c\xb1Y\x92'
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
