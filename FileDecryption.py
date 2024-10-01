codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '0', 'D': '^', 'd': '1',
    'E': '&', 'e': '2', 'F': '*', 'f': '3', 'G': '(', 'g': '4', 'H': ')', 'h': '5',
    'I': '-', 'i': '6', 'J': '_', 'j': '7', 'K': '=', 'k': '8', 'L': '+', 'l': '~',
    'M': '[', 'm': '{', 'N': ']', 'n': '}', 'O': ':', 'o': ';', 'P': '"', 'p': "'",
    'Q': '<', 'q': ',', 'R': '>', 'r': '.', 'S': '?', 's': '/', 'T': '|', 't': '\\',
    'U': 'A', 'u': 'B', 'V': 'C', 'v': 'D', 'W': 'E', 'w': 'F', 'X': 'G', 'x': 'H',
    'Y': 'I', 'y': 'J', 'Z': 'K', 'z': 'L', ' ': ' ', '\n': '\n'
} #Copied over from fileencryption

def decrypt_file(input):
    decryption_codes = {}
    for k, v in codes.items():
        decryption_codes[v] = k

    with open(input, 'r') as infile:
        decrypted_content = ''
        for char in infile.read():

            decrypted_content += decryption_codes.get(char, char)
    return decrypted_content 

input_filename = 'encrypted.txt'

print("decrypted content: ")
print(decrypt_file(input_filename) )