import pathlib
import itertools

cwd = pathlib.Path()
file = cwd.cwd() / "07" / "input.txt"


def evaluate(inputs: list[int], ops: list[str]):
    result = inputs[0]

    for i, v in enumerate(ops):
        op = v
        val = inputs[i + 1]

        if op == "+":
            result += val
        elif op == "*":
            result *= val
        elif op == "||":
            result = int(str(result) + str(val))
        else:
            raise ValueError(f"Unknown operator: {op}")

    return result


with open(file=file, encoding="utf-8") as f:
    total = 0

    while line := f.readline():
        line = line.replace(":", "")
        line = line.rstrip("\n")
        numbers = list(map(int, line.split()))

        output = numbers[0]
        inputs = numbers[1:]
        n = len(inputs)

        verdict: list[bool] = []

        for operands in itertools.product(["+", "*", "||"], repeat=n - 1):
            verdict.append(evaluate(inputs, list(operands)) == output)

        if any(verdict):
            total += output

    print(total)
