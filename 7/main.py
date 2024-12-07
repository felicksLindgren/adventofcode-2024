input = open('input.txt').read()
rows = input.splitlines()

def part_1():
    possible_target_values = set() 

    for row in rows:
        target, numbers = row.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))

        n = len(numbers)
        numbers_to_check = [numbers[0]]

        for i in range(1, n + 1):
            if i == n:
                if any([number == target for number in numbers_to_check]):
                    possible_target_values |= {target}
                break

            next_numbers = []
            for number in numbers_to_check:
                next_numbers += [number + numbers[i], number * numbers[i]]

            numbers_to_check = next_numbers

    return sum(possible_target_values)

def part_2():
    possible_target_values = set() 

    for row in rows:
        target, numbers = row.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))

        n = len(numbers)
        numbers_to_check = [numbers[0]]

        for i in range(1, n + 1):
            if i == n:
                if any([number == target for number in numbers_to_check]):
                    possible_target_values |= {target}
                break

            next_numbers = []
            for number in numbers_to_check:
                next_numbers += [number + numbers[i], number * numbers[i], int(str(number) + str(numbers[i]))]

            numbers_to_check = next_numbers

    return sum(possible_target_values)

if __name__ == "__main__":
    print(part_1())
    print(part_2())