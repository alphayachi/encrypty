from cryptography.fernet import Fernet, InvalidToken
import PySimpleGUI as sg


def fernetDecrypt(input_file, key, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    actualdata = data[16:]
    fernet = Fernet(key)

    #output_file = f"Dec-{input_file}"

    try:

        decrypted = fernet.decrypt(actualdata)

        with open(output_file, 'wb') as f:
            f.write(decrypted)

    except:
        print("Invalid Key")
        layout = [sg.Text("INVALID KEY"), ]
        sg.popup('INVALID KEY')
