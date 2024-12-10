input = open('input.txt').readlines()
grid = [list(row.strip()) for row in input]
grid = {i + j * 1j: int(cell) for i, row in enumerate(grid) for j, cell in enumerate(row)}

def part_1():
    sum_of_trailheads = 0

    for position, cell in grid.items():
        if cell != 0:
            continue

        directions = [(position, 1, 1), (position, 1, -1), (position, 1, 1j), (position, 1, -1j)]
        trailheads = set()

        while directions:
            pos, look_up, dir = directions.pop(0)
            next_position = pos + dir

            if next_position not in grid:
                continue

            next_cell = grid[next_position]

            if next_cell == 9 and look_up == 9:
                trailheads |= {next_position}
                continue

            if next_cell == look_up:
                directions.append((next_position, look_up + 1, 1))
                directions.append((next_position, look_up + 1, -1))
                directions.append((next_position, look_up + 1, 1j))
                directions.append((next_position, look_up + 1, -1j))

        sum_of_trailheads += len(trailheads)

    return sum_of_trailheads

def part_2():
    sum_of_trailheads = 0

    for position, cell in grid.items():
        if cell != 0:
            continue

        directions = [(position, 1, 1), (position, 1, -1), (position, 1, 1j), (position, 1, -1j)]
        score = 0

        while directions:
            pos, look_up, dir = directions.pop(0)
            next_position = pos + dir

            if next_position not in grid:
                continue

            next_cell = grid[next_position]

            if next_cell == 9 and look_up == 9:
                score += 1
                continue

            if next_cell == look_up:
                directions.append((next_position, look_up + 1, 1))
                directions.append((next_position, look_up + 1, -1))
                directions.append((next_position, look_up + 1, 1j))
                directions.append((next_position, look_up + 1, -1j))

        sum_of_trailheads += score

    return sum_of_trailheads

if __name__ == '__main__':
    print(part_1())
    print(part_2())