#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

+------+--------------------------------------------------+
| Size |                     Meaning                      |
+------+--------------------------------------------------+
| 1    | Number of following bytes for the algorithm name |
| x    | Name of the algorithm                            |
| 4    | Number of iterations as unsigned integer         |
| 2    | Number of following bytes for the salt           |
| x    | Salt                                             |
| 2    | Number of following bytes for the hash           |
| x    | Hash                                             |
+------+--------------------------------------------------+

"""
import io
import typing as t


__all__ = ['dumps', 'loads', 'Loaded', 'extract_algorythm', 'extract_iterations', 'extract_salt', 'extract_hashed']


class SizeBytes:
    ALGORITHM: int = 1
    ITERATIONS: int = 4
    SALT: int = 2
    HASHED: int = 2


def dumps(algorithm: str, iterations: int, salt: bytes, hashed: bytes) -> bytes:
    r"""
    Dumps all relevant information about the hashed password into bytes to be stored in a database or other medium

    :param algorithm: the algorithm used for hashing the password
    :param iterations: the number of iterations the algorithm was used
    :param salt: the salt
    :param hashed: the final result
    :return: dumped information as bytes
    """
    if len(algorithm) == 0:
        raise ValueError("Bad Algorithm")

    parts: t.List[bytes] = []

    algo = algorithm.encode()
    parts.append(len(algo).to_bytes(SizeBytes.ALGORITHM, byteorder='big', signed=False))
    parts.append(algo)

    parts.append(iterations.to_bytes(SizeBytes.ITERATIONS, byteorder='big', signed=False))

    parts.append(len(salt).to_bytes(SizeBytes.SALT, byteorder='big', signed=False))
    parts.append(salt)

    parts.append(len(hashed).to_bytes(SizeBytes.HASHED, byteorder='big', signed=False))
    parts.append(hashed)

    return b''.join(parts)


class Loaded(t.NamedTuple):
    algorithm: str
    iterations: int
    salt: bytes
    hashed: bytes


def loads(dump: bytes, *, verify: bool = False) -> Loaded:
    r"""
    Loads all relevant information about the hashed password from a dump and returns it as a NamedTuple

    class Loaded(NamedTuple):
        algorithm: str
        iterations: int
        salt: bytes
        hashed: bytes

    :param dump: the bytes that store all information
    :param verify: verify
    :return:
    """
    stream = io.BytesIO(dump)

    algo_length = int.from_bytes(stream.read(SizeBytes.ALGORITHM), byteorder='big', signed=False)
    algo = stream.read(algo_length).decode()

    iterations = int.from_bytes(stream.read(SizeBytes.ITERATIONS), byteorder='big', signed=False)

    salt_length = int.from_bytes(stream.read(SizeBytes.SALT), byteorder='big', signed=False)
    salt = stream.read(salt_length)
    if len(salt) != salt_length:
        raise ValueError(f"dumped information-salt has an invalid length")

    hashed_length = int.from_bytes(stream.read(SizeBytes.HASHED), byteorder='big', signed=False)
    hashed = stream.read(hashed_length)
    if len(hashed) != hashed_length:
        raise ValueError(f"dumped information-hash has an invalid length")

    if verify and stream.read(1) != b'':
        raise ValueError(f"dumped information has an invalid length")

    return Loaded(algo, iterations, salt, hashed)


def extract_algorythm(dump: bytes) -> str:
    r"""

    :param dump:
    :return:
    """
    stream = io.BytesIO(dump)
    algo_length = int.from_bytes(stream.read(SizeBytes.ALGORITHM), byteorder='big', signed=False)
    algo = stream.read(algo_length).decode()
    return algo


def extract_iterations(dump: bytes) -> int:
    stream = io.BytesIO(dump)
    algo_length = int.from_bytes(stream.read(SizeBytes.ALGORITHM), byteorder='big', signed=False)
    stream.seek(stream.tell() + algo_length)
    iterations = int.from_bytes(stream.read(SizeBytes.ITERATIONS), byteorder='big', signed=False)
    return iterations


def extract_salt(dump: bytes) -> bytes:
    stream = io.BytesIO(dump)
    algo_length = int.from_bytes(stream.read(SizeBytes.ALGORITHM), byteorder='big', signed=False)
    stream.seek(stream.tell() + algo_length + SizeBytes.ITERATIONS)
    salt_length = int.from_bytes(stream.read(SizeBytes.SALT), byteorder='big', signed=False)
    salt = stream.read(salt_length)
    return salt


def extract_hashed(dump: bytes) -> bytes:
    stream = io.BytesIO(dump)
    algo_length = int.from_bytes(stream.read(SizeBytes.ALGORITHM), byteorder='big', signed=False)
    stream.seek(stream.tell() + algo_length + SizeBytes.ITERATIONS)
    salt_length = int.from_bytes(stream.read(SizeBytes.SALT), byteorder='big', signed=False)
    stream.seek(stream.tell() + salt_length)
    hashed_length = int.from_bytes(stream.read(SizeBytes.HASHED), byteorder='big', signed=False)
    hashed = stream.read(hashed_length)
    return hashed
