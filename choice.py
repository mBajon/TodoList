from Todos import Todo,Todos

class Choice(object):
    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc
    def onSelect(self,index):
        print("**'{}' was selected".format(self.choiceDesc))
        MainTodo=Todos()
        if index==1:
            user_input=input("Please add the Todo: \n")
            MainTodo.addTodo(Todo(1,user_input))
            print("\n {} was added".format(user_input))
        elif index ==2:
            MainTodo.delTodo
        elif index==3:
            MainTodo.__str__()
        return self
class exitChoice(Choice):
    def onSelect(self):
        print("bye bye ")
        raise SystemExit
