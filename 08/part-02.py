import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "08" / "input.txt"

# Code below this line.
import itertools

attenas: dict[str, list[tuple[int, int]]] = {}

with open(file=input_file, encoding="utf-8") as f:
    lines = f.readlines()

    rows, cols = len(lines), len(lines[0]) - 1

    for row, line in enumerate(lines):
        line = line.strip("\n")
        for col, char in enumerate(line):
            # for the sake(TM) of convenient copy paste.
            if char != "." and char != "#":
                if char not in attenas:
                    attenas[char] = []
                attenas[char].append((row, col))

    results: list[tuple[int, int]] = []

    for attena in attenas:
        entries = attenas[attena]
        for pair in itertools.combinations(entries, 2):
            this, other = pair
            r1, c1 = this
            r2, c2 = other
            rd = r2 - r1
            cd = c2 - c1
            for t in range(100):
                results.append((r1 - t * rd, c1 - t * cd))
                results.append((r2 + t * rd, c2 + t * cd))

    def is_in_board(entry: tuple[int, int]):
        r, c = entry
        return 0 <= r < rows and 0 <= c < cols

    results = list(filter(is_in_board, results))

    # for i in range(rows):
    #     for j in range(cols):
    #         if (i, j) in results:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print(results)

    print(len(set(results)))
