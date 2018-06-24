import itertools

class Todos():

    TodoDict={}

    def addTodo(self,Todo):
        self.TodoDict[Todo.id]=Todo.todotext

    def delTodo(self,TodoId):
        if self.TodoDict:
            self.TodoDict.pop(TodoId)
        else:
            print("There are no ToDos to delete...")

    def modTodo(self,TodoId,NewTodoDesc):
        if self.TodoDict:
            self.TodoDict[TodoId]=NewTodoDesc
        else:
            print("There are no ToDos to modify...")
     
    
    def __str__(self):
        for key, value in self.TodoDict.items():
            print("id:{}  value:{}".format(key,value))

class Todo():
    id=itertools.count(0,1)
    def __init__(self,text):
        self.id=Todo.id.__next__()
        self.todotext=text
