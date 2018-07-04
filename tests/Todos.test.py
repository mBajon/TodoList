import itertools
import unittest
import sys
sys.path.append('../')
from app import Todos as t

class Todos_Test(unittest.TestCase):
    
    def test_todos(self):
        self.TestTodos=t.Todos()
        self.assertIsInstance(self.TestTodos,t.Todos)
    
    def test_adding_todo(self):
        self.TestTodos=t.Todos()
        self.test_todo=t.Todo
        self.TestTodos.addTodo(self.test_todo("hello"))
        test_dict_size=len(self.TestTodos.TodoDict)
        self.assertEqual(test_dict_size,1)

    def test_modyfying_todo(self):
        self.TestTodos=t.Todos()
        self.test_todo=t.Todo
        self.TestTodos.addTodo(self.test_todo("hello"))
        self.TestTodos.modTodo(0,"nonie")
        self.assertEqual(self.TestTodos.TodoDict[0],"nonie")

    def test_deleting_a_todo(self):
        self.TestTodos=t.Todos()
        self.test_todo=t.Todo
        self.TestTodos.addTodo(self.test_todo("hello"))
        self.TestTodos.delTodo(1)
        test_dict_size=len(self.TestTodos.TodoDict)
        print(test_dict_size)
        self.assertEqual(test_dict_size,0)
        

if __name__ == '__main__':
    unittest.main()
