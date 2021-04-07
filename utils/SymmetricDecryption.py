import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def aesDecrypt(input_file, key, output_file):
    data = input_file
    actualdata = data[16:-16]
    iv = data[-16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(actualdata) + decryptor.finalize()
    with open(output_file, 'wb') as f:
        f.write(decrypted)
