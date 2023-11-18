# planning the game 
# - start the game
# - make an empty array to save the trying attempts in it
# - ask the user to pick a number between 1 and 10
# - ask the pc to pick a number between 1 and 10
# - if they choose the same number
# - say smth nice to the user
# - prints the num of the attempts 
# - if the pick lower or higher the choosen num , through a error
# - if the guess doesn't equal the pick of the pc
# - repeat the same question again, give the user a hint
# - if the game is done , ask the user if he wants to play again or not

import random 

attempts_list = []

def show_score():
    if not attempts_list:
        print("there's no a high score , start playing")
    else:
        print(f"the current high score is {min(attempts_list)}")

attempts = 0 
rand_num = random.randint(1, 10)

user_name = input("what's your name : ")
wanna_play = input(f"welcome {user_name}, would you like to play the guessing game ? "
    "Enter (Yes / No) "
).lower()

if wanna_play == 'no':
    print("that's cool")
    exit()
else :
    show_score()

while wanna_play == 'yes':
    try :
        guess = int(input("pick a number between 1 and 10: "))
        if guess < 1 or guess > 10 :
            raise ValueError("please give a num between the given range!")
        
        attempts += 1 

        if guess == rand_num :
            print("nice , you got it")
            print(f"it took you {attempts} attempts to get it")
            wanna_play = input("do you want to play again (yes , no) ").lower()
            attempts_list.append(attempts)

            if (wanna_play == 'no'):
                print("that's cool , have a nice day")
            else:
                attempts = 0 
                rand_num = random.randint(1, 10)
                show_score()
                continue
        elif guess > rand_num :
            print("it's lower !")

        else:
            print("it's higher! ")
    except ValueError as er:
        print(er)