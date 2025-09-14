from player import Player
from flow_control import ControlFlow
from subjects import *

'''player1 = Player("Muci", 0)
player2 = Player("Nyuszi", 0)
players = [player1,player2]'''


def convert_input(userinput):
    if userinput.isdigit():
        return int(userinput)
    else:
        return userinput

rounds = 0

test_playeyrs = ControlFlow.create_players()


player_counter_simulate = 0


while True:

    for player in test_playeyrs:
        print(player)
    
    ControlFlow.order_players(test_playeyrs)
    input("test for input")
    retrieve_answer = ControlFlow.select_subject()
    answer_to_question = input("Enter answer: ")
    convertred_input = convert_input(answer_to_question)
    ControlFlow.recieve_and_checkanswer(convertred_input, retrieve_answer)
    print(player_counter_simulate)
    print(type(retrieve_answer), retrieve_answer)
    print(type(convertred_input), convertred_input)




