"""Library for encoding and decoding values using bencode specification"""
from __future__ import annotations

import itertools
import re


def encode(input_value: bytes | int | str | list | dict) -> bytes:
    """Encode input value using bencode specification"""

    if isinstance(input_value, bytes):
        return str(len(input_value)).encode() + b":" + input_value
    if isinstance(input_value, int):
        return b"i" + str(input_value).encode() + b"e"
    if isinstance(input_value, str):
        return encode(input_value.encode())
    if isinstance(input_value, list):
        return b"l" + b"".join(map(encode, input_value)) + b"e"
    if isinstance(input_value, dict):
        if not all(isinstance(i, bytes) for i in input_value.keys()):
            raise ValueError("dict keys should be bytes")
        items = list(input_value.items())
        items.sort()
        return b"d" + b"".join(map(encode, itertools.chain(*items))) + b"e"
    return bytes(0)


def decode(input_value: bytes | str) -> bytes | int | str | list | dict:
    """Decode input value using bencode specification"""

    if isinstance(input_value, str):
        input_value = input_value.encode()
    if input_value.startswith(b"i"):
        first_int = re.match(b"i(-?\\d+)e", input_value)
        if first_int:
            return int(first_int.group(1))
        raise ValueError("Malformed input.")
    if input_value.startswith(b"l"):
        res = []
        input_value = input_value[1:]
        while not input_value.startswith(b"e"):
            val = decode(input_value)
            res.append(val)
            input_value = input_value[len(encode(val)) :]
        return res
    if input_value.startswith(b"d"):
        res = []
        input_value = input_value[1:]
        while not input_value.startswith(b"e"):
            val = decode(input_value)
            res.append(val)
            input_value = input_value[len(encode(val)) :]
        return dict(zip(res[::2], res[1::2]))
    if any(input_value.startswith(str(i).encode()) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        val_length = re.match(b"(\\d+):", input_value)
        if val_length:
            length = int(val_length.group(1))
            start = val_length.span()[1]
            end = start + length
            return input_value[start:end]
        raise ValueError("Malformed input.")
    raise ValueError("Malformed input.")
