from player import Player
from flow_control import ControlFlow
from subjects import *
import time
import os



test_playeyrs = ControlFlow.create_players()

limit_end_round = len(test_playeyrs)

while True:
    
    if ControlFlow.count_rounds_til_end == limit_end_round:
        ControlFlow.count_rounds_til_end = 0
        ControlFlow.outer_id = None
        ControlFlow.round_counter += 1
        
        if ControlFlow.round_counter == 3:
            print("Game is DONE!")
            time.sleep(1)
            os.system("cls")
            ControlFlow.finish_game(test_playeyrs)
            break
        
        print("Round ends here")
        time.sleep(2)
        ControlFlow.end_round(test_playeyrs, ControlFlow.end_round)
    

    """Game starts here: """

    if ControlFlow.flag_for_players_list:
        for player in test_playeyrs:
            print(player)
    ControlFlow.flag_for_players_list = False

    
    #Psuts the players in the list in order according to their ID numbers.
    ControlFlow.order_players(test_playeyrs)
    

    print("outer ID current value: ",ControlFlow.outer_id)
    current_player = ControlFlow.select_next_player(test_playeyrs)
    print("current player: ", current_player)
    time.sleep(1)
    current_subject = ControlFlow.select_subject()
    while True:
        retrieve_answer = ControlFlow.select_question(current_subject)
        try:
            answer_to_question = input("Enter answer: ")
        except EOFError:
            print("Try again")
            time.sleep(1)
            continue
        convertred_input = ControlFlow.convert_input(answer_to_question)
        if ControlFlow.recieve_and_checkanswer(convertred_input, retrieve_answer, current_player):
            ControlFlow.points_in_round += 1000
            goforward = str(input("Go for an other question? Y/N"))
            if goforward.lower() == "y":
                continue
            else:
                current_player.points += ControlFlow.points_in_round
                ControlFlow.points_in_round = 0
                print("Breaking")
                time.sleep(1)
                break
        else:
            ControlFlow.points_in_round = ControlFlow.points_in_round / 2
            current_player.points += ControlFlow.points_in_round
            ControlFlow.points_in_round = 0
            print("Breaking loop")
            time.sleep(1)
            break

    ControlFlow.count_rounds_til_end += 1
    
    
   

