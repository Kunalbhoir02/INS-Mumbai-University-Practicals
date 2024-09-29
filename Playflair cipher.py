def to_lower_case(text):
    """Converts the text to lowercase."""
    return text.lower()

def clean_text(text):
    """Removes non-alphabetic characters and converts to lowercase."""
    return ''.join(filter(str.isalpha, text)).lower()

def add_filler_letter(text):
    """Adds 'x' between identical consecutive letters in the text."""
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            new_text += 'x'
        i += 1
    return new_text

def create_diagraph(text):
    """Groups the text into pairs of two characters (diagraphs)."""
    if len(text) % 2 != 0:
        text += 'x'  # Append 'x' if odd-length
    return [text[i:i+2] for i in range(0, len(text), 2)]

def generate_key_table(key, alpha):
    """Generates a 5x5 key square matrix from the key."""
    key_letters = []
    for char in key:
        if char not in key_letters and char in alpha:
            key_letters.append(char)
    
    # Handle 'j' as 'i'
    key_letters = [char if char != 'j' else 'i' for char in key_letters]
    
    key_letters += [char for char in alpha if char not in key_letters]
    matrix = [key_letters[i:i + 5] for i in range(0, 25, 5)]
    
    return matrix

def search(matrix, element):
    """Finds the row and column of an element in the matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == element:
                return row, col

def encrypt_row_rule(matrix, r1, c1, r2, c2):
    """Encrypts characters in the same row."""
    return matrix[r1][(c1 + 1) % 5], matrix[r2][(c2 + 1) % 5]

def encrypt_column_rule(matrix, r1, c1, r2, c2):
    """Encrypts characters in the same column."""
    return matrix[(r1 + 1) % 5][c1], matrix[(r2 + 1) % 5][c2]

def encrypt_rectangle_rule(matrix, r1, c1, r2, c2):
    """Encrypts characters in different rows and columns."""
    return matrix[r1][c2], matrix[r2][c1]

def encrypt_by_playfair_cipher(matrix, diagraphs):
    """Encrypts the text using the Playfair cipher."""
    cipher_text = []
    for digraph in diagraphs:
        r1, c1 = search(matrix, digraph[0])
        r2, c2 = search(matrix, digraph[1])
        
        if r1 == r2:
            cipher1, cipher2 = encrypt_row_rule(matrix, r1, c1, r2, c2)
        elif c1 == c2:
            cipher1, cipher2 = encrypt_column_rule(matrix, r1, c1, r2, c2)
        else:
            cipher1, cipher2 = encrypt_rectangle_rule(matrix, r1, c1, r2, c2)
        
        cipher_text.append(cipher1 + cipher2)
    return "".join(cipher_text)

# Main function to execute the Playfair cipher
def main():
    alpha = "abcdefghiklmnopqrstuvwxyz"  # Note 'j' is excluded
    plain_text = input("Enter plain text: ")
    key = input("Enter key: ")

    # Clean and prepare the text
    plain_text = clean_text(plain_text)
    plain_text = add_filler_letter(plain_text)
    diagraphs = create_diagraph(plain_text)

    key = to_lower_case(key)
    key_matrix = generate_key_table(key, alpha)

    cipher_text = encrypt_by_playfair_cipher(key_matrix, diagraphs)

    print("Key text:", key)
    print("Plain Text:", plain_text)
    print("CipherText:", cipher_text)

if __name__ == "__main__":
    main()
