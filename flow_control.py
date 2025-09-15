import time
import random
from subjects import subjects
from player import Player

class ControlFlow:

    outer_id = None
    @staticmethod
    def select_subject():
        
        random_number_subject = random.randrange(len(subjects))
        
        for subject in subjects:
            if random_number_subject == subjects.index(subject):
                
            
                print("Spinning...")
                time.sleep(3)
                
                print("Category: ", subject.category)
                time.sleep(1)
                
                question = random.choice(list(subject.questions.items()))
                print(question[0])
                return question[1]
                #input the user for an answer, and if it's the same as the second element in the list, he's correct.Otherwise, he isn't
        
    @staticmethod
    def recieve_and_checkanswer(players_answer, correct_answer):
        
        if players_answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect!")

    @staticmethod
    def assign_points(current_player):
        current_player.points += 1

    @staticmethod
    def select_next_player(players_list):
        if players_list[0].next_round_value == 0:
            
            next_player = players_list[0]
            ControlFlow.outer_id = players_list[0].pid  #outer ID becomes 0
            players_list[0].next_round_value += 1
            return next_player
        
        for player in players_list:
            if player.pid == ControlFlow.outer_id + 1 and player.next_round_value == 0:
                next_player = player
                ControlFlow.outer_id = player.pid #outer ID becomes > 0
                player.next_round_value += 1
                return next_player
        

        '''I was able to create this simple method that chooses the next player in the round based on its player ID and a counter, that can be eitehr
                0 or 1. The player either participated in the round or it didn't'''

    @staticmethod
    def order_players(players_list):
        
        sorted_list = sorted(players_list, key=lambda p: p.pid)
        print(sorted_list)

    @staticmethod
    def create_players(): 
        
        players = []
        x = 0
        next_id = 0
        while x < 4:
            if x >= 1:
                quit_process = str(input("Want to add an other player? Y/N: "))
                if quit_process == "N":
                    break
                else:
                    pass
            x += 1

            user_input_name = str(input("Enter username: "))
            player = Player(user_input_name, 0, None, next_id)
            next_id += 1
            players.append(player)
        
        
        return players
    
    @staticmethod
    def end_round(players_list):
        for player in players_list:
            player.next_round_value = 0

