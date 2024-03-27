# high_and_low.py
from random import randint


def get_answer():
    while True:
        ans = input("High(H) or Low(L) >")
        if ans.upper() == "H" or ans.upper() ==  "L":
            break
    return ans.upper()


def main():
    player_count = 0
    computer_count = 0
    while player_count < 5 and computer_count < 5:
        player_number = randint(1,13)
        print ("Your number:{}".format(player_number))
        computer_number = randint(1,13)
        print ("Computer number:?")
        answer = get_answer()
        balance = computer_number - player_number
        if balance == 0:
            print("even")
        elif balance > 0 and answer == "H":
            print("Hit!")
            player_count += 1
        elif balance < 0 and answer == "L":
            print("Hit!")
            player_count += 1
        else:
            print("Miss!")
            computer_count += 1
        print("Computer number:{}".format(computer_number))
        print("Next>>")
        
            
    if player_count == 5:
        print("You Win!")
    else:
        print("You Lose!")
        
        
if __name__ == '__main__':
    main()
