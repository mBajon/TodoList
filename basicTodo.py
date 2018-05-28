from choice import Choice, exitChoice
from Menu import Menu

class Todos():
    def __init__(self):
        self.TodoDict={}

    def addTodo(self,Todo):
        self.TodoDict[Todo.date]=Todo.todotext

    def delTodo(self,Date):
        self.TodoDict.pop(Date)
    
    def __str__(self):
        return print(self.TodoDict)

class Todo():
    def __init__(self,date,text):
        self.date=date
        self.todotext=text

if __name__=="__main__":
    menu = Menu("Please select an item")
    menu.addChoice([
        Choice('Add Todo'), Choice('Delete Todo'),Choice('View Todos'), exitChoice('Exit')
    ])
    menu.view()


        
