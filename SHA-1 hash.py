import hashlib

user_input = input('Enter the value to encode: ').strip()  # Stripping whitespace
hash_object = hashlib.sha1(user_input.encode())
print('The hexadecimal equivalent of SHA-1 is:')
print(hash_object.hexdigest())
