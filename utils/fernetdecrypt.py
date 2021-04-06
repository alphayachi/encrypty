from cryptography.fernet import Fernet, InvalidToken


def fernetDecrypt(input_file, key, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)

    #output_file = f"Dec-{input_file}"

    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)

    except:
        print("Invalid Key")
