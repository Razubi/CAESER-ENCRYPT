import string



def caeser(text, shift,alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]


    shifted_alphabets = tuple(map(shift_alphabet,alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet =''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


plain_text = "Hello, My Name Is Jynx"
word_2 = "And I Play Games"
EN_1 =(caeser(plain_text,-3,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))
EN_2 =(caeser(word_2,-3,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))
print(caeser(EN_1 +" "+ EN_2,-69,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))