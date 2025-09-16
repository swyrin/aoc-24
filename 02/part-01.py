import pathlib

cwd = pathlib.Path()
file = cwd.cwd() / "02" / "input.txt"


def is_monotone(x: list[int]) -> bool:
    # yes, bad code.
    sort = sorted(x)
    return x == sort or x == list(reversed(sort))


with open(file, encoding="utf-8") as f:
    safe = 0

    while line := f.readline():
        x: list[int] = list(map(int, line.split()))

        if not is_monotone(x):
            continue

        n = len(x)
        satisfy = True

        for u in range(n - 1):
            a = x[u]
            b = x[u + 1]

            if not 1 <= abs(a - b) <= 3:
                satisfy = False
                break

        safe += satisfy

    print(safe)
