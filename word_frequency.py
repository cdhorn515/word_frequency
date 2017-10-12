import re

with open("sample.txt") as file:
    lines = file.read()
print(type(lines))
# returns a str
lines = re.sub("[^a-zA-Z\s]", "", lines).lower()
print(lines)
