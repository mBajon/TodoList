from Todos import Todo,Todos

class Choice(object):

    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc

    def onSelect(self,index):
        print("**'{}' was selected".format(self.choiceDesc))
        MainTodo=Todos()
        if index==1:
            user_input=input("Please add the Todo: \n")
            MainTodo.addTodo(Todo(user_input))
            print("\n {} was added".format(user_input))
            
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


class exitChoice(Choice):
    def onSelect(self):
        print("bye bye ")
        raise SystemExit
