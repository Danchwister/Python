import unittest
from bubble import bubble_sort

class TestBubble(unittest.TestCase):
   
   def test_bubble_sort(self):
        lista = [2,1,5,4]
        lista_esperada= [1,2,4,5]
        bubble_sort(lista)
        self.assertEqual(lista, lista_esperada)

if __name__ == '__main__':
    unittest.main()

