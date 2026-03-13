import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct_letters = []
placeholder = ""
for letter in chosen_word:
 def check_letter(placeholder,word_length):
  while not game_over:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
       if letter == guess:
           placeholder += letter
           word_length -= 1
       elif letter == guess:
               correct_letters+=guess
               print(correct_letters)
       else:
           placeholder += "_"
           print(correct_letters.append(placeholder))
placeholder = ""
check_letter(placeholder, word_length)
print(correct_letters)


