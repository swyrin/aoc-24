import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "10" / "input.txt"

# Code below this line.


def floodfill(
    grid: list[str],
    current_row: int,
    current_col: int,
) -> list[str]:
    rows = len(grid)
    cols = len(grid[0])
    results: list[str] = []
    visited: list[list[bool]] = [[False] * cols for _ in range(rows)]

    def _flood(
        _current_row: int,
        _current_col: int,
        _current_path: str,
        _visited: list[list[bool]],
    ):
        if not (0 <= _current_row < rows and 0 <= _current_col < cols):
            return

        if _visited[_current_row][_current_col]:
            return

        # "and always increases by a height of exactly 1 at each step"
        if len(_current_path) > 0:
            last_taken = _current_path[-1]
            next_up = grid[_current_row][_current_col]
            if int(next_up) != int(last_taken) + 1:
                return

        _current_path += grid[_current_row][_current_col]
        _visited[_current_row][_current_col] = True

        if grid[_current_row][_current_col] == "9":
            results.append(_current_path)
            return

        _flood(_current_row, _current_col - 1, _current_path, _visited.copy())
        _flood(_current_row, _current_col + 1, _current_path, _visited.copy())
        _flood(_current_row + 1, _current_col, _current_path, _visited.copy())
        _flood(_current_row - 1, _current_col, _current_path, _visited.copy())

    _flood(current_row, current_col, "", visited)

    return results


with open(file=input_file, encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

    total = 0

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "0":
                outcomes = floodfill(lines, r, c)
                count = len(
                    [outcome for outcome in outcomes if outcome == "0123456789"]
                )
                total += count

    print(total)
