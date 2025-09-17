import re
import pathlib

pattern = re.compile(r"mul\((\d+),(\d+)\)")

cwd = pathlib.Path()
file = cwd.cwd() / "03" / "input.txt"

with open(file, encoding="utf-8") as f:
    text = f.read()
    matches = re.findall(pattern, text)

    if matches is None:
        print("We are cooked")

    total = 0

    for match in matches:
        x, y = match
        x, y = int(x), int(y)
        total += x * y

    print(total)
