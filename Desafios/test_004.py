import unittest

def media(notas):
    return sum(notas) / len(notas)

class TestMedia(unittest.TestCase):

    def test_media(self):
        notas = [7.5, 8.0, 6.5, 9.0] # valores esperados
        self.assertEqual(media(notas), 7.5) # verificação

if __name__ == '__main__':
    unittest.main()
    