import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "09" / "input.txt"

# Code below this line.

import enum


class ObjectType(enum.Enum):
    FILE = 0
    SPACE = 1


with open(file=input_file, encoding="utf-8") as f:
    FILE_EMPTY: int = -1
    file_type = ObjectType.FILE

    file_name: int = 0
    files: list[int] = []

    for char in f.read().rstrip("\n"):
        if file_type == ObjectType.FILE:
            files += [file_name] * int(char)
            file_name += 1
            file_type = ObjectType.SPACE
        elif file_type == ObjectType.SPACE:
            files += [FILE_EMPTY] * int(char)
            file_type = ObjectType.FILE

    head = 0
    tail = len(files) - 1

    while True:
        while files[head] != FILE_EMPTY:
            head += 1
        while files[tail] == FILE_EMPTY:
            tail -= 1

        if tail < head:
            break

        files[head] = files[tail]
        files[tail] = FILE_EMPTY

    result = 0

    for i, v in enumerate(files):
        if v == FILE_EMPTY:
            continue

        val = int(v)
        result += val * i

    print(result)
