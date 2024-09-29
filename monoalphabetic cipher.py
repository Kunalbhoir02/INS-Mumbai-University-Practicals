import random

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(original, key=None):
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)
    
    new = []
    for letter in original:
        if letter in alpha:
            new.append(key[alpha.index(letter)])
        else:
            new.append(letter)  # Keep non-alphabet characters unchanged
    
    return "".join(new), key

def decrypt(cipher, key=None):
    if key is not None:
        new = []
        for letter in cipher:
            if letter in key:
                new.append(alpha[key.index(letter)])
            else:
                new.append(letter)  # Keep non-alphabet characters unchanged
        return "".join(new)
    return None  # Return None if no key is provided

text = input("Enter plain text: ").lower()
encrypted_message, encryption_key = encrypt(text)
print("\nEncrypted message and key:")
print(encrypted_message, encryption_key)
print("\nDecrypted message is:", decrypt(encrypted_message, encryption_key))
