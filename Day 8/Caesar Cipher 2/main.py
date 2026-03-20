alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    if direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    if direction == 'decode':
        decrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount):
    decrypt_text=""
    for letter in original_text:
        shift_letter = alphabet.index(letter)-shift_amount
        shift_letter %= 26
        decrypt_text += alphabet[shift_letter]
    print(f"Here is the decrypted message: {decrypt_text}")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


caesar(text, shift, direction)


