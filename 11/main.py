from functools import cache

input = open('input.txt').readline().strip().split(" ")
input = list(map(int, input))

@cache
def evolve(stone, blinks):
    # If we have no more blinks, we return 1 because we're only interested in the number of stones
    if blinks == 0:
        return 1

    # First rule
    if stone == 0:
        return evolve(1, blinks - 1)
    
    # Second rule
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return evolve(int(str_stone[:half]), blinks - 1) + evolve(int(str_stone[half:]), blinks - 1)
    
    # Third rule
    return evolve(stone * 2024, blinks - 1)

def part_1():
    amount_of_stones = 0

    for stone in input:
        amount_of_stones += evolve(stone, 25)

    return amount_of_stones

def part_2():
    amount_of_stones = 0

    for stone in input:
        amount_of_stones += evolve(stone, 75)

    return amount_of_stones

if __name__ == "__main__":
    print(part_1())
    print(part_2())

    