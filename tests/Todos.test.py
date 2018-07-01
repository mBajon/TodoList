import unittest
import app.Todos
#from ..Todos import Todos

class Todos_test(unittest.TestCase):
    TestTodo=app.Todos.Todos()
    #assert(isinstance(TestTodo,Todos),True)
    

if __name__ == '__main__':
    unittest.main()