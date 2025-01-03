# Write the is_valid_guess function here.
def is_valid_guess(guess, required_letters):
 for letter in required_letters:
    if letter not in guess:
      return False
 return True
 
