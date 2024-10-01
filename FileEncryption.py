codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '0', 'D': '^', 'd': '1',
    'E': '&', 'e': '2', 'F': '*', 'f': '3', 'G': '(', 'g': '4', 'H': ')', 'h': '5',
    'I': '-', 'i': '6', 'J': '_', 'j': '7', 'K': '=', 'k': '8', 'L': '+', 'l': '~',
    'M': '[', 'm': '{', 'N': ']', 'n': '}', 'O': ':', 'o': ';', 'P': '"', 'p': "'",
    'Q': '<', 'q': ',', 'R': '>', 'r': '.', 'S': '?', 's': '/', 'T': '|', 't': '\\',
    'U': 'A', 'u': 'B', 'V': 'C', 'v': 'D', 'W': 'E', 'w': 'F', 'X': 'G', 'x': 'H',
    'Y': 'I', 'y': 'J', 'Z': 'K', 'z': 'L', ' ': ' ', '\n': '\n'  #LLM created dictionary
}
    


def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file,'w') as outfile:

        for character in infile.read():
            encripted_char = codes.get(character, character)
            outfile.write(encripted_char)


input_filename = 'info_security-1.txt'
output_filename = 'encrypted.txt'

encrypt_file(input_filename, output_filename)

print(f" File '{input_filename}' has been encrypted to '{output_filename}'. ")


        