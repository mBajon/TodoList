from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
from choice import Choice,exitChoice

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
                x=int(user_input.strip())
                choice=self.choices[x-1]
                choice.onSelect(x)
            except ValueError:
                    prompt="ERROR please input an integer in {}-{}?\n".format(1, len(self.choices))
                    continue 
            

        


