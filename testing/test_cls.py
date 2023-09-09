from cls import Calc
import unittest


class CalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        a = 4
        b = 2
        cls.c = Calc(a, b)
        print('setup')

    def test_sum(self):
        expected_result = 6
        actual_result = self.c.sum()
        self.assertEqual(expected_result, actual_result)
        print('sum')

    def test_divide(self):
        expected_result = 2
        actual_result = self.c.divide()
        self.assertEqual(expected_result, actual_result)
        print('divide')

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.c
        print('teardown')



if __name__ == '__main__':
    unittest.main()