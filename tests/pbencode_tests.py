"""Testing of pbencode library"""
import unittest

from pbencode import decode
from pbencode import encode


class TestEncode(unittest.TestCase):
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


class TestDecode(unittest.TestCase):
    """Testing of pbencode decoding"""

    def test_decode_int(self):
        """Testing of pbencode int decoding"""

        self.assertEqual(decode(b"i4e"), 4)
        self.assertEqual(decode(b"i0e"), 0)
        self.assertEqual(decode(b"i42e"), 42)
        self.assertEqual(decode(b"i-42e"), -42)

    def test_decode_bytes(self):
        """Testing of pbencode bytes decoding"""

        self.assertEqual(decode(b"4:spam"), b"spam")

    def test_decode_str(self):
        """Testing of pbencode str decoding"""

        self.assertEqual(decode("4:spam"), b"spam")

    def test_decode_list(self):
        """Testing of pbencode list decoding"""

        self.assertEqual(decode(b"l4:spami42ee"), [b"spam", 42])

    def test_decode_dict(self):
        """Testing of pbencode dict decoding"""

        self.assertEqual(decode(b"d3:bar4:spam3:fooi42ee"), {b"bar": b"spam", b"foo": 42})


if __name__ == "__main__":
    unittest.main()
