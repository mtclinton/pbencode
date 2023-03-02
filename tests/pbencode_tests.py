"""Testing of pbencode library"""
import unittest

from pbencode import encode


class TestEncodeDecode(unittest.TestCase):
    """Testing of pbencode encoding"""

    def test_encode_int(self):
        """Testing of pbencode int encoding"""

        self.assertEqual(encode(4), b"i4e")
        self.assertEqual(encode(0), b"i0e")
        self.assertEqual(encode(42), b"i42e")
        self.assertEqual(encode(-42), b"i-42e")

    def test_encode_bytes(self):
        """Testing of pbencode bytes encoding"""

        self.assertEqual(encode(b"spam"), b"4:spam")

    def test_encode_str(self):
        """Testing of pbencode str encoding"""

        self.assertEqual(encode("spam"), b"4:spam")

    def test_encode_list(self):
        """Testing of pbencode list encoding"""

        self.assertEqual(encode(["spam", 42]), b"l4:spami42ee")

    def test_encode_dict(self):
        """Testing of pbencode dict encoding"""

        self.assertEqual(encode({b"bar": "spam", b"foo": 42}), b"d3:bar4:spam3:fooi42ee")


if __name__ == "__main__":
    unittest.main()
