import pyautogui
from cryptography.fernet import Fernet
import time

with open("PasswordKey.key", "rb") as key_file:
    key = key_file.read()

def decrypt(check):
    while check:
        I_password = pyautogui.prompt(text='Put in your password', title='Password checker')
        I_password = str(I_password)
        if I_password == 'None':
            pass
        else:
            with open("thepassword.txt", "rb") as password_F:
                password = password_F.read()
            I_password_DC = Fernet(key).decrypt(password)
            I_password = bytes(I_password, 'utf-8')
            if I_password_DC == I_password:
                print('U are correct!')
                print(I_password_DC)
                time.sleep(10)
                check = False
            else:
                print('Wrong!')
                print(I_password_DC)
                time.sleep(5)
                quit()

decrypt(True)