import time
import random
from subjects import subjects
from player import Player

class ControlFlow:

    """This variable helps to choose the next player in the round by storing the first users ID number.
    After that, it will increase by one, so the function selects the next users who's ID matchers the previous users ID + 1
    It is initialized as None"""
    outer_id = None 
    
    """This variable counts the number of rounds. After 3 rounds, the code calls the finish_game() function"""
    round_counter = 0
    
    """This variable helps to determine when a round should end. In every iteration it is chekced wether this value matches the value of len(players).
    If it does, the round ends. Logic has flaws, I need to check on this later."""
    count_rounds_til_end = 0

    """Remains true only before the first round of the game starts, if ture the script lists all the players.
    This only happens once, at the start of the game."""
    flag_for_players_list = True

    """Counts the number of points a player collected in a round. If he fails a question, the points reduce by 50%"""
    points_in_round = 0

    """It takes questions that were already used in game, so they dont appear again"""
    questions_asked = []

    @staticmethod
    def select_subject():
        
        random_number_subject = random.randrange(len(subjects))
        
        for subject in subjects:
            if random_number_subject == subjects.index(subject):
                print("Spinning...")
                time.sleep(3)
                
                print("Category: ", subject.category)
                return subject
                
    @staticmethod
    def select_question(subject):

        while True:
            time.sleep(1)
            question = random.choice(list(subject.questions.items())) 
            if question[0] in ControlFlow.questions_asked:
                continue
            ControlFlow.questions_asked.append(question[0])
            print(question[0])
            return question[1]
    
    @staticmethod
    def recieve_and_checkanswer(players_answer, correct_answer,current_player):
        
        if players_answer == correct_answer:
            print("Correct!")
            #current_player.points += 1000
            return True
        else:
            print("Incorrect!")
            time.sleep(1)
            return False

   

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

    @staticmethod
    def create_players(): 
        
        names_taken = []
        players = []
        x = 0
        next_id = 0
        while x < 4:
            if x >= 1:
                quit_process = str(input("Want to add an other player? Y/N: "))
                if quit_process.lower() == "n":
                    break
                else:
                    pass
            user_input_name = str(input("Enter username: "))
            if len(user_input_name) > 10:
                print("Username can't exceed 10 charachters.")
                time.sleep(1)
                print("Current iteration: ", x)
                continue
            elif user_input_name in names_taken:
                print("This name is taken")
                time.sleep(1)
                print("Current iteration: ", x)
                continue
            names_taken.append(user_input_name)
            x += 1

            player = Player(user_input_name, 0, None, next_id)
            next_id += 1
            players.append(player)
        
        
        return players
    
    @staticmethod
    def end_round(players_list, outer_id):
        for player in players_list:
            player.next_round_value = 0
            outer_id = 0

    @staticmethod
    def finish_game(players_list):
        sorted_list = sorted(players_list, key=lambda p: p.points)
        print("The winner is: ",sorted_list[-1])


        pass
        """Function should chose the winner player, and order the rest of them according to their points.
        If its a draw, it's a draw..for so far
        maybe the two players should be able to deciede on whether or not compete for some more time
        This happens when players hit the last round, which should be 3 so far, so testing can be easier.
        """
    @staticmethod
    def convert_input(userinput):
        if userinput.isdigit():
            return int(userinput)
        else:
            return userinput
