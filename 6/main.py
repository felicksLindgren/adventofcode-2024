grid = {i+j*1j: column for i, row in enumerate(open('input.txt')) for j, column in enumerate(row.strip())}
start = min(position for position in grid if grid[position] == '^')

def walk(grid=grid):
    position, direction, visited = start, -1, set()
    while position in grid and (position,direction) not in visited:
        visited |= {(position,direction)}
        next_char = grid.get(position+direction)

        if next_char == "#":
            direction *= -1j
        else: position += direction
        
    return {position for position,_ in visited}, (position,direction) in visited

def part_1():
    visited, _ = walk()
    return len(visited)

def part_2():
    visited, _ = walk()
    sum = 0

    for position in visited:
        _, loop_detected = walk(grid | {position: "#"})

        if loop_detected:
            sum += 1

    return sum

if __name__ == "__main__":
    print(part_1())
    print(part_2())


