from choice import Choice, exitingChoice, addingChoice,deletingChoice,modifingChoice
from Menu import Menu
from Todos import Todos


if __name__=="__main__":

    menu = Menu("Please select an item")
    menu.addChoice(
    [
        addingChoice('Add Todo'),modifingChoice('Modify Todo'),deletingChoice('Delete Todo'),Choice('View Todos'), exitingChoice('Exit')
    ])
    menu.view()
