# Author: Habraino de Deus
# Email: habraino12@gmail.com
# Date: 13-10-2023

# function to show main menu
def showMainMenu():
    print('''
    WELCOME TO MY WORLD OF CRYPTOGRAPHY
    
    [1]: Encrypt/Decrypt Files
    [2]: Encrypt/Decrypt Message
    ''')

    return int(input('What you wanna do? '))

# function to show menu
def showMenu():
    print('''
    CHOOSE ONE TYPE TO ENCRYPT/DECRYPT
    
    [1]: Caesar Chyper
    [2]: BGCrypt
    [3]: Bcrypt
    ''')

    return int(input('What you wanna do? '))

# function to show if user wanna encrypt or decrypt
def showEDcrypt():
    print('''
    
    CHOOSE ONE OF THEN
    
    [1]: to encrypt
    [2]: to decrypt
    ''')

    return int(input('What you wanna do? '))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import os
    import sys
    opt1 = showMainMenu()
    opt2 = showMenu()
    opt3 = showEDcrypt()

    if opt1 == 1: # if user want encrypt files
        try:
            import Cryptography_Chyper as crypto
            crypto.encrypt()
        except ImportError: # if module Cryptography does'nt exists
            if 'win' in sys.platform:
                os.system('pip install cryptography')
            else:
                os.system('sudo pip install cryptography')

    elif opt1 == 2:
        try:
            # if user want use Caesar Chyper
            if opt2 == 1:
                import CaesarChyper
                key = int(input('Enter with key [1-26]: '))
                message = input('Enter with message: ')

                # encrypt message
                if opt3 == 1:
                    CaesarChyper.encrypt(key, message)
                # decrypt message
                elif opt3 == 2:
                    CaesarChyper.decrypt(key, message)
            elif opt2 == 2:
                import BGCrypt

                BGCrypt.encrypt()
            elif opt2 == 3:
                import BcryptChyper

                BcryptChyper.encrypt()
        except ModuleNotFoundError:
            print("Module BGCrypt or CaesarChyper does'nt exists")
