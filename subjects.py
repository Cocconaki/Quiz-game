

class Subject:

    def __init__(self, category:str, questions:dict=None):
        
        self.category = category
        
        if questions is None:
            self.questions = {}
        else:
            self.questions = questions


subject1 = Subject("History", {"When did ww1 start?":1914,"When asdasd":1914,"When did ww1 s":1914,"When ":1914})
subject2 = Subject("Phisics",{"What letter is the symbol of gravity?":"g","When dfff":1914,"Whewewe":1914,"When art?":1914})
subject3 = Subject("Movies", {"Who is the protagonLotr?":"Frodggins","art?":1914,"?":1914,})
subject4 = Subject("Programming", {"What language is considered to be the descendant of Java?":"Kotlin"})


subjects = [subject1, subject2, subject3, subject4]
 