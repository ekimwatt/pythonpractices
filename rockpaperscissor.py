import random
def play_game():

    choices = ['rock', 'paper', 'scissors']
    player_choice = input('rock paper scissors\n')
    player_choice = player_choice.lower()

    computer_choice = random.choice(choices)
    print(computer_choice)

    if player_choice == 'rock':
        if computer_choice == 'paper':
            print("HAHA HAHA! You lose!")
        elif computer_choice == 'scissors':
            print("You got lucky. You win this round!")
        else:
            print("It's a tie.. Let's go again!")

    if player_choice == 'paper':
        if computer_choice == 'paper':
            print("It's a tie.. Let's go again!")
        elif computer_choice == 'scissors':
            print("HAHA HAHA! You lose!")
        else:
            print("You got lucky. You win this round!")

    if player_choice == 'scissors':
        if computer_choice == 'paper':
            print("You got lucky. You win this round!")
        elif computer_choice == 'scissor':
            print("It's a tie.. Let's go again!")
        else:
            print("HAHA HAHA! You lose!")

def main():
    play_game()
    ask = input('Want to play another round? yes or no?')
    if ask.lower() == 'yes':
        main()
    else:
        print("That's lame. Good bye!")
main()