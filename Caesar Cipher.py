# A Python program to illustrate Caesar Cipher Technique

def encrypt(text, s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

# Check the above function
technique = input("Enter your choice for Caesar Cipher Technique (Encrypt or Decrypt): ").strip()

if technique == 'Encrypt':
    text = input("Enter the text you want to be encrypted: ").strip()
    shift = int(input("Enter your choice for secret key: "))
    encrypted_text = encrypt(text, shift)
    print(f"\nYour Text      : {text}")
    print(f"Shift          : {shift}")
    print(f"Encrypted Text : {encrypted_text}")

elif technique == 'Decrypt':
    text = input("Enter the cipher text you want to be decrypted: ").strip()
    shift = int(input("Enter the number of shifts provided to you: "))
    decrypted_text = encrypt(text, 26 - shift)
    print(f"\nYour Cipher Text    : {text}")
    print(f"Shift               : {shift}")
    print(f"Decrypted Text      : {decrypted_text}")

else:
    print("Wrong choice. Please try again.")
