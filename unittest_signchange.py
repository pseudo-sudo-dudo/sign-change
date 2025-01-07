import unittest
from sign_change import SignChanger


class TestSignChange(unittest.TestCase):
    def test_case1(self):
        sc = SignChanger()

        str1 = "Hello World"
        str2 = "hold On"
        expected = {'N': 1}
        actual, _ = sc.find_differences(str1, str2)
        self.assertEqual(actual, expected)


# Run the tests
if __name__ == '__main__':
    unittest.main()