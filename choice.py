from Todos import Todo,Todos

MainTodo=Todos()

class Choice(object):

    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc

    def onSelect(self,index):
        print("**'{}' was selected".format(self.choiceDesc))

        if index==1:
            try:
                self.onAdd(MainTodo)
            except Exception:
                print("sth went wrong")
        elif index ==2:
            try:
                self.onDelete(MainTodo)
            except KeyError:
                print("Please provide a valid ToDo ID")
        elif index==3:
            MainTodo.__str__()
        else:
            exitChoice.onSelect()
        return self

    def onDelete(self,MainTodo):
        user_input=input("Please provide the Todo id: \n")
        deletedTodoId=int(user_input.strip())
        MainTodo.delTodo(deletedTodoId)
        print("** Todo id:'{}' was deleted".format(deletedTodoId))

    def onAdd(self,MainTodo):
            user_input=input("Please add the Todo: \n")
            MainTodo.addTodo(Todo(user_input))
            print("\n {} was added".format(user_input))        


class exitChoice(Choice):
    def onSelect(self):
        print("bye bye ")
        raise SystemExit
