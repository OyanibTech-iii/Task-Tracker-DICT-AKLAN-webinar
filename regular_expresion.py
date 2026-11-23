import re

 

def looks_like_email(value):

    """Basic format check only; not full verification."""

    value = value.strip()

    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

    return bool(re.match(pattern, value))

 

print(looks_like_email("ana@example.com"))  # True

print(looks_like_email("not-an-email"))     # False