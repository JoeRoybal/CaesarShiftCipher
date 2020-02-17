def shift(chars):



def encrypt(file, content):
    with open(file, 'r') as f:
        for line in f.readlines():
            for chars in line:
                shift(chars)
        #shift cypher the test


def encrypt_file():
    response = input("input file path:")
    file = open(response, 'r')
    content = file.read()

    new_path = '/home/joe/Documents/pyProjects/PycharmProjects/caesarCipher/EncryptedText.txt'
    encrypted_file = open(new_path, 'w')

    new_content = encrypt(response, content)
    encrypted_file.write(new_content)

    file.close()
    encrypted_file.close()


def encrypt_text():
    pass


def encrypt_query():
    response = input("Would you like to encrypt an existing file(1) or input text(2)")
    if response == '1':
        encrypt_file()
    elif response == '2':
        encrypt_text()
    else:
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
        decrypt_query()


def origin():
    response = input("Would you like to Encrypt or Decrypt?")
    if response == 'Envrypt' or 'encrypt':
        encrypt_query()
    elif response == 'Decrypt' or 'decrypt':
        decrypt_query()
    else:
        origin()
        return response


origin()
