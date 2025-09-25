import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "11" / "input.txt"

# Code below this line.

from collections import defaultdict

with open(file=input_file, encoding="utf-8") as f:
    stones = {x: 1 for x in list(map(int, f.readline().split()))}

    for _ in range(25):
        change: defaultdict[int, int] = defaultdict(int)

        # guess the array is useless?
        # if I do a particular thing, say, a stone 11 then I will do the same for every [count] of 11's I see.
        for stone, count in stones.items():
            if stone == 0:
                change[1] += count
                continue

            st = str(stone)
            sz = len(st)

            if sz % 2 == 0:
                a = int(st[: sz // 2])
                b = int(st[sz // 2 :])
                change[int(a)] += count
                change[int(b)] += count
            else:
                change[stone * 2024] += count

        stones = change

    print(sum(stones.values()))
