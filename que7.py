import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  SecretNum = ''
  for i in range(numDigits):
    SecretNum += (numbers[i])
  print (SecretNum)

def getClues(guess, SecretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == SecretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    if guess[i] == SecretNum[i]:
      clue.append('Fermi')
    elif guess[i] in SecretNum:
      clue.append('Pico')
    if len(clue) == 0:
      return 'None'
  return ' '.join(clue)

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False

  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return True

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = input("Do you want to play again? Yes or No?") 
  return play.lower.startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
  SecretNum = SecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  while numGuesses <= MAXGUESS:
    while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
      print ('Guess' + (numGuesses))
      guess = input("Guess Again")

    clue = getClues(guess, SecretNum)
    print(clue)
    numGuesses += 1
    if guess == SecretNum:
      break
    if numGuesses < MAXGUESS:
      print ('You ran out of guesses. The answer was ' + secretNum)
  if not playAgain:
    break
 