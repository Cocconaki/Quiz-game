from player import Player
from flow_control import ControlFlow
from subjects import *
import time

def convert_input(userinput):
    if userinput.isdigit():
        return int(userinput)
    else:
        return userinput
 


rounds = 0
player_counter_simulate = 0

test_playeyrs = ControlFlow.create_players()

limit_end_round = len(test_playeyrs)
count_rounds_til_end = 0

while True:

    if count_rounds_til_end == limit_end_round:
        print("Round ends here")
        time.sleep(2)
        ControlFlow.end_round(test_playeyrs)
    
    for player in test_playeyrs:
        print(player)
    
    #Psuts the players in the list in order according to their ID numbers.
    ControlFlow.order_players(test_playeyrs)
    

    print("outer ID current value: ",ControlFlow.outer_id)
    
    print("current player: ", ControlFlow.select_next_player(test_playeyrs))
    
    
    
    input("test for input")
      
    retrieve_answer = ControlFlow.select_subject()
    
    answer_to_question = input("Enter answer: ")
    
    convertred_input = convert_input(answer_to_question)
    
    ControlFlow.recieve_and_checkanswer(convertred_input, retrieve_answer)
    count_rounds_til_end += 1
    
    
    #print(player_counter_simulate)
    #print(type(retrieve_answer), retrieve_answer)
    #print(type(convertred_input), convertred_input)




