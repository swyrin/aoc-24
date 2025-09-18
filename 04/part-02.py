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

    def is_mas(ch1: str, ch2: str, ch3: str) -> bool:
        cat = ch1 + ch2 + ch3
        return cat == "MAS" or cat == "SAM"

    count = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "A":
                diagonal = is_mas(
                    try_get(r - 1, c - 1), try_get(r, c), try_get(r + 1, c + 1)
                )

                anti_diagonal = is_mas(
                    try_get(r - 1, c + 1), try_get(r, c), try_get(r + 1, c - 1)
                )

                count += diagonal and anti_diagonal

    print(count)
