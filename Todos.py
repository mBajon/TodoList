class Todos():

    TodoDict={}

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