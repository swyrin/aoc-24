import collections
import pathlib

cwd = pathlib.Path()
file = cwd.cwd() / "01" / "input.txt"

with open(file, encoding="utf-8") as f:
    L_heap, R_heap = [], []

    while line := f.readline():
        A, B = map(int, line.split())
        L_heap.append(A)
        R_heap.append(B)

    cr = collections.Counter(R_heap)

    total_similarity = 0

    for x in L_heap:
        cnt = cr[x]
        total_similarity += x * cnt

    print(total_similarity)
