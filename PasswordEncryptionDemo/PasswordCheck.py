import pyautogui
from cryptography.fernet import Fernet
import time
#Read the key
with open("PasswordKey.key", "rb") as key_file:
    key = key_file.read()
#Make a new function
def decrypt(check):
    while check:
        #Ask for password
        I_password = pyautogui.prompt(text='Put in your password', title='Password checker')
        I_password = str(I_password) #We have to make it into a string becuse if the user preses cancel it returns None as a NoType
        if I_password == 'None':
            pass
        else:
            #Read the encrypted password from last script
            with open("thepassword.txt", "rb") as password_F:
                password = password_F.read()
            I_password_DC = Fernet(key).decrypt(password) #Decrypt it
            I_password = bytes(I_password, 'utf-8') #Tranform our inputed password into bytes
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
