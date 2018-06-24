from choice import Choice,MethodDictionary,exitingChoice

class Menu():
    def __init__(self,question):
        self.question= question
        self.choices=[]
    
    def addChoice(self,choice):
        self.choices.extend(choice)

    def view(self):
        choice_list = "\n".join("  {}){}".format(i, c.choiceDesc ) for i, c in enumerate(self.choices,1))
        first_line="""{}\n{}\n""".format(self.question, choice_list)
        prompt = "?"
        
        while True:
            user_input=input(first_line+prompt+"\n")
            try:
                userChoice=int(user_input.strip())
                choice=self.choices[userChoice-1]
                if userChoice!=5:
                    Choice.onSelect(choice,userChoice)
                else:
                    exitingChoice.onSelect(self)
            except ValueError:
                    print("ERROR please input an integer in {}-{}?\n".format(1, len(self.choices)))
            except IndexError:
                    print("ERROR please input an integer in {}-{}?\n".format(1, len(self.choices))) 
            continue 
            