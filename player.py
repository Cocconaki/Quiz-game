

class Player:

    def __init__(self, name:str, next_round_value:int = None, points:int=None, pid:int=None):
        if points is None:
            self.points = 0
        else:
            self.points = points
        if next_round_value is None:
            self.next_round_value = 0
        else:
            self.next_round_value = next_round_value
        self.name = name
        
        if pid is None:
            self.pid = 0
        else:
            self.pid = pid

    def __repr__(self):
        return f"Name:{self.name}, ID: {self.pid}, Points:{self.points}"
    



