from naive import exact_naive
import unittest

### INPUT PARAMETERS ###

ref1 = "123456789"
ref2 = "ababc"
ref3 = "abchhhabc"
ref4 = "hfhab"

seq = "abc"


class TestNaive(unittest.TestCase):
    def test1(self):
        result = exact_naive(seq,ref1)
        self.assertEqual(result, [] )

    def test2(self):
        result = exact_naive(seq,ref2)
        self.assertEqual(result, [[2, ['a', 'b', 'c']]])

    def test3(self):
        result = exact_naive(seq,ref3)
        self.assertEqual(result, [[0, ['a', 'b', 'c']],[6, ['a', 'b', 'c']]])

    def test4(self):
        result = exact_naive(seq,ref4)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()