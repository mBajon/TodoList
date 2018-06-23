from Todos import Todo,Todos



class Choice(object):
    MainTodo=Todos()

    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc
        self.map_on_select=MethodDictionary
        #self.MainTodo=Todos()

    def printSelected(self):
        print("**'{}' was selected".format(self.choiceDesc))

    def onSelect(self,index):
        self.map_on_select[index](self)

    def on_add(self):
        self.printSelected()
        #print("**'{}' was selected".format(self.choiceDesc))
        try:
            user_input=input("Please add the Todo: \n")
            Choice.MainTodo.addTodo(Todo(user_input))
            print(id(Choice.MainTodo))
            print("\n {} was added".format(user_input))
        except Exception:
            print("sth went wrong")
    
    def on_delete(self):
        self.printSelected()
        try:
            user_input=input("Please provide the Todo id to be deleted: \n")
            deletedTodoId=int(user_input.strip())
            Choice.MainTodo.delTodo(deletedTodoId)
            print("** Todo id:'{}' was deleted".format(deletedTodoId))
        except KeyError:
            print("Please provide a valid ToDo ID")

    def on_modify(self):
        user_input=input("Please provide the Todo id to be modified: \n")
        modifiedTodoID=int(user_input.strip())
        user_new_todo_desc=input("Please provide the new todo description: \n")
        Choice.MainTodo.modTodo(modifiedTodoID,user_new_todo_desc)
        print("** Todo id:'{}' was modified".format(modifiedTodoID))

    def on_view(self):
        Choice.MainTodo.__str__()

class exitingChoice(Choice):
    def onSelect(self):
        #self.printSelected()
        print("bye bye ")
        raise SystemExit

MethodDictionary={
                  1:Choice.on_add,
                  2:Choice.on_modify,
                  3:Choice.on_delete,
                  4:Choice.on_view,
                  5:exitingChoice.onSelect
                 }