# passwordlib-py
utility library to verify, hash, compare and more for passwords

> Currently, this project is in the earliest stages of development.
> But below is what it should be

passwordlib should offer an easy interface to create password-hashes
```python
from passwordlib import util as pwutil

hashed = pwutil.password_hash("my_secret")

print(pwutil.compare_password("your_secret", hashed))  # False
print(pwutil.compare_password("my_secret", hashed))  # True
```
it should also offer
```python
from passwordlib.attr import PasswordAttribute


class User:
    name: str
    password: PasswordAttribute = PasswordAttribute()


user = User()
print(user.password)  # None
user.password = "secret"
print(user.password)  # Password(algorithm='sha256', iterations=100_000)
print(user.password.bytes)  # b'\x06sha256\x00\x01\x86\xa0\x00 \x07\xcfg\x0ec\xa6D\xea\xae\x03S\xa1\xfcz\xaew\x02\x8b\xf1\xe5\xaf\x83n&\x87'\xcdRi!\xd9\xe7\x00@qV\xd3\x81\x113:*"\x05\xba\x12Xb\x04\xeb\x08Sn\x08Z\x9f\x89\xa50~\xa0\xb4\xbd.\xc6\x18"\xf9l\xeds\xbc\xc2B\xa7\xef\xa1\x8a\x7f3\xc1u\x17d\xce\xf2\x98+l\x86\xb7\x1c\xb4\xf0\x07t8\xc9'
print(user.password.algorithm)  # sha256
print(user.password.iterations)  # 100000
print(user.password.salt)  # b"\x07\xcfg\x0ec\xa6D\xea\xae\x03S\xa1\xfcz\xaew\x02\x8b\xf1\xe5\xaf\x83n&\x87'\xcdRi!\xd9\xe7"
print(user.password.hash)  # b'qV\xd3\x81\x113:*"\x05\xba\x12Xb\x04\xeb\x08Sn\x08Z\x9f\x89\xa50~\xa0\xb4\xbd.\xc6\x18"\xf9l\xeds\xbc\xc2B\xa7\xef\xa1\x8a\x7f3\xc1u\x17d\xce\xf2\x98+l\x86\xb7\x1c\xb4\xf0\x07t8\xc9'
```
```python
from passwordlib.validator import PasswordValidator, rules

validator = PasswordValidator("my_secret")
print(validator.is_secure)  # False
print(validator.score)  # 4

print(validator.contains_lowercase)  # True
print(validator.contains_uppercase)  # False
print(validator.contains_numbers)  # False
print(validator.contains_symbols)  # False
print(validator.length)  # 9
print(validator.too_short)  # False
print(validator.max_consecutive)  # 1
print(validator.is_common)  # False
```
