import PySimpleGUI as sg
import os.path

from utils.keygenerator import passgen
from utils.fernetencrypt import fernetEncrypt
from utils.fernetdecrypt import fernetDecrypt


def EncryptoMeter():

    # layout the form

    prm_layout = [
        [sg.ProgressBar(1, orientation='h', size=(20, 20), key='-PROGRESS-')]]

    # create the form
    prm_window = sg.Window('Encrypting').Layout(prm_layout)
    progress_bar = prm_window.FindElement('progress')

    while i < 400:
        event, values = prm_window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+1, 4000)

    if event == 'Cancel' or event == None:
        break
    # loop that would normally do something useful
    for i in range(4000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = prm_window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+1, 4000)
    # done with loop... need to destroy the window as it's still open
    prm_window.Close()
