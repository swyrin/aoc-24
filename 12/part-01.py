import pathlib

cwd = pathlib.Path()
input_file = cwd.cwd() / "12" / "input.txt"

# Code below this line.

with open(file=input_file, encoding="utf-8") as f:
    garden = [line.strip("\n") for line in f.readlines()]
    rows = len(garden)
    cols = len(garden[0])
    visited = [[False] * cols for _ in range(rows)]

    def get_region_tiles(r: int, c: int, ch: str) -> list[tuple[int, int]]:
        path: list[tuple[int, int]] = []

        def span(_r: int, _c: int, _ch: str):
            if not (0 <= _r < rows and 0 <= _c < cols):
                return

            if visited[_r][_c]:
                return

            if garden[_r][_c] != _ch:
                return

            visited[_r][_c] = True
            path.append((_r, _c))

            span(_r + 1, _c, _ch)
            span(_r - 1, _c, _ch)
            span(_r, _c + 1, _ch)
            span(_r, _c - 1, _ch)

        span(r, c, ch)
        return path

    total = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                result = get_region_tiles(row, col, garden[row][col])
                area = len(result)
                perimeters = 0
                for tile in result:
                    r, c = tile
                    adj = [
                        (r + 1, c),
                        (r - 1, c),
                        (r, c + 1),
                        (r, c - 1),
                    ]
                    conflicts = len(
                        [
                            verdict
                            for verdict in [check in result for check in adj]
                            if verdict
                        ]
                    )
                    perimeters += 4 - conflicts
                total += area * perimeters

    print(total)
