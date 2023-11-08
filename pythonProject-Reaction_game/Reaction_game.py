import time
from time import time as my_time
from random import randint

BLUE = "\033[0;34m"
RED = "\033[0;31m"
RESET = '\033[0m'

MAX = 5
player1 = 0
player2 = 0

while player1 < MAX or player2 < MAX:
    print(BLUE, "Player1's turn", RESET)
    input("Press Enter to START! ")
    wait_time1 = randint(2, 5)
    time.sleep(wait_time1)
    start_time1 = my_time()
    input("Press Enter to STOP!")
    end_time1 = my_time()
    print("Player1 started at {}".format(time.strftime('%X', time.localtime(start_time1))))
    print("Player1 ended at {}".format(time.strftime('%X', time.localtime())))
    reaction_time1 = end_time1 - start_time1
    print(RED, "Player1's reaction time is {}".format(reaction_time1), RESET)

    print(BLUE, "Player2's turn", RESET)
    input("Press Enter to START! ")
    wait_time2 = randint(2, 5)
    time.sleep(wait_time2)
    start_time2 = my_time()
    input("Press Enter to STOP!")
    end_time2 = my_time()
    print("Player2 started at {}".format(time.strftime('%X', time.localtime(start_time2))))
    print("Player2 ended at {}".format(time.strftime('%X', time.localtime(end_time2))))
    reaction_time2 = end_time2 - start_time2
    print(RED, "Player2's reaction time is {}".format(reaction_time2), RESET)

    if reaction_time1 == reaction_time2:
        print(BLUE, "Tie", RESET)
        print("Player1's score is {}".format(player1))
        print("Player2's score is {}".format(player2))

    elif ((reaction_time1 < reaction_time2) and (reaction_time1 != 0)) or reaction_time2 == 0:
        print(BLUE, "Player1 won", RESET)
        player1 += 1
        print("Player1's score is {}".format(player1))
        print("Player2's score is {}".format(player2))
        if player1 == MAX:
            print(BLUE, "Player1 won the whole game!", RESET)
            break

    elif ((reaction_time2 < reaction_time1) and (reaction_time2 != 0)) or reaction_time1 == 0:
        print(BLUE, "Player2 won", RESET)
        player2 += 1
        print("Player1's score is {}".format(player1))
        print("Player2's score is {}".format(player2))
        if player2 == MAX:
            print(BLUE, "Player2 won the whole game!", RESET)
            break
