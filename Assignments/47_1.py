import re
my_string = """Strings are amongst the most popular data types in Python. We can create the strings by enclosing 
characters in quotes. Python treats single quotes the same as double quotes."""

count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('strings'), my_string))
print count
