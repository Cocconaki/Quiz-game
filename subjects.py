import json

with open(r"C:\Users\admin\Desktop\Coding\quiz game project\testing.json", "r") as f:
    data = json.load(f)

class Subject:

    def __init__(self, category:str, questions:dict=None):
        
        self.category = category
        
        if questions is None:
            self.questions = {}
        else:
            self.questions = questions
    
    def __repr__(self):
        return f"Subject name: {self.category}"


subject1 = Subject("History", None)
subject2 = Subject("Phisics", None)
subject3 = Subject("Movies", None)
subject4 = Subject("Programming", None)


subjects = [subject1, subject2, subject3, subject4]
for subject in subjects:
    subject.questions = data[subject.category]
