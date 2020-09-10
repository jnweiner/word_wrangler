import random

points = {
  "player": 0,
  "total possible": 0
}

words_and_answers = [
  {"word": "house", "answers": ["hoe", "sue", "hue", "she", "use", "shoe", "hoes", "hues", "hose", "house"]},
  {"word": "noodle", "answers": ["nod", "end", "loo", "one", "ode", "led", "eon", "den", "don", "old", "doe", "ole", "dole", "lend", "lone", "noel", "done", "lode", "node", "loon", "olden", "noodle"]},
  {"word": "forest", "answers": ["forest", "fortes", "foster", "softer", "fores", "forte", "forts", "frets", "frost", "store", "foes", "fore", "fort", "fret", "ores", "rest", "rose", "rote", "rots", "soft", "sore", "sort", "toes", "tore", "foe", "for", "fro", "ore", "rot", "set", "toe"]}
]

# Generates a randomly scrambled version of the input word
def scramble_word(word):
  chars = list(word)
  random.shuffle(chars)
  scrambled = ''
  scrambled = scrambled.join(chars)
  return scrambled

# Will display the appropriate number of available words to find, plus any correctly guessed hidden words so far
# Called each time for words of varying lengths (so called once for hidden words of length 3, then again for hidden words of length 4, etc.)
def display_words(word_length, answers):
  # First, figure out which correct guesses are the appropriate length to display
  guesses_to_display = []
  for guess in correct_guesses:
    if len(guess) == word_length:
      guesses_to_display.append(guess)

  # Next, figure out how many answers are the appropriate length
  answer_amount = 0
  for answer in answers:
    if len(answer) == word_length:
      answer_amount += 1

  # Print numbers in ascending order, indicating how many answers there are of that length, and correct guesses if applicable
  n = 0
  while n < answer_amount:
    if n < len(guesses_to_display):
      print(f"  {n + 1})", guesses_to_display[n])
    else:
      print(f"  {n+1})")
    n+=1

# Displays player options
def display_menu():
  print("\n--------------------\n")
  print("Guess a word or input one of the following:")
  print("  [S]CRAMBLE the master word again")
  print("  [R]EVEAL a hidden word")
  print("  [Q]UIT")
  print("\n--------------------\n")

# Displays current master word and player points, and calls the display_words function as many times as necessary, beginning with hidden words of length 3
def display_progress(master_word, answers):
  print("\n--------------------\n")
  print(f"Your scrambled master word is: '{master_word}'")
  print(f"\nYour points: {points['player']}")

  length = 3
  while length <= len(master_word):
    print(f"\nHIDDEN {length}-LETTER WORDS:")
    display_words(length, answers)
    length += 1

# Appends a random word from the answers list to the correct_guesses list
# Does this by generating a randint to use as a index from answers list
# By adding to correct_guesses, this means it will now be displayed in display_words
def reveal_random_word(answers):
  while True:
    index = random.randint(0, len(answers) - 1)
    random_word = answers[index]
    if not random_word in correct_guesses:
      correct_guesses.append(random_word)
      break
  return random_word

# Adds up possible points based on lengths of each word in answers for the particular level
def calculate_possible_points(answers):
    possible_points = 0
    for answer in answers:
        possible_points += len(answer)
    return possible_points

# Runs each level, asking player for input and responding accordingly
# Originally had a separate function for player input, but ran into trouble with scope and variables, particularly for player points, and figuring out how to break the loop if the player quits or beats the level.
# Each time play_level is called, it also updates the player's point total, so their points will be tracked level to level.
def play_level(master_word, answers):

  while True:
    display_progress(master_word, answers)
    display_menu()
    player_input = input(">> ").lower()

    if player_input == "q":
      print("\nThanks for playing!")
      break
    elif player_input == "s":
      pass
    elif player_input == "r":
      print("\nRevealing a random hidden word...")
      random_word = reveal_random_word(answers)
      points['player'] -= len(random_word)
    elif player_input in correct_guesses:
      print("\nAlready got that one...")
    elif player_input in answers:
      correct_guesses.append(player_input)
      points['player'] += len(player_input)
      print("\nCorrect!")
    else:
      print("\n Try again!\n")

    if len(correct_guesses) == len(answers):
      display_progress(master_word, answers)
      print("\n~~~~~~~~~~~~~~~~~~~~~~~\n")
      print("LEVEL COMPLETE!")
      print(f"\nYour score: {points['player']} out of {points['total possible']} possible points")
      print("\n~~~~~~~~~~~~~~~~~~~~~~~")
      break

  return player_input

def setup_level(n):
  master_word = scramble_word(words_and_answers[n]["word"])
  answers = words_and_answers[n]["answers"]

  points['total possible'] += calculate_possible_points(answers)

  print(f"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LEVEL {n + 1} <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
  player_input = play_level(master_word, answers)
  return player_input

############# GAME INTRO ############

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

############# RUN LEVELS ############

n = 0
while n < 3:
  correct_guesses = []
  player_input = setup_level(n)
  if player_input == 'q':
    break
  n += 1
