from random import randint
def win():
    print ('You win!')

def lose():
    print ('You lose!')

value=True
while value:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    if player_choice == computer_choice:
        print ('Draw!')
        value=False
    elif player_choice=='rock' and computer_choice == 'scissors':
        win()
        value=False
    elif player_choice=='paper' and computer_choice == 'scissors':
        lose()
        value=False
    elif player_choice== 'scissors' and computer_choice == 'paper':
        win()
        value=False
    elif player_choice== 'scissors' and computer_choice == 'rock':
        lose()
        value=False
    elif player_choice== 'paper' and computer_choice == 'rock':
        win()
        value=False
    elif player_choice=='rock' and computer_choice == 'paper':
        lose()
        value=False
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'y':
        value=True
    else:
        value=False
        