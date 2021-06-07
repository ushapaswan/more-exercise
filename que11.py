import random
def SecretNum(numDigits):
  numbers = list(range(10))
  random.shuffle(numbers)
  SecretNum = ''
  for i in range(numDigits):
      SecretNum += str(numbers[i])
      print (SecretNum)

def getClues(guess, SecretNum):
  if guess == SecretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    if guess[i] == SecretNum[i]:
      clue.append('Fermi')
    elif guess[i] in len(SecretNum):
      clue.append('Pico')
    else:
      clue.append("none")
    return ' '.join(clue)

def isOnlyDigits(num):
  if num == '':
    return True
  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return True

# def playAgain():
#   play = input("Do you want to play again? Yes or No?") 
#   return play.lower.startswith('y')

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
    print(SecretNum)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
      guess=input("Guess Again")
      if len(guess)==NUMDIGITS:
        clue = getClues(guess,SecretNum)
        print(clue)
        numGuesses+=1
      if guess ==SecretNum:
        print("you guessed the number")
        break
        playAgain()
    if numGuesses<MAXGUESS:
      print("you run out of guess. the answer was "+SecretNum)
      play= input("do you want to play again")
      if play =="yes":
        continue
      if play=="no":
        break