filename = 'sometext-1.txt'
def word_frequency(filename):

    with open(filename, 'r') as file:
        text = file.read()


    words = text.split()
    
    frequency_dict = {}

    for word in words:
            if word in frequency_dict:
                    frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1

    return frequency_dict

word_frequencies = word_frequency(filename)

for word, frequency in word_frequencies.items():
      print(f"'{word}': {frequency}")