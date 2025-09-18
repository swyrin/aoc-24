import pathlib

cwd = pathlib.Path()
file = cwd.cwd() / "04" / "input.txt"

with open(file, encoding="utf-8") as f:
    text = f.read()
    lines = text.split("\n")
    rows = len(lines)
    cols = len(lines[0])

    def try_get(h: int, v: int) -> str:
        # negative index exists in python, smh my head
        if h < 0 or v < 0:
            return "0"

        try:
            return lines[h][v]
        except IndexError:
            return "0"

    def is_xmas(ch1: str, ch2: str, ch3: str, ch4: str) -> bool:
        cat = ch1 + ch2 + ch3 + ch4
        return cat == "XMAS" or cat == "SAMX"

    count = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "X":
                # right
                right_check = is_xmas(
                    try_get(r, c),
                    try_get(r, c + 1),
                    try_get(r, c + 2),
                    try_get(r, c + 3),
                )

                if right_check:
                    print("XMAS found right at", r, c)

                # down-right
                down_right_check = is_xmas(
                    try_get(r, c),
                    try_get(r + 1, c + 1),
                    try_get(r + 2, c + 2),
                    try_get(r + 3, c + 3),
                )

                if down_right_check:
                    print("XMAS found down-right at", r, c)

                # down
                down_check = is_xmas(
                    try_get(r, c),
                    try_get(r + 1, c),
                    try_get(r + 2, c),
                    try_get(r + 3, c),
                )

                if down_check:
                    print("XMAS found down at", r, c)

                # down-left
                down_left_check = is_xmas(
                    try_get(r, c),
                    try_get(r + 1, c - 1),
                    try_get(r + 2, c - 2),
                    try_get(r + 3, c - 3),
                )

                if down_left_check:
                    print("XMAS found down-left at", r, c)

                # left
                left_check = is_xmas(
                    try_get(r, c),
                    try_get(r, c - 1),
                    try_get(r, c - 2),
                    try_get(r, c - 3),
                )

                if left_check:
                    print("XMAS found left at", r, c)

                # up-left
                up_left_check = is_xmas(
                    try_get(r, c),
                    try_get(r - 1, c - 1),
                    try_get(r - 2, c - 2),
                    try_get(r - 3, c - 3),
                )

                if up_left_check:
                    print("XMAS found up-left at", r, c)

                # up
                up_check = is_xmas(
                    try_get(r, c),
                    try_get(r - 1, c),
                    try_get(r - 2, c),
                    try_get(r - 3, c),
                )

                if up_check:
                    print("XMAS found up at", r, c)

                # up-right
                up_right_check = is_xmas(
                    try_get(r, c),
                    try_get(r - 1, c + 1),
                    try_get(r - 2, c + 2),
                    try_get(r - 3, c + 3),
                )

                if up_right_check:
                    print("XMAS found up-right at", r, c)

                count += (
                    up_check
                    + up_right_check
                    + up_left_check
                    + left_check
                    + right_check
                    + down_check
                    + down_left_check
                    + down_right_check
                )

    print(count)
