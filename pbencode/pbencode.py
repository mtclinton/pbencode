"""Library for encoding and decoding values using bencode specification"""
from __future__ import annotations

import itertools


def encode(input_value: bytes | int | str | list | dict) -> bytes:
    """Encode input value using bencode specification"""

    if isinstance(input_value, bytes):
        return str(len(input_value)).encode("UTF-8") + b":" + input_value
    if isinstance(input_value, int):
        return b"i" + str(input_value).encode("UTF-8") + b"e"
    if isinstance(input_value, str):
        return encode(input_value.encode("UTF-8"))
    if isinstance(input_value, list):
        return b"l" + b"".join(map(encode, input_value)) + b"e"
    if isinstance(input_value, dict):
        if not all(isinstance(i, bytes) for i in input_value.keys()):
            raise ValueError("dict keys should be bytes")
        items = list(input_value.items())
        items.sort()
        return b"d" + b"".join(map(encode, itertools.chain(*items))) + b"e"
    return bytes(0)
