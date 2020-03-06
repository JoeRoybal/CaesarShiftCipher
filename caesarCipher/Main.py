def shift(chars):
    pass


def encrypt():
    pass


def encrypt_text(text, key):
    result = ""
    if 0 < key < 26:
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
    else:
        key = int(input("Please enter in correct format"))
        encrypt_text(text, key)

    return print(result)


def encrypt_file():
    response = input("input file path:")
    file = open(response, 'r')
    content = file.read()

    new_path = '/home/joe/Documents/Python/Projects/CaesarShiftCipher/caesarCipher/EncryptedText.txt'
    encrypted_file = open(new_path, 'w')

    new_content = encrypt(response, content)
    encrypted_file.write(new_content)

    file.close()
    encrypted_file.close()


def encrypt_query():
    response = input("Would you like to encrypt an existing file(1) or input text(2)")
    if response == '1':
        encrypt_file()
    elif response == '2':
        text = input("Enter the phrase you would like encrypted")
        key = int(input("Enter numerical value for shift cipher (1-25)"))
        encrypt_text(text, key)
    else:
        print("Please enter either a 1 or 2")
        encrypt_query()


def decrypt_file():
    pass


def decrypt_text(text, key):
    result = ""
    if 0 < key < 26:
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # decrypt uppercase characters in plain text

            if char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            # decrypt lowercase characters in plain text
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
    else:
        key = int(input("Please enter in correct format"))
        encrypt_text(text, key)

    return print(result)



def brute_force_decrypt(text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)):
        translated = ''
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                translated += chr((ord(char) - key - 65) % 26 + 65)
            else:
                translated += chr((ord(char) - key - 97) % 26 + 97)
        print("Key #%s: %s" % (key, translated))


def decrypt_query():
    response = input("Would you like to decrypt an existing file(1), input text(2), or brute force input text(3)")
    if response == '1':
        decrypt_file()
    elif response == '2':
        text = input("Enter the phrase you would like decrypted")
        key = int(input("Enter numerical value for shift cipher (1-25)"))
        encrypt_text(text, key)
        decrypt_text()
    elif response == '3':
        text = input("Enter the phrase you would like decrypted")
        brute_force_decrypt(text)
    else:
        print("Please enter either a 1 or 2")
        decrypt_query()


def origin():
    response = input("Would you like to Encrypt(1) or Decrypt(2)?")
    if response == '1':
        encrypt_query()
    elif response == '2':
        decrypt_query()
    else:
        print("Please enter valid response")
        origin()
        return response


origin()
