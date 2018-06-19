from Todos import Todo,Todos

MainTodo=Todos()

class Choice(object):

    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc
    
    def printSelected(self):
        print("**'{}' was selected".format(self.choiceDesc))

    def onSelect(self):
        pass


class exitingChoice(Choice):
    def onSelect(self):
        self.printSelected()
        print("bye bye ")
        raise SystemExit

class addingChoice(Choice):
    def onSelect(self):
        self.printSelected()
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
        self.printSelected()
        try:
            self.onDelete(MainTodo)
        except KeyError:
            print("Please provide a valid ToDo ID")

    def onDelete(self,MainTodo):
        user_input=input("Please provide the Todo id to be deleted: \n")
        deletedTodoId=int(user_input.strip())
        MainTodo.delTodo(deletedTodoId)
        print("** Todo id:'{}' was deleted".format(deletedTodoId))

class modifingChoice(Choice):
    def onSelect(self,MainTodo):
        user_input=input("Please provide the Todo id to be modified: \n")
        modifiedTodoID=int(user_input.strip())
        user_new_todo_desc=input("Please provide the new todo description: \n")
        MainTodo.modTodo(modifiedTodoID,user_new_todo_desc)
        print("** Todo id:'{}' was modified".format(modifiedTodoID))

MethodDictionary={
                  1:addingChoice.onSelect,
                  2:modifingChoice.onSelect,
                  3:deletingChoice.onSelect,
                  4:MainTodo.__str__,
                  5:exitingChoice.onSelect
                 }