from choice  import  Choice, exitingChoice
from Menu import Menu
from Todos import Todos


if __name__=="__main__":

    menu = Menu("Please select an item")
    menu.addChoice(
    [
        Choice('Add Todo'),Choice('Modify Todo'),Choice('Delete Todo'),Choice('View Todos'), exitingChoice('Exit')
    ])
    menu.view()
