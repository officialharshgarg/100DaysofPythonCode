alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(alphabet))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift, direction):
    result = ""

    # Normalize shift (handles shift > 26)
    shift = shift % 26

    # Reverse shift for decoding
    if direction == "decode":
        shift *= -1

    for letter in original_text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = (pos + shift) % 26
            result += alphabet[new_pos]
        else:
            # Keep spaces, numbers, symbols unchanged
            result += letter

    return result

output = caesar(text, shift, direction)
print("Result:", output)