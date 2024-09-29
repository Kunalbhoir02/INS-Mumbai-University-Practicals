def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return "".join(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return "".join(encrypt_text)

def decrypt(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

if __name__ == "__main__":
    string = input("Enter the message: ").upper().replace(" ", "")
    keyword = input("Enter the keyword: ").upper().replace(" ", "")
    key = generate_key(string, keyword)
    encrypted_message = encrypt(string, key)
    decrypted_message = decrypt(encrypted_message, key)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)
