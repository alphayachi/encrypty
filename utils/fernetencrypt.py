from cryptography.fernet import Fernet


def fernetEncrypt(input_file, key, salt, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    encrypted = salt + encrypted

    with open(output_file, 'wb') as f:
        f.write(encrypted)
