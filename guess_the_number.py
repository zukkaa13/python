
from random import randrange
import math

def main():
  game_mode = int(input("choose game mode \nUser to guees the number, press 1 \nComputer to guess the number, press 2:\n choose game "))
  lower_bound = int(input("plase enter lower bound: "))
  upper_bound = int(input("plase enter higher bound: "))
 # if game_mode =
  if game_mode == 1:
      guess_the_number_user(lower_bound, upper_bound)
  elif game_mode == 2:
      guess_the_number_comouter(lower_bound, upper_bound)

  return 0

def guess_the_number_user(lower_bound, upper_bound):
    number_to_guess = randrange(lower_bound, upper_bound)
    user_guess = math.inf
    guess_counter = 0 

    while number_to_guess != user_guess:
        guess_counter = guess_counter + 1
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}:  "))
        if user_guess < number_to_guess:
            print("to small, try again: ")
        elif user_guess > number_to_guess:
            print("to big, try again")

    print(f"congratulation you guessed the number {number_to_guess} in {guess_counter} tries ")
    game_over = input("to return to main menu press the (m) button to quit game press (enter)")
    if game_over == 'm':
      print("___________________________________________________________________________\n")
      main()

    return 0

def guess_the_number_comouter(lower_bound, upper_bound):
    feedback = ' '
    computer_guess = math.inf
    while feedback != 'c':
        computer_guess = randrange(lower_bound, upper_bound)
        feedback = input(f"is {computer_guess} correct (c), too low (l) or too high (h): ")
        if feedback == 'l':
            lower_bound = computer_guess + 1
        elif feedback == 'h':
            upper_bound = computer_guess - 1
        if lower_bound == upper_bound:
            print(f"only number left is {lower_bound}\n")
            computer_guess = lower_bound
            break
        
    print(f"computer gussed the number {computer_guess} in {guess_the_number_comouter} tries")

    game_over = input("to return to main menu press the (m) button to quit game press (enter)")
    if game_over == 'm':
      print("___________________________________________________________________________\n")
      main()

    return 0

main()