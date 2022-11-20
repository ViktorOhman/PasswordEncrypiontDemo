import pyautogui
from cryptography.fernet import Fernet

#Make a new function
def check_password(check):
    while check:
        wantToSee = pyautogui.confirm(text='Do you want to see your Password???', title='???', buttons=['YES', 'NO']) #Ask the user if they want to see the password
        if wantToSee == 'YES':
            wantToSee_2 = pyautogui.confirm(text='Are you really sure?', title='???', buttons=['YES', 'NO']) #Ask again
            if wantToSee_2 == 'YES':
                #Read the key and encrypted password
                with open("PasswordKey.key", "rb") as Key_F:
                    key = Key_F.read()
                with open("thepassword.txt", "rb") as password_F:
                    password_E = password_F.read()
                # Decrypt the encrypted password
                password = Fernet(key).decrypt(password_E)
                password = str(password) #Make the byte into a string for editing
                password = password[2:] #If we were toprint a Normal byte variable it would look something like this, b'Hello'
                password = password.replace("'","") #So we need to remove the b' that is in the beginning and then the ' at the end
                #Give the user the password
                pyautogui.alert(text=password, title='???', button='Ok')
                check = False
            else:
                pyautogui.alert(text='Ok', title='???', button='...')
                quit()
        else:
            pyautogui.alert(text='Ok', title='???', button='...')
            quit()

check_password(True)