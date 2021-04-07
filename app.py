

import PySimpleGUI as sg
import os.path

from utils.keygenerator import passgen, decPassgen
from utils.fernetencrypt import fernetEncrypt
from utils.fernetdecrypt import fernetDecrypt
from utils.SymmetricEncryption import aesEncrypt
from utils.SymmetricDecryption import aesDecrypt


sg.theme('Reddit')


file_column = [
    [sg.Image(key="-FILE IMAGE-", pad=(0, (0, 10)))],
    [sg.Text(key="-UPLOADED FILE-", size=(40, 1), auto_size_text=True, font=('Helvetica', 15),
             justification='center', pad=(0, (0, 30)))],
    [
        sg.Text(text="Choose a file to encrypt/decrypt",
                font=('Helvetica', 11)),
        sg.In(size=(25, 1), enable_events=True,
              key="-FILE-", visible=False),
        sg.FileBrowse("Browse", font=('Helvetica', 11), size=(15, 2)),
    ],
    [sg.Checkbox("I know what I am doing", font=(
        'Helvetica', 11), enable_events=True, key="-ADVANCED SETTINGS-", pad=(0, (30, 15)))],
    [sg.Combo(['Fernet (recommended)', 'AES-CBC'], default_value='Fernet (recommended)',
              size=(30, 2), enable_events=True, key="-CIPHER CHOICE-", visible=False)],
]


password_column = [
    [sg.Image(key="-ENCRYPTED IMAGE-", pad=(0, (0, 40)))],
    [sg.ProgressBar(1, orientation='h', size=(20, 20),
                    key='-PROGRESS-', visible=False, pad=((60, 0), (0, 20)))],
    [sg.Text("Password", key="-PASSWORD TEXT-", font=('Helvetica', 11), size=(8, 1)),
     sg.Input(password_char="*", key="-PASSWORD INPUT-", size=(40, 1))],
    [sg.Text("*Password length should be atleast 7", font=(
        'Helvetica', 9), key="-ERR PASSLEN-", visible=False, justification='right')],
    [sg.Text("*Choose a file first", font=('Helvetica', 9),
             key="-ERR NOFILE-", visible=False, justification='right')],
    [sg.Input(key="-ENCRYPT-", visible=False, enable_events=True),
     sg.SaveAs("Encrypt", key="-ENCRYPT BTN-", font=('Helvetica', 11), size=(15, 2), pad=(0, (20, 10)))],
    [sg.Input(key="-DECRYPT-", visible=False, enable_events=True),
     sg.SaveAs("Decrypt", key="-DECRYPT BTN-", font=('Helvetica', 11), size=(15, 2), pad=(0, 10))],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_column,
                  element_justification='center', size=(450, 400), pad=(0, 30)),
        sg.VSeperator(),
        sg.Column(password_column,
                  element_justification='center', size=(450, 400), pad=(0, 30)),
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
                file_img = os.path.join(os.getcwd(), "assets", "file.png")
                enc_img = os.path.join(os.getcwd(), "assets", "key-lock.png")
                file_name, ext = os.path.splitext(file)
                window["-FILE IMAGE-"].update(filename=file_img)
                window["-ENCRYPTED IMAGE-"].update(filename=enc_img)
                window["-UPLOADED FILE-"].update(os.path.basename(file))
                window["-ERR NOFILE-"].update(visible=False)
                window["-ERR PASSLEN-"].update(visible=False)
                window["-ENCRYPT BTN-"].update(file_types=(('PNG', ext),))
                window["-DECRYPT BTN-"].update(file_types=(('PNG', ext),))
        except:
            print("error in listing files of this directory")

        print("file selected")

    elif event == "-ENCRYPT-":  # A file was chosen from the listbox to encrypt
        print("Encrypting event")
        try:
            # input_file = os.path.join(
            #    values["-FOLDER-"], values["-FILE LIST-"][0]
            # )
            # filename = 'D:/VS Codes/Encrypt/test.txt'
            input_file = values["-FILE-"]

            password_provided = values["-PASSWORD INPUT-"]
            output_file = values["-ENCRYPT-"]
            filename, extension = os.path.splitext(input_file)
            print("Adding extension")
            output_file += extension
            print(output_file)
            if len(password_provided) >= 7 and input_file:
                window["-ERR PASSLEN-"].update(visible=False)

                window["-PASSWORD INPUT-"].update("")
                print("starting progress bar")
                # window["-PROGRESS-"].update(visible=True)
                print("Encrypting ....")

                for i in range(4000):
                    if i == 1000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            key, salt = passgen(password_provided, 16)
                        else:
                            key, salt = passgen(password_provided, 32)

                    if i == 3000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            aesEncrypt(input_file, key, salt, output_file)
                        else:
                            fernetEncrypt(input_file, key, salt, output_file)
                    i = i+1
                    window["-PROGRESS-"].update(i+1, 4000, visible=True)

                print("Successful Encryption")
                window["-PROGRESS-"].update(1, 4000, visible=False)
            elif not input_file:
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
            print("Adding extension")
            output_file += extension
            print(output_file)
            if len(password_provided) >= 7 and input_file:
                with open(file, 'rb') as f:
                    data = f.read()
                salt = data[:16]

                window["-PASSWORD INPUT-"].update("")
                # fernetDecrypt(input_file, password, output_file)

                for i in range(4000):
                    if i == 700:
                        with open(file, 'rb') as f:
                            data = f.read()
                        salt = data[:16]
                    if i == 1500:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            key = decPassgen(password_provided, 16, salt)
                        else:
                            key = decPassgen(password_provided, 32, salt)

                    if i == 3000:
                        if values["-CIPHER CHOICE-"] == "AES-CBC" and values["-ADVANCED SETTINGS-"]:
                            aesDecrypt(data, key, output_file)
                        else:
                            fernetDecrypt(input_file, key, output_file)

                    i = i+1
                    window["-PROGRESS-"].update(i+1, 4000, visible=True)

                print("Successful Decryption")
                window["-PROGRESS-"].update(1, 4000, visible=False)

        except:
            print("Failed Encryption")

    elif event == "-ADVANCED SETTINGS-":
        if values["-ADVANCED SETTINGS-"]:
            window["-CIPHER CHOICE-"].update(visible=True)
        else:
            window["-CIPHER CHOICE-"].update(
                value="Fernet (recommended)", visible=False)

    print(event, values)

window.close()
