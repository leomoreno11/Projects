# A Caesar Cypher encription works by shifting the whole alphabet by a given number, making the content of a letter or
# message appears nonsense for the unknow eye

import string

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)

    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

print('╔═╗╔═╗╔═╗╔═╗╔═╗╦═╗  ╔═╗╦ ╦╔═╗╦ ╦╔═╗╦═╗')
print('║  ╠═╣║╣ ╚═╗╠═╣╠╦╝  ║  ╚╦╝╠═╝╠═╣║╣ ╠╦╝')
print('╚═╝╩ ╩╚═╝╚═╝╩ ╩╩╚═  ╚═╝ ╩ ╩  ╩ ╩╚═╝╩╚═\n')


print('You want to encrypt or decrypt a message ?\n', '1 - Encrypt.\n 2 - Decrypt.')
option = int(input(''))

if option == 1:
    plain_text = input('What message you wanna encrypt ?\n')
    key = int(input('Input the key:\n'))
    key %= 26
    print(caesar(plain_text, key, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
elif option == 2:
    plain_text = input('What message you wanna decrypt ?\n')
    key = int(input('Input the key:\n'))
    key %= 26
    key_shifted = 26 - key
    # key %= 26

    print(caesar(plain_text, key_shifted, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
