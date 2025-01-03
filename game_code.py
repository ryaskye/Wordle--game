from get_guess_fn import get_guess                 #
from is_game_over_fn import is_game_over           #
from modules import print_in_color                 #
from print_guess_fn import print_guess             #
####################################################
secret_word= input("Enter the secret word:\n")
tries_left=5
required_letters=[]
game_over= False
while game_over is False:
  user_guess= get_guess(required_letters)
  game_over=is_game_over(secret_word,user_guess,tries_left)
  if game_over:
    break
  required_letters= print_guess(secret_word, user_guess)
  print()
  tries_left= tries_left -1
