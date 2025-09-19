
import json

with open("testing.json", "r") as f:
    data = json.load(f)

topics = []
for key, value in list(data.items()):
    topics.append(key)

class Subject:

    def __init__(self, category:str, questions:dict=None):
        
        self.category = category
        
        if questions is None:
            self.questions = {}
        else:
            self.questions = questions
    
    def __repr__(self):
        return f"Subject name: {self.category}"


subject1 = Subject("history", None)
subject2 = Subject("music", None)
subject3 = Subject("phisics", None)
subjects = [subject1,subject2,subject3]


for subject in subjects:
    subject.questions = data[subject.category]
    print(subject.questions, subject.category)
