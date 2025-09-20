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


with open(file=file, encoding="utf-8") as f:
    grid = [line.rstrip("\n") for line in f.readlines()]

    # row, col
    starting_pos: tuple[int, int] = (-1, -1)

    for i, v in enumerate(grid):
        try:
            starting_pos = i, v.index("^")
        except ValueError:
            continue

    def sim(pos: tuple[int, int], obs_r: int, obs_c: int) -> bool:
        move_count = 1
        direction = Direction.UP
        copy_grid = grid.copy()
        nr, nc = len(copy_grid), len(copy_grid[0])

        copy_grid[obs_r] = (
            copy_grid[obs_r][:obs_c] + "#" + copy_grid[obs_r][obs_c + 1 :]
        )

        thres = nr * nc // 2

        while move_count <= thres:
            row, col = pos
            dr, dc = move_direction[direction]

            # funny ass python negative indexing
            if row + dr < 0 or col + dc < 0:
                break

            try:
                copy_grid[row + dr][col + dc]
            except IndexError:
                break

            if copy_grid[row + dr][col + dc] != "#":
                pos = row + dr, col + dc
                move_count += 1
            else:
                direction = turn_right_direction[direction]
                continue

        if move_count > thres:
            return True

        return False

    loop_count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                continue

            result = sim(starting_pos, r, c)

            if result:
                loop_count += 1

    print(loop_count)
