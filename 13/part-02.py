import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "13" / "input.txt"

# Code below this line.

import re
import numpy as np
from sympy import Matrix

with open(file=input_file, encoding="utf-8") as f:
    i = 0
    btn_A_regex = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
    btn_B_regex = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
    coord_regex = re.compile(r"Prize: X=(\d+), Y=(\d+)")
    dataset: list[list[list[int]]] = []
    x: list[int] = []
    y: list[int] = []

    while line := f.readline():
        line = line.rstrip("\n")

        if line == "":
            bundle: list[list[int]] = []
            bundle.append(x.copy())
            bundle.append(y.copy())
            dataset.append(bundle)
            x.clear()
            y.clear()
            continue

        if i == 0:
            match = btn_A_regex.search(line)
            if match is None:
                raise ValueError("We are cooked.")

            groups = match.groups()
            x1, y1 = map(int, groups)
            x.append(x1)
            y.append(y1)
        elif i == 1:
            match = btn_B_regex.search(line)
            if match is None:
                raise ValueError("We are cooked.")

            groups = match.groups()
            x2, y2 = map(int, groups)
            x.append(x2)
            y.append(y2)
        elif i == 2:
            match = coord_regex.search(line)
            if match is None:
                raise ValueError("We are cooked.")

            groups = match.groups()
            x0, y0 = map(int, groups)
            x.append(x0 + 10000000000000)
            y.append(y0 + 10000000000000)
        else:
            raise ValueError("Huh?")

        i = (i + 1) % 3

    result = 0

    for data in dataset:
        mat: Matrix = Matrix(data)
        rref = mat.rref()[0]
        n_rref = np.array(rref)
        count_A: int = n_rref[0][2]
        count_B: int = n_rref[1][2]

        if not (count_A != int(count_A) or count_B != int(count_B)):
            cost = 3 * count_A + count_B
        else:
            cost = 0

        result += cost

    print(result)
