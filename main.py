import sys
import pathlib

day = sys.argv[1].rjust(2, "0")

path = pathlib.Path()
dest = path.cwd() / day

content = f"""
import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "{day}" / "input.txt"

# Code below this line.

with open(file=input_file, encoding="utf-8") as f:
    ...
"""


def main():
    input_file = dest / "input.txt"
    part_1_file = dest / "part-01.py"
    part_2_file = dest / "part-02.py"

    dest.mkdir()
    input_file.touch()

    _ = part_1_file.write_text(content)
    _ = part_2_file.write_text(content)


if __name__ == "__main__":
    try:
        main()
        print(f"Day {day} submission created!")
    except:
        print("We are cooked")
