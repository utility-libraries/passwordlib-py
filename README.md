# passwordlib-py
utility library to verify, hash, compare and more for passwords

## Installation

Just run `pip install password-library`

## Example usage

passwordlib should offer an easy interface to create password-hashes
```python
from passwordlib import util as pwutil

hashed = pwutil.hash_password("my_secret")

print(pwutil.compare_password("your_secret", hashed))  # False
print(pwutil.compare_password("my_secret", hashed))  # True

print(pwutil.extract_algorythm(hashed))  # sha256
print(pwutil.extract_iterations(hashed))  # 100_000
print(pwutil.extract_salt(hashed))  # b'...'
print(pwutil.extract_hashed(hashed))  # b'...'
```
it should also offer
```python
from passwordlib.attr import PasswordAttribute


class User:
    name: str
    password = PasswordAttribute()


user = User()
print(user.password)  # None
user.password = "secret"
print(user.password)  # b'\x06sha256\x00\x01\x86\xa0\x00 \x07\xcfg\x0ec\xa6D\xea\xae\x03S\xa1\xfcz\xaew\x02\x8b\xf1\xe5\xaf\x83n&\x87'\xcdRi!\xd9\xe7\x00@qV\xd3\x81\x113:*"\x05\xba\x12Xb\x04\xeb\x08Sn\x08Z\x9f\x89\xa50~\xa0\xb4\xbd.\xc6\x18"\xf9l\xeds\xbc\xc2B\xa7\xef\xa1\x8a\x7f3\xc1u\x17d\xce\xf2\x98+l\x86\xb7\x1c\xb4\xf0\x07t8\xc9'
```
check if a password is commonly used
```python
from passwordlib.commonly_used import is_commonly_used

print(is_commonly_used("password"))  # True
print(is_commonly_used("123456"))  # True
print(is_commonly_used("matrix"))  # True
print(is_commonly_used("password-library"))  # False
print(is_commonly_used("TifnedjothUj"))  # False
```
and be able to validate a password against different criteria
to ensure a password is safe.
```python
from passwordlib.validator import PasswordValidator

validator = PasswordValidator("my_secret")
print(validator.is_valid)  # False
print(validator.is_secure)  # False
print(validator.score)  # 4

print(validator.contains_lowercase)  # True
print(validator.contains_uppercase)  # False
print(validator.contains_numbers)  # False
print(validator.contains_symbols)  # False
print(validator.length)  # 9
print(validator.too_short)  # False
print(validator.max_consecutive)  # 1
print(validator.is_commonly_used)  # False
```

## Roadmap

- [ ] passwordlib
  - [X] passwordlib.util
    - [X] def hashing
    - [X] def comparing
    - [X] def dumping
    - [X] def loading
  - [X] passwordlib.attr
    - [ ] class PasswordAttribute
  - [ ] passwordlib.commonly_used
    - [ ] def is_common_password
  - [ ] passwordlib.validator
    - [ ] class PasswordValidator 
    - [ ] passwordlib.validator.rules
- [ ] Documentation
