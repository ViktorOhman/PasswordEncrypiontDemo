import pyautogui
from cryptography.fernet import Fernet
import time



def check_password(check):
    while check:
        wantToSee = pyautogui.confirm(text='Do you want to see your Password???', title='???', buttons=['YES', 'NO'])
        if wantToSee == 'YES':
            wantToSee_2 = pyautogui.confirm(text='Are you really sure?', title='???', buttons=['YES', 'NO'])
            if wantToSee_2 == 'YES':
                with open("PasswordKey.key", "rb") as Key_F:
                    key = Key_F.read()
                with open("thepassword.txt", "rb") as password_F:
                    password_E = password_F.read()
                password = Fernet(key).decrypt(password_E)
                password = str(password)
                password = password[2:]
                password = password.replace("'","")
                pyautogui.alert(text=password, title='???', button='Ok')
                check = False
            else:
                pyautogui.alert(text='Ok', title='???', button='...')
                quit()
        else:
            pyautogui.alert(text='Ok', title='???', button='...')
            quit()
check_password(True)