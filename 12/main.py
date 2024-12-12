input = open("input.txt", "r").readlines()

def bfs(grid, x, y, character, visited):
    stack = [(x, y, '')]
    area, perimeter, side, sides = 0, 0, 0, set()

    while stack:
        x, y, dir = stack.pop()

        # Check if we are out of bounds or if we are not on the same character
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != character:
            # Check if we are on the edge of the character
            if not((x+1, y, dir) in sides or (x-1, y, dir) in sides or (x, y+1, dir) in sides or (x, y-1, dir) in sides):
                side += 1

            # Check if we are on the corner of the character
            if ((x+1, y, dir) in sides and (x-1, y, dir) in sides) or ((x, y+1, dir) in sides and (x, y-1, dir) in sides):
                side -= 1

            sides.add((x, y, dir))
            perimeter += 1
            continue
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        area += 1
        
        stack.append((x + 1, y, 'DOWN'))
        stack.append((x, y - 1, 'LEFT'))
        stack.append((x - 1, y, 'UP'))
        stack.append((x, y + 1, 'RIGHT'))

    return area, perimeter, side

def part_1():
    grid = [list(row.strip()) for row in input]
    visited = set()
    price = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                area, perimeters, _ = bfs(grid, i, j, grid[i][j], visited)
                price += area * perimeters

    return price

def part_2():
    grid = [list(row.strip()) for row in input]
    visited = set()
    price = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                area, _, side = bfs(grid, i, j, grid[i][j], visited)
                price += area * side

    return price

if __name__ == "__main__":
    print(part_1())
    print(part_2())
