import time
import random
from subjects import subjects
from player import Player

class ControlFlow:

    @staticmethod
    def select_subject():
        
        return_subject = None
        random_number_subject = random.randrange(len(subjects))
        
        for subject in subjects:
            if random_number_subject == subjects.index(subject):
                
                return_subject = subject
                random_number_question = random.randrange(len(subject.questions))
                
                print("Spinning...")
                time.sleep(3)
                
                print("Category: ", subject.category)
                
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
    def assign_points():
        pass

    @staticmethod
    def select_next_player(players_list):
        pass
       

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
            player = Player(user_input_name, None, None, next_id)
            next_id += 1
            players.append(player)
        
        
        return players


