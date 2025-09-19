import pathlib
import graphlib

cwd = pathlib.Path()
file = cwd.cwd() / "05" / "input.txt"

rules: list[list[int]] = []


def filter_rules(arr: list[int]) -> list[list[int]]:
    return [[x, y] for [x, y] in rules if x in arr and y in arr]


def create_graph_arr(rules: list[list[int]]) -> list[int]:
    topo: graphlib.TopologicalSorter[int] = graphlib.TopologicalSorter()

    for rule in rules:
        a, b = rule
        topo.add(b, a)

    return [*topo.static_order()]


with open(file=file, encoding="utf-8") as f:
    result = 0

    while line := f.readline():
        if line == "\n":
            break

        a, b = map(int, line.split("|"))
        rules.append([a, b])

    while line := f.readline():
        arr = list(map(int, line.split(",")))

        # shit's not DAG so... yeah, spaghetti coming :D
        filtered_rules = filter_rules(arr)
        order = [*create_graph_arr(filtered_rules)]
        indices = list(map(order.index, arr))

        if indices == list(sorted(indices)):
            result += arr[len(arr) // 2]

    print(result)
