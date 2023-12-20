import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_even_number_of_evens(self):
        self.assertEqual(even_number_of_evens(5), False)
        self.assertEqual(even_number_of_evens(10), True)
        self.assertEqual(even_number_of_evens(15), False)
        self.assertEqual(even_number_of_evens(20), True)
        self.assertEqual(even_number_of_evens(25), False)
        self.assertEqual(even_number_of_evens(30), True)
        self.assertEqual(even_number_of_evens(35), False)
        self.assertEqual(even_number_of_evens(40), True)
        self.assertEqual(even_number_of_evens(45), False)
        self.assertEqual(even_number_of_evens(50), True)
        self.assertEqual(even_number_of_evens(55), False)
        self.assertEqual(even_number_of_evens(60), True)
        self.assertEqual(even_number_of_evens(65), False)



if __name__ == "__main__":
    unittest.main()
