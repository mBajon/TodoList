import unittest
from todo.app.todos import Todos
#from ..Todos import Todos

class Todos_test(unittest.TestCase):
    TestTodo=Todos()
    assert TestTodo
    #assert(isinstance(TestTodo,Todos),True)
    

if __name__ == '__main__':
    unittest.main()