class Todos():

    TodoDict={}

    def addTodo(self,Todo):
        self.TodoDict[Todo.date]=Todo.todotext

    def delTodo(self,Date):
        self.TodoDict.pop(Date)
    
    def __str__(self):
        for key, value in self.TodoDict.items():
            print("date:{}  value:{}".format(key,value))

class Todo():
    def __init__(self,date,text):
        self.date=date
        self.todotext=text