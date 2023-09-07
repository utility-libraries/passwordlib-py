#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestUtil(unittest.TestCase):
    def test_import_util(self):
        import passwordlib.util  # noqa

    def test_salt_generation(self):
        from passwordlib.util import generate_salt
        self.assertIsInstance(generate_salt(), bytes)
        self.assertEquals(len(generate_salt(length=32)), 32)
        self.assertEquals(len(generate_salt(length=64)), 64)

    def test_dumping(self):
        from passwordlib.util import (
            dumps,
            get_algorithm, get_iterations, get_salt
        )
        algorithm = get_algorithm()
        iterations = get_iterations()
        salt = get_salt()
        hashed = b'hashed'

        dumped = dumps(algorithm=algorithm, iterations=iterations, salt=salt, hashed=hashed)

        self.assertIsInstance(dumped, bytes)

    def test_loading(self):
        from passwordlib.util import (
            dumps, loads,
            get_algorithm, get_iterations, get_salt
        )
        algorithm = get_algorithm()
        iterations = get_iterations()
        salt = get_salt()
        hashed = b'hashed'

        dumped = dumps(algorithm=algorithm, iterations=iterations, salt=salt, hashed=hashed)
        loaded = loads(dumped, verify=True)

        self.assertEquals(loaded.algorithm, algorithm)
        self.assertEquals(loaded.iterations, iterations)
        self.assertEquals(loaded.salt, salt)
        self.assertEquals(loaded.hashed, hashed)

    def test_redumping(self):
        from passwordlib.util import (
            dumps, loads,
            get_algorithm, get_iterations, get_salt,
        )
        algorithm = get_algorithm()
        iterations = get_iterations()
        salt = get_salt()
        hashed = b'hashed'

        dumped = dumps(algorithm=algorithm, iterations=iterations, salt=salt, hashed=hashed)
        loaded = loads(dumped, verify=True)

        dumped2 = dumps(algorithm=loaded.algorithm, iterations=loaded.iterations,
                        salt=loaded.salt, hashed=loaded.hashed)

        self.assertEquals(dumped, dumped2)

    def test_extraction(self):
        from passwordlib.util import (
            dumps,
            extract_algorythm, extract_iterations, extract_salt, extract_hashed,
            get_algorithm, get_iterations, get_salt,
        )
        algorithm = get_algorithm()
        iterations = get_iterations()
        salt = get_salt()
        hashed = b'hashed'

        dumped = dumps(algorithm=algorithm, iterations=iterations, salt=salt, hashed=hashed)

        self.assertEquals(algorithm, extract_algorythm(dumped))
        self.assertEquals(iterations, extract_iterations(dumped))
        self.assertEquals(salt, extract_salt(dumped))
        self.assertEquals(hashed, extract_hashed(dumped))


if __name__ == '__main__':
    unittest.main()
