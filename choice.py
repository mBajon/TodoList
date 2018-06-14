from Todos import Todo,Todos

MainTodo=Todos()

class Choice(object):

    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc
    
    def printSelected(self):
        print("**'{}' was selected".format(self.choiceDesc))

    def onSelect(self,index):
        pass


class exitingChoice(Choice):
    def onSelect(self):
        print("bye bye ")
        raise SystemExit

class addingChoice(Choice):
    def onSelect(self,index):
        print("**'{}' was selected".format(self.choiceDesc))
        try:
            self.onAdd(MainTodo)
        except Exception:
            print("sth went wrong")
    
    def onAdd(self,MainTodo):
            user_input=input("Please add the Todo: \n")
            MainTodo.addTodo(Todo(user_input))
            print("\n {} was added".format(user_input))
            return self

class deletingChoice(Choice):
    def onSelect(self,index):
        try:
            self.onDelete(MainTodo)
        except KeyError:
            print("Please provide a valid ToDo ID")

    def onDelete(self,MainTodo):
        user_input=input("Please provide the Todo id: \n")
        deletedTodoId=int(user_input.strip())
        MainTodo.delTodo(deletedTodoId)
        print("** Todo id:'{}' was deleted".format(deletedTodoId))