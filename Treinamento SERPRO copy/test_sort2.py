import unittest
from sort2 import bubble_sort

class TesteSort(unittest.TestCase):

    def TestSort(self):
        array = [2,1,5,4]
        array_esperado = [1,2,4,5]
        bubble_sort(array)
        self.assertEqual(array, array_esperado)

if __name__ == '__main__':
    unittest.main()


