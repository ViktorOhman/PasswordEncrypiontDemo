import pyautogui
from cryptography.fernet import Fernet

#New function
def encrypt(check):
    key = Fernet.generate_key()  # Generate a key
    with open("PasswordKey.key", "wb") as keyfile:  # Writte the key to a File
        keyfile.write(key)
    while check:
        #Ask for the password using pyautogui
        password = pyautogui.password(text='Input Your desired password (No Special Characters)', title='Password Encrypter', mask='*')
        paasword_C = pyautogui.confirm(text='Is this your Password? \n\n' + password, title='???', buttons=['YES', 'NO']) #This Line returns YES or NO

        if paasword_C == 'YES':
            password = bytes(password, 'utf-8') #For encryption the string must be tranformed into bytes
            password_E = Fernet(key).encrypt(password) # Encrypt the password using our key
            #Write the password to a file
            with open("thepassword.txt", "wb") as passwordfile:
                passwordfile.write(password_E)
            pyautogui.alert(text='All Done', title='???', button='Good')
            quit()



encrypt(True)

