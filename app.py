

import PySimpleGUI as sg
import os.path

from utils.keygenerator import *
#from utils.fernetencrypt import fernetEncrypt
#from utils.fernetdecrypt import fernetDecrypt
from utils.SymmetricEncryption import *
from utils.SymmetricDecryption import *


sg.theme('Reddit')


file_column = [
    [sg.Image(key="-FILE IMAGE-", filename=os.path.join(os.getcwd(),
              "assets", "file.png"), pad=(0, (0, 10)))],
    [sg.Text(key="-UPLOADED FILE-", size=(40, 1), auto_size_text=True, font=('courier', 15),
             justification='center', pad=(0, (0, 30)))],
    [
        sg.Text(text="Choose a file to encrypt/decrypt",
                font=('Arial', 11)),
        sg.In(size=(25, 1), enable_events=True,
              key="-FILE-", visible=False),
        sg.FileBrowse("Browse", font=('Arial', 11), size=(15, 2)),
    ],
    [sg.Checkbox("What are my options", font=(
        'Arial', 11), enable_events=True, key="-ADVANCED SETTINGS-", pad=(0, (30, 7)))],
    [sg.Combo(['Fernet (recommended)', 'AES-CBC', 'ChaCha20Poly1305', 'AES-GCM'],
              default_value='Fernet (recommended)', enable_events=True, key="-CIPHER CHOICE-", disabled=True)],
    [sg.Checkbox("Help me out here please", font=(
                 'Arial', 11), enable_events=True, key="-INSTRUCTIONS BOOL-", pad=(0, (15, 15)))],
    [sg.Multiline(default_text="INSTRUCTIONS \n\n1. Choose a file from your computer. \n\n2. (Not necessary) Select 'I know what I am doing' if you want to choose your own cipher. \n\n3. Set password (at least 7 characters). In some ciphers you might need to enter an associated data. \n\n4. Choose whether you want to Encrypt/Decrypt the file and choose the save directory. ",
                  size=(40, 8), disabled=True, font='courier', key='-INSTRUCTIONS-', auto_size_text=True, visible=False)],
]


password_column = [
    [sg.Image(key="-ENCRYPTED IMAGE-", filename=os.path.join(os.getcwd(),
              "assets", "key-lock.png"))],
    [sg.Text(key="-ENC FILE-", size=(40, 1), auto_size_text=True,
             font=('courier', 15), pad=(0, (0, 30)), justification='center')],
    [sg.ProgressBar(1, orientation='h', size=(20, 20),
                    key='-PROGRESS-', visible=False, pad=((60, 0), (0, 20)))],
    [sg.Text("Password", key="-PASSWORD TEXT-", font=('Arial', 11), size=(8, 1)),
     sg.Input(password_char="*", key="-PASSWORD INPUT-", size=(40, 1), pad=((0, 40), 0), disabled=True)],
    [sg.Text("Please enter the associated data:",
             key="-AAD TEXT-", font=('Arial', 11), pad=(0, (20, 10)), visible=False)],
    [sg.Multiline(key="-AAD-", size=(30, 4), pad=((10, 0), (0, 20)),
                  visible=False, disabled=True, font='courier', auto_size_text=True)],
    [sg.Text("*Password length should be atleast 7", font=(
        'Arial', 9), key="-ERR PASSLEN-", visible=False, justification='right')],
    [sg.Text("*Choose a file first", font=('Arial', 9),
             key="-ERR NOFILE-", visible=False, justification='right')],
    [sg.Input(key="-ENCRYPT-", visible=False, enable_events=True),
     sg.SaveAs("Encrypt", key="-ENCRYPT BTN-", font=('Arial', 11), size=(15, 2), pad=(0, (20, 10)), disabled=True)],
    [sg.Input(key="-DECRYPT-", visible=False, enable_events=True),
     sg.SaveAs("Decrypt", key="-DECRYPT BTN-", font=('Arial', 11), size=(15, 2), pad=(0, 10), disabled=True)],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_column,
                  element_justification='center', size=(450, 550), pad=(0, 30)),
        sg.VSeperator(),
        sg.Column(password_column,
                  element_justification='center', size=(450, 550), pad=(0, 30)),
    ]
]

window = sg.Window("ENCRYPTY", layout)

# Run the Event Loop
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FILE-":
        print("Browsing folder")
        file = values["-FILE-"]
        print(file)
        try:
            print("getting file name")
            if file:
                file_name, ext = os.path.splitext(file)
                window["-UPLOADED FILE-"].update(os.path.basename(file))
                window["-ERR NOFILE-"].update(visible=False)
                window["-ERR PASSLEN-"].update(visible=False)
                window["-ENCRYPT BTN-"].update(disabled=False)
                window["-DECRYPT BTN-"].update(disabled=False)
                window["-PASSWORD INPUT-"].update(disabled=False)
                window["-AAD-"].update(disabled=False)
        except:
            print("error in listing files of this directory")

        print("file selected")

    elif event == "-ENCRYPT-":  # A file was chosen from the listbox to encrypt
        print("Encrypting event")
        try:

            input_file = values["-FILE-"]
            password_provided = values["-PASSWORD INPUT-"]
            output_file = values["-ENCRYPT-"]
            filename, extension = os.path.splitext(input_file)

            if len(password_provided) >= 7 and input_file and output_file:
                window["-ERR NOFILE-"].update(visible=False)
                of = os.path.basename(output_file)
                of += extension
                window["-ENC FILE-"].update(of)
                print("Adding extension")
                output_file += extension
                print(output_file)
                window["-ERR PASSLEN-"].update(visible=False)
                window["-PASSWORD INPUT-"].update("")
                window["-AAD-"].update("")
                print("starting progress bar")
                # window["-PROGRESS-"].update(visible=True)
                print("Encrypting ....")

                for i in range(4000):
                    if i == 1000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            key, salt = passgen(password_provided, 16)
                        elif values["-CIPHER CHOICE-"] == "ChaCha20Poly1305" and values["-ADVANCED SETTINGS-"]:
                            key, salt = chachaPassgen(password_provided, 32)
                        elif values["-CIPHER CHOICE-"] == "AES-GCM" and values["-ADVANCED SETTINGS-"]:
                            key, salt = chachaPassgen(password_provided, 32)
                            print("pass generated ********")
                        else:
                            key, salt = passgen(password_provided, 32)

                    if i == 3000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            aesEncrypt(input_file, key, salt, output_file)
                        elif values["-CIPHER CHOICE-"] == "ChaCha20Poly1305" and values["-ADVANCED SETTINGS-"]:
                            aadmessage = values["-AAD-"]
                            aad = aadmessage.encode()
                            chacha20poly1305Encrypt(
                                input_file, key, salt, aad, output_file)
                        elif values["-CIPHER CHOICE-"] == "AES-GCM" and values["-ADVANCED SETTINGS-"]:
                            aadmessage = values["-AAD-"]
                            aad = aadmessage.encode()
                            aesgcmEncrypt(input_file, key, salt,
                                          aad, output_file)
                        else:
                            fernetEncrypt(input_file, key, salt, output_file)
                    i = i+1
                    window["-PROGRESS-"].update(i+1, 4000, visible=True)

                print("Successful Encryption")
                window["-PROGRESS-"].update(1, 4000, visible=False)
                window["-ENCRYPT-"].update("")
                output_file = ''
            elif not input_file or not output_file:
                window["-ERR NOFILE-"].update(visible=True)
            elif len(password_provided) < 7:
                window["-ERR PASSLEN-"].update(visible=True)

        except:
            print("Failed Encryption")

    elif event == "-DECRYPT-":
        print("Decrypting event")
        try:
            input_file = values["-FILE-"]
            # filename = 'D:/VS Codes/Encrypt/test.txt'
            password_provided = values["-PASSWORD INPUT-"]
            output_file = values["-DECRYPT-"]
            filename, extension = os.path.splitext(input_file)

            if input_file and output_file:
                window["-ERR NOFILE-"].update(visible=False)
                print("Adding extension")
                output_file += extension
                print(output_file)

                with open(file, 'rb') as f:
                    data = f.read()
                salt = data[:16]

                window["-PASSWORD INPUT-"].update("")
                window["-AAD-"].update("")
                # fernetDecrypt(input_file, password, output_file)

                for i in range(4000):
                    if i == 700:
                        with open(file, 'rb') as f:
                            data = f.read()
                        salt = data[:16]
                    if i == 1500:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            key = decPassgen(password_provided, 16, salt)
                        elif values["-CIPHER CHOICE-"] == "ChaCha20Poly1305" and values["-ADVANCED SETTINGS-"]:
                            key = chachadecPassgen(password_provided, 32, salt)
                        elif values["-CIPHER CHOICE-"] == "AES-GCM" and values["-ADVANCED SETTINGS-"]:
                            key = chachadecPassgen(password_provided, 32, salt)
                        else:
                            key = decPassgen(password_provided, 32, salt)

                    if i == 3000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            aesDecrypt(data, key, output_file)
                        elif values["-CIPHER CHOICE-"] == "ChaCha20Poly1305" and values["-ADVANCED SETTINGS-"]:
                            aadmessage = values["-AAD-"]
                            aad = aadmessage.encode()
                            chacha20poly1305Decrypt(
                                data, key, aad, output_file)
                        elif values["-CIPHER CHOICE-"] == "AES-GCM" and values["-ADVANCED SETTINGS-"]:
                            aadmessage = values["-AAD-"]
                            aad = aadmessage.encode()
                            aesgcmDecrypt(data, key, aad, output_file)
                        else:
                            fernetDecrypt(input_file, key, output_file)

                    i = i+1
                    window["-PROGRESS-"].update(i+1, 4000, visible=True)

                print("Successful Decryption")
                output_file = ''
                window["-DECRYPT-"].update("")
                window["-PROGRESS-"].update(1, 4000, visible=False)
            else:
                window["-ERR NOFILE-"].update(visible=True)

        except:
            print("Failed Encryption")

    elif event == "-ADVANCED SETTINGS-":
        if values["-ADVANCED SETTINGS-"]:
            window["-CIPHER CHOICE-"].update(disabled=False, readonly=True)
        else:
            window["-CIPHER CHOICE-"].update(
                value="Fernet (recommended)", disabled=True)
            window["-AAD-"].update(visible=False)
            window["-AAD TEXT-"].update(visible=False)
    elif event == "-CIPHER CHOICE-":
        if values["-CIPHER CHOICE-"] == "ChaCha20Poly1305" or values["-CIPHER CHOICE-"] == "AES-GCM":
            window["-AAD-"].update(visible=True)
            window["-AAD TEXT-"].update(visible=True)
        else:
            window["-AAD-"].update(visible=False)
            window["-AAD TEXT-"].update(visible=False)

    elif event == "-INSTRUCTIONS BOOL-":
        if values["-INSTRUCTIONS BOOL-"]:
            window["-INSTRUCTIONS-"].update(visible=True)
        else:
            window["-INSTRUCTIONS-"].update(visible=False)

    print(event, values)

window.close()
