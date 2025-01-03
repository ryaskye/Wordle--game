# Write the print_guess function here.
from modules import print_in_color
### DO NOT MODIFY ABOVE


def print_guess(secret_word, guess):
  required_letters= []
  for i in range(len(guess)):
    should_print_first_letter_green = guess[i] == secret_word[i] # COPY YOUR CODE FROM THE GREEN EXERCISE
    should_print_first_letter_red = guess[i] != secret_word[i] and guess[i] not in secret_word
    should_print_first_letter_yellow = guess[i] != secret_word[i] and guess[i] in secret_word  
    if guess[i] == secret_word[i]:
      print_in_color(guess[i], 'green')
      required_letters.append(guess[i])
    elif guess[i] != secret_word[i] and guess[i] in secret_word:  
      print_in_color(guess[i], 'yellow')
      required_letters.append(guess[i])
    elif guess[i] != secret_word [i] and guess [i] not in secret_word:
      print_in_color(guess[i],'red') 
  return required_letters
 
