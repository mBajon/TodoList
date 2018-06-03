from choice import Choice, exitChoice
from Menu import Menu
from Todos import Todos


if __name__=="__main__":

    menu = Menu("Please select an item")
    menu.addChoice([
        Choice('Add Todo'), Choice('Delete Todo'),Choice('View Todos'), exitChoice('Exit')
    ])
    menu.view()


        
