#!/bin/python

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

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

# Main
option_1 = '1- Encrypt Message'
option_2 = '2- Decrypt Message'
option_3 = '3- Encrypt File'
option_4 = '4- Decrypt File'
option_5 = '5- Encrypt all the Files in a directory'
option_6 = '6- Decrypt all the Files in a directory'
option_7 = '7- Encrypt File with PBKDF2'
option_8 = '8- Encrypt File with PBKDF2'
print('''       Menu Options:
{}
{}
{}
{}
{}
{}
{}
{}
      
PBKDF2: password-based key derivation function       
'''.format(option_1, option_2, option_3, option_4, option_5, option_6, option_7, option_8))

menu_option = input("Please choose the desired menu option (1-8): ") 

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

else:
    print("\nYou did not choose an available option. Goodbye!")



