alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift):
    for letter in original_text:
        if letter not in alphabet:
            print("Invalid Input")
        elif letter in alphabet and shift < len(alphabet):
            pos=alphabet.index(letter)
            if pos==len(alphabet)-1:
                pos=0
                encrypt_char = alphabet[pos+shift]
            elif pos < 20 and shift < 7 or pos < 7 and shift < 20:
                encrypt_char = alphabet[pos+shift]
            elif pos > 19:
                if shift + pos == len(alphabet):
                    encrypt_char = alphabet[pos+shift]
                elif shift + pos < len(alphabet):
                    encrypt_char = alphabet[pos + shift]
                elif shift + pos > len(alphabet):
                    excess = (shift + pos)-len(alphabet)
                    pos=0
                    encrypt_char = alphabet[pos+excess]
        elif shift > len(alphabet):
                excess=shift-len(alphabet)
                pos=shift
                encrypt_char = alphabet[pos+shift]
    return encrypt_char

encrypt_text=encrypt(text, shift)
print(encrypt_text)