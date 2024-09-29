def split_len(seq, length):
    """Split the sequence into chunks of specified length."""
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    """Encode the plaintext using the columnar transposition cipher with the given key."""
    # Create a mapping from key values to column positions
    order = {int(val): num for num, val in enumerate(key)}
    ciphertext = ''

    # Process the plaintext in chunks of the length of the key
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                # Append character from the column specified by the key order
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext

# Get user input for plaintext and column key
text = input("Enter text: ")
columnkey = input("Enter reading column sequence: ")

# Output the encrypted text
print("Encrypted text:", encode(columnkey, text))
