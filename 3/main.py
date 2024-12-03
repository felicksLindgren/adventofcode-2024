import re

input = open("input.txt", "r").read()

def part_1():
    sum_of_muliplied_digits = 0
    instructions = re.findall(r"mul[(][0-9]+[,][0-9]+[)]", input)

    for instruction in instructions:
        sections = instruction.split(",")
        first_digits = sections[0].split("(")[1]
        second_digits = sections[1].split(")")[0]

        sum_of_muliplied_digits += int(first_digits) * int(second_digits)

    return sum_of_muliplied_digits

def part_2():
    # exclude sections that starts with don't() and end with do() or EOF
    exclude_pattern = r"[d][o][n]['][t][(][)][\s\S]+?([d][o][(][)]|$(?![\r\n]))"
    instructions = re.sub(exclude_pattern, "", input)
    instructions = re.findall(r"mul[(][0-9]+[,][0-9]+[)]", instructions)

    sum_of_muliplied_digits = 0

    for instruction in instructions:
        sections = instruction.split(",")
        first_digits = sections[0].split("(")[1]
        second_digits = sections[1].split(")")[0]

        sum_of_muliplied_digits += int(first_digits) * int(second_digits)

    return sum_of_muliplied_digits

if __name__ == "__main__":
    print(part_1())
    print(part_2())