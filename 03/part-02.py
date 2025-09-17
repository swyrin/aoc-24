import re
import pathlib

pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))")

cwd = pathlib.Path()
file = cwd.cwd() / "03" / "input.txt"

with open(file, encoding="utf-8") as f:
    text = f.read()
    matches = re.findall(pattern, text)

    if matches is None:
        print("We are cooked")

    total = 0
    should_mul = True

    for match in matches:
        x, y, do, do_not = match

        if do != "":
            should_mul = True

        if do_not != "":
            should_mul = False

        if x != "" and y != "":
            x, y = int(x), int(y)
            total += x * y * should_mul

    print(total)
