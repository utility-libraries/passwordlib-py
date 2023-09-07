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
from passwordlib.analyzer import Analyzer


# may not seem safe at first, but think:
# 9 digits,lowercase and symbols, not commonly used and no repeating characters
result = Analyzer("my_secret")
print(result.is_secure)  # True
print(result.is_highly_secure)  # False
print(result.score)  # 5

print(result.contains_lowercase)  # True
print(result.contains_uppercase)  # False
print(result.contains_digits)  # False
print(result.contains_symbols)  # True
print(result.length)  # 9
print(result.max_consecutive_character)  # 1
print(result.is_commonly_used)  # False

r = Analyzer("password")
print(r.score, r.is_secure, r.is_highly_secure)
# 0 False False
r = Analyzer("123456")
print(r.score, r.is_secure, r.is_highly_secure)
# 0 False False
r = Analyzer("matrix")
print(r.score, r.is_secure, r.is_highly_secure)
# 0 False False
r = Analyzer("password-library")
print(r.score, r.is_secure, r.is_highly_secure)
# 7 True False
r = Analyzer("TifnedjothUj")
print(r.score, r.is_secure, r.is_highly_secure)
# 6 True False
r = Analyzer("passwoooooooooooooord")
print(r.score, r.is_secure, r.is_highly_secure)
# 1 False False
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
  - [X] passwordlib.Analyzer
    - [X] class Analyzer
  - [ ] passwordlib.validator
    - [ ] class PasswordValidator 
    - [ ] passwordlib.validator.rules
- [ ] Documentation
