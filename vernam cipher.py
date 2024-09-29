# A Python program to illustrate the Vernam Cipher Technique.

print("# A Python program to illustrate Vernam Cipher Technique.")

def encrypt(message, key):
    message = message.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    encrypt = ""
    
    for i in range(len(message)):
        letter = ord(message[i]) - 65
        key_letter = ord(key[i]) - 65
        encrypted_letter = (letter + key_letter) % 26
        encrypt += chr(encrypted_letter + 65)
    
    return encrypt

def decrypt(message, key):
    message = message.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    decrypt = ""
    
    for i in range(len(message)):
        letter = ord(message[i]) - 65
        key_letter = ord(key[i]) - 65
        decrypted_letter = (letter - key_letter + 26) % 26
        decrypt += chr(decrypted_letter + 65)
    
    return decrypt

def testing(text, key, encrypted_text):
    test = input("Do you want to check what your original text was by decrypting the message?\n(Type 'Yes' or 'No')\t")
    
    if test.lower() == 'yes':
        decrypted_text = decrypt(encrypted_text, key)
        print("\nYour Mode        : Decrypt")
        print("Your Cipher Text : " + encrypted_text)
        print("Key              : " + key)
        print("Decrypted Text   : " + decrypted_text)
    elif test.lower() == 'no':
        print("Thank you!")
    else:
        print("Invalid choice. Please try again.")

# Main program
technique = input("Enter your choice for Vernam Cipher Technique (Encrypt or Decrypt):\t")

if technique.lower() == 'encrypt':
    text = input("Enter the text you want to be converted:\t")
    key = input("Enter the key of your choice:\t")
    encrypted_text = encrypt(text, key)
    print("\nYour Mode      : Encrypt")
    print("Your Text      : " + text)
    print("Key            : " + key)
    print("Encrypted Text : " + encrypted_text)
    testing(text, key, encrypted_text)

elif technique.lower() == 'decrypt':
    text = input("Enter the Vernam cipher text you want to be decrypted:\t")
    key = input("Enter the key provided to you:\t")
    decrypted_text = decrypt(text, key)
    print("\nYour Mode                  : Decrypt")
    print("Your Vernam Cipher Text    : " + text)
    print("Key                        : " + key)
    print("Decrypted Text             : " + decrypted_text)

else:
    print("Wrong choice. Please try again.")
