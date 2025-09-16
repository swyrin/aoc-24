import pathlib

cwd = pathlib.Path()
file = cwd.cwd() / "02" / "input.txt"


def is_monotone(x: list[int]) -> bool:
    # yes, bad code.
    sort = sorted(x)
    return x == sort or x == list(reversed(sort))


def is_safe(x: list[int]) -> bool:
    if not is_monotone(x):
        return False

    n = len(x)

    for u in range(n - 1):
        a = x[u]
        b = x[u + 1]

        if not 1 <= abs(a - b) <= 3:
            return False

    return True


with open(file, encoding="utf-8") as f:
    safe = 0

    while line := f.readline():
        x: list[int] = list(map(int, line.split()))
        satisfy = False

        for i in range(len(x)):
            xc: list[int] = x.copy()
            del xc[i]
            if is_safe(xc):
                satisfy = True
                break

        safe += satisfy

    print(safe)
