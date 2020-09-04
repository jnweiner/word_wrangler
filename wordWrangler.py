import random

def scramble_word(word):
  chars = list(word)
  random.shuffle(chars)
  scrambled = ''
  scrambled = scrambled.join(chars)
  return scrambled

def display_words(word_length, answers):
  # figure out which guesses are the length we're looking for
  guesses_to_display = []
  for guess in correct_guesses:
    if len(guess) == word_length:
      guesses_to_display.append(guess)

  # figure out how many answers are of that length
  answer_amount = 0
  for answer in answers:
    if len(answer) == word_length:
      answer_amount += 1

  # print nums in ascending order, indicating how many answers there are of that length, and correct guesses if applicable
  n = 0
  while n < answer_amount:
    if n < len(guesses_to_display):
      print(f"  {n + 1})", guesses_to_display[n])
    else:
      print(f"  {n+1})")
    n+=1

def display_progress(master_word, answers, current_points):
  print("\n--------------------")

  print(f"\nYour scrambled master word is: '{master_word}'")
  print(f"\nYour points: {current_points}")

  print("\nGuess a word or input one of the following:")
  print("  [S]CRAMBLE the master word again")
  print("  [R]EVEAL a hidden word")
  print("  [Q]UIT")

  # made this more flexible to accommodate master words of any length with any number of interior word breakdowns (starting at length 3)

  length = 3
  while length <= len(master_word):
    print(f"\nHIDDEN {length}-LETTER WORDS:")
    display_words(length, answers)
    length += 1

  print("\n--------------------\n")

# reveal word process
    # goal - append a random word from answers to the correct_guesses list
    # generate randint for to get random index from answers list
def reveal_random_word(answers):
  while True:
    index = random.randint(0, len(answers) - 1)
    random_word = answers[index]
    if not random_word in correct_guesses:
      correct_guesses.append(random_word)
      break
  return random_word

def calculate_possible_points(answers):
    possible_points = 0
    for answer in answers:
        possible_points += len(answer)
    return possible_points

def play_level(master_word, answers, player_points):
  current_points = player_points

  while True:
    display_progress(master_word, answers, current_points)
    player_input = input(">> ").lower()

    if player_input == "q":
      print("\nThanks for playing!")
      break
    elif player_input == "s":
      pass
    elif player_input == "r":
      print("\nRevealing a random hidden word...")
      random_word = reveal_random_word(answers)
      current_points -= len(random_word)
    elif player_input in correct_guesses:
      print("\nAlready got that one...")
    elif player_input in answers:
      correct_guesses.append(player_input)
      current_points += len(player_input)
      print("\nCorrect!")
    else:
      print("\n Try again!\n")

    if len(correct_guesses) == len(answers):
      print("LEVEL COMPLETE!")
      print(f"\nYour score: {current_points} out of {total_possible_points} possible points")
      break

  return current_points


## GAME INTRO MOCKUP ##

print("\nWelcome to WORD WRANGLER!")
print("\nIn each round, you'll receive a scrambled MASTER WORD.")
print("Try to find as many hidden words inside this word as you can!")
print("\nEach hidden word is worth one point per letter.")
print("\nIf you're stuck and you choose to reveal a hidden word, you'll lose its point value!\n")

player_points = 0
total_possible_points = 0

while True:
  ready = input("Enter 'P' when you're ready to play! ")

  if ready.upper() == "P":
    break


### LEVEL ONE TEST - "house" ###

level1_master_word = scramble_word("house")
level1_answers = ["hoe", "sue", "hue", "she", "use", "shoe", "hoes", "hues", "hose", "house"]

total_possible_points += calculate_possible_points(level1_answers)

correct_guesses = []

player_points = play_level(level1_master_word, level1_answers, player_points)

