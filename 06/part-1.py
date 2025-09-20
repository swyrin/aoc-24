import pathlib
import enum

cwd = pathlib.Path()
file = cwd.cwd() / "06" / "input.txt"


class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


move_direction: dict[Direction, tuple[int, int]] = {
    Direction.UP: (-1, 0),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
    Direction.RIGHT: (0, 1),
}

turn_right_direction: dict[Direction, Direction] = {
    Direction.UP: Direction.RIGHT,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
    Direction.RIGHT: Direction.DOWN,
}

visited: list[tuple[int, int]] = []


with open(file=file, encoding="utf-8") as f:
    grid = [line.rstrip("\n") for line in f.readlines()]

    # row, col
    pos: tuple[int, int] = (-1, -1)

    for i, v in enumerate(grid):
        try:
            pos = i, v.index("^")
        except ValueError:
            continue

    # "Including the guard's starting position"
    visited.append(pos)
    direction = Direction.UP

    # def is_inside(grid: list[str], current_pos: tuple[int, int]):
    #     r, c = current_pos
    #     nr, nc = len(grid), len(grid[0])
    #     return 0 <= r < nr and 0 <= c < nc

    while True:
        row, col = pos
        dr, dc = move_direction[direction]

        # funny ass python negative indexing
        if row + dr < 0 or col + dc < 0:
            break

        try:
            grid[row + dr][col + dc]
        except IndexError:
            break

        if grid[row + dr][col + dc] != "#":
            pos = row + dr, col + dc
            visited.append(pos)
        else:
            direction = turn_right_direction[direction]
            continue

    print(len(set(visited)))
