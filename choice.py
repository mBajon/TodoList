
class Choice(object):
    def __init__(self,choiceDesc):
        self.choiceDesc=choiceDesc
    def onSelect(self,index):
        print("**'{}' was selected".format(self.choiceDesc))

        if index==1:
            user_input=input("Please add the Todo: \n")
            Todos.addTodo(1,user_input)
        elif index ==2:
            Todos.delTodo
        elif index==3:
            pass
        return self
class exitChoice(Choice):
    def onSelect(self):
        print("bye bye ")
        raise SystemExit
