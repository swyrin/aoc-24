import heapq
import pathlib

cwd = pathlib.Path()
file = cwd.cwd() / "01" / "input.txt"

with open(file, encoding="utf-8") as f:
    L_heap: list[int] = []
    R_heap: list[int] = []

    while line := f.readline():
        A, B = map(int, line.split())
        L_heap.append(A)
        R_heap.append(B)

    total_dist = 0

    L_heap = heapq.nsmallest(len(L_heap), L_heap)
    R_heap = heapq.nsmallest(len(R_heap), R_heap)

    for x, y in zip(L_heap, R_heap):
        total_dist += abs(x - y)

    print(total_dist)
