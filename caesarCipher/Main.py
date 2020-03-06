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
        text = input("Enter the phrase you would like encrpted")
        key = int(input("Enter numerical value for shift cipher (1-25)"))
        encrypt_text(text, key)
    else:
        print("Please enter either a 1 or 2")
        encrypt_query()


def decrypt_file():
    pass


def decrypt_text():
    pass


def decrypt_query():
    response = input("Would you like to encrypt an existing file(1) or input text(2)")
    if response == '1':
        decrypt_file()
    elif response == '2':
        decrypt_text()
    else:
        print("Please enter either a 1 or 2")
        decrypt_query()


def origin():
    response = input("Would you like to Encrypt or Decrypt?")
    if response == 'Envrypt' or 'encrypt':
        encrypt_query()
    elif response == 'Decrypt' or 'decrypt':
        decrypt_query()
    else:
        print("Please enter valid response")
        origin()
        return response


origin()
