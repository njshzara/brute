import itertools

# Set the password and the list of possible characters
password = input('Enter pass:    ')
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Use itertools to generate all possible combinations of characters
for length in range(1, len(characters)+1):
  for guess in itertools.product(characters, repeat=length):
    guess = "".join(guess)
    if guess == password:
      print("Found password: " + guess)
      exit()
  print("Tried all combinations of length " + str(length))

print("Could not find password")
