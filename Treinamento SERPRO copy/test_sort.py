import unittest
from sort import SortTroca

class test_sort(unittest.TestCase):

    def test_sort(self):
        lista = [2,1,5,9,4,5,6,8,2,3]
        lista_esperada = [1, 2, 2, 3, 4, 5, 5, 6, 8, 9]
        SortTroca(lista)
        self.assertEqual(lista, lista_esperada)

if __name__ == '__main__':
    unittest.main()

    