from random import randint

number = randint(1, 100)
guess = int(input("Guess the number: "))
times_tried = 1

# write a while-loop that repeats itself as long as the number is not guessed
# within this while, create an if-statement that displays if the number is higher or lower
# also, add one to the times_tried
while guess != number:
  if number > guess:
    print("The number is higher, try again")
  else:
    print("The number is lower, try again")
  
  times_tried = times_tried + 1
  guess = int(input("Guess the number: "))

# print a message that the user guessed it including the times tried to guess it
print("You guessed it! It took you",times_tried,"times!")
