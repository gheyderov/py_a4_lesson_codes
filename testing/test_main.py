from main import sum, divide
import unittest


class CalcTest(unittest.TestCase):

    def test_sum(self):
        a = 4
        b = 2
        expected_result = 6
        actual_result = sum(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        a = 4
        b = 2
        expected_result = 2
        actual_result = divide(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide_with_zero_args(self):
        a = 4
        b = 0
        self.assertRaises(ZeroDivisionError, divide, a, b)
        




if __name__ == '__main__':
    unittest.main()