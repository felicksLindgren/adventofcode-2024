input = open('input.txt').read()
rows = input.splitlines()

grid = {}
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        grid[(y + x * 1j)] = cell

def part_1():
    antennas = {k for k, v in grid.items() if v != "."}

    frequency_dictionary = {}

    for position in antennas:
        frequency = grid[position]

        if frequency not in frequency_dictionary:
            frequency_dictionary[frequency] = [position]
        else:
            frequency_dictionary[frequency].append(position)

    antinodes = set()
    for frequency, positions in frequency_dictionary.items():
        for i, position in enumerate(positions):
            next_positions = positions[i + 1:]

            for i in range(len(next_positions)):
                next_position = next_positions[i]
                first_antinode = next_position + (next_position - position)
                second_antinode = position + (position - next_position)

                antinodes |= {first_antinode, second_antinode}
            
    antinodes = {k for k in antinodes if k in grid}
    return len(antinodes)

def part_2():
    antennas = {k for k, v in grid.items() if v != "."}
    frequency_dictionary = {}

    for position in antennas:
        frequency = grid[position]

        if frequency not in frequency_dictionary:
            frequency_dictionary[frequency] = [position]
        else:
            frequency_dictionary[frequency].append(position)

    antinodes = set()
    for frequency, positions in frequency_dictionary.items():
        for i, position in enumerate(positions):
            next_positions = positions[i + 1:]

            for i in range(len(next_positions)):
                next_position = next_positions[i]

                found_antinodes = set()

                for i in range(0, len(rows)):
                    found_antinodes |= {next_position + (next_position - position) * i}
                    found_antinodes |= {position + (position - next_position) * i}

                antinodes |= found_antinodes
            
    antinodes = {k for k in antinodes if k in grid}
    return len(antinodes)

if __name__ == "__main__":
    print(part_1())
    print(part_2())


