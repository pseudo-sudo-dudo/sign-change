import unittest
from sign_change import SignChanger


class TestSignChange(unittest.TestCase):
    # basic tests
    def test_case1(self):
        sc = SignChanger()

        str1 = "Hello World"
        str2 = "hold On"
        expected = {'N': 1}
        actual, _ = sc.find_differences(str1, str2)
        self.assertEqual(actual, expected)

    def test_case2(self):
        sc = SignChanger()

        str1 = "Python"
        str2 = "python programming"
        expected = {'P': 1, 'R': 2, 'O': 1, 'G': 2, 'A': 1, 'M': 2, 'I': 1, 'N': 1}
        actual, _ = sc.find_differences(str1, str2)
        self.assertEqual(actual, expected)

    def test_case3(self):
        sc = SignChanger()
        str1 = "ABCD"
        str2 = "abcd"
        expected = {}  # No differences when case is ignored
        actual, _ = sc.find_differences(str1, str2)
        self.assertEqual(actual, expected)

    # real life example of church signs:
    def test_case4(self):
        sc = SignChanger()
        str1 = "CHOIR & ORCHESTRA CHRISTMAS CANTATA 7:30PM, DEC. 12"
        str2 = "DEC 15, 9AM WORSHIP 11AM WORSHIP AND CHRISTMAS PAGEANT"
        expected = {'D': 1, '1': 2, '5': 1, '9': 1, 'A': 1, 'M': 1, 'W': 2, 'S': 1, 'I': 1, 'P': 2, 'N': 1, 'G': 1}
        actual, _ = sc.find_differences(str1, str2)
        self.assertEqual(actual, expected)


# Run the tests
if __name__ == '__main__':
    unittest.main()