from functools import cache

input = open('input.txt').readline().strip().split(" ")
input = list(map(int, input))

def apply_rules(stone):
    # First rule
    if stone == 0:
        return [1]
    
    str_stone = str(stone)
    # Second rule
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return [int(str_stone[:half]), int(str_stone[half:])]
    
    # Third rule
    return [stone * 2024]

@cache
def fast_forward(stone, steps):
    new_stones = apply_rules(stone)

    if steps == 1:
        return len(new_stones)
    else:
        total_of_stones = 0

        for new_stone in new_stones:
            total_of_stones += fast_forward(new_stone, steps - 1)

        return total_of_stones


def part_1():
    total_of_stones = 0

    for stone in input:
        total_of_stones += fast_forward(stone, 25)

    return total_of_stones


def part_2():
    total_of_stones = 0

    for stone in input:
        total_of_stones += fast_forward(stone, 75)

    return total_of_stones

if __name__ == "__main__":
    print(part_1())
    print(part_2())