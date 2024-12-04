input = open("input.txt", "r").read()
lines = input.split("\n")

def part_1():
    found_instances_of_XMAS = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]

            if char != "X":
                continue

            # Vertical check forwards
            # Check if there's a M to the right of the X
            if j + 2 < len(lines[i]) and lines[i][j + 1] == "M":
                # M to the right of X
                # Check if there's a S to the right of the M
                if lines[i][j + 2] == "A" and j + 3 < len(lines[i]):
                    # S to the right of M
                    # Check if there's a X to the right of the S
                    if lines[i][j + 3] == "S":
                        # X to the right of S
                        found_instances_of_XMAS += 1

            # Vertical check backwards
            # Check if there's a M to the left of the X
            if lines[i][j - 1] == "M" and j - 2 >= 0:
                # M to the left of X
                # Check if there's a S to the left of the M
                if lines[i][j - 2] == "A" and j - 3 >= 0:
                    # S to the left of M
                    # Check if there's a X to the left of the S
                    if lines[i][j - 3] == "S":
                        # X to the left of S
                        found_instances_of_XMAS += 1

            # Horizontal check forwards
            # Check if there's a M below the X
            if i + 2 < len(lines) and lines[i + 1][j] == "M":
                # M below X
                # Check if there's a S below the M
                if lines[i + 2][j] == "A" and i + 3 < len(lines):
                    # S below M
                    # Check if there's a X below the S
                    if lines[i + 3][j] == "S":
                        # X below S
                        found_instances_of_XMAS += 1

            # Horizontal check backwards
            # Check if there's a M above the X
            if lines[i - 1][j] == "M" and i - 2 >= 0:
                # M above X
                # Check if there's a S above the M
                if lines[i - 2][j] == "A" and i - 3 >= 0:
                    # S above M
                    # Check if there's a X above the S
                    if lines[i - 3][j] == "S":
                        # X above S
                        found_instances_of_XMAS += 1

            # Diagonal check forwards (down-right)
            # Check if there's a M below and to the right of the X
            if i + 2 < len(lines) and j + 2 < len(lines[i]) and lines[i + 1][j + 1] == "M":
                # M below and to the right of X
                # Check if there's a S below and to the right of the M
                if lines[i + 2][j + 2] == "A" and i + 3 < len(lines) and j + 3 < len(lines[i]):
                    # S below and to the right of M
                    # Check if there's a X below and to the right of the S
                    if lines[i + 3][j + 3] == "S":
                        # X below and to the right of S
                        found_instances_of_XMAS += 1

            # Diagonal check forwards (up-right)
            # Check if there's a M above and to the right of the X
            if i - 2 >= 0 and j + 2 < len(lines[i]) and lines[i - 1][j + 1] == "M":
                # M above and to the right of X
                # Check if there's a S above and to the right of the M
                if lines[i - 2][j + 2] == "A" and i - 3 >= 0 and j + 3 < len(lines[i]):
                    # S above and to the right of M
                    # Check if there's a X above and to the right of the S
                    if lines[i - 3][j + 3] == "S":
                        # X above and to the right of S
                        found_instances_of_XMAS += 1
            
            # Diagonal check backwards (down-left)
            # Check if there's a M below and to the left of the X
            if i + 2 < len(lines) and j - 2 >= 0 and lines[i + 1][j - 1] == "M":
                # M below and to the left of X
                # Check if there's a S below and to the left of the M
                if lines[i + 2][j - 2] == "A" and i + 3 < len(lines) and j - 3 >= 0:
                    # S below and to the left of M
                    # Check if there's a X below and to the left of the S
                    if lines[i + 3][j - 3] == "S":
                        # X below and to the left of S
                        found_instances_of_XMAS += 1

            # Diagonal check backwards (up-left)
            # Check if there's a M above and to the left of the X
            if lines[i - 1][j - 1] == "M" and i - 2 >= 0 and j - 2 >= 0:
                # M above and to the left of X
                # Check if there's a S above and to the left of the M
                if lines[i - 2][j - 2] == "A" and i - 3 >= 0 and j - 3 >= 0:
                    # S above and to the left of M
                    # Check if there's a X above and to the left of the S
                    if lines[i - 3][j - 3] == "S":
                        # X above and to the left of S
                        found_instances_of_XMAS += 1

    return found_instances_of_XMAS

def part_2():
    found_instances_of_XMAS = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]

            if char != "A":
                continue

            if i - 1 < 0 or i + 1 >= len(lines) or j - 1 < 0 or j + 1 >= len(lines[i]):
                continue
            
            # Check for 'S' north-east
            if lines[i - 1][j + 1] == "S":
                # Check for 'M' south-west
                if lines[i + 1][j - 1] == "M":
                    # Check for 'M' north-west
                    if lines[i - 1][j - 1] == "M":
                        # Check for 'S' south-east
                        if lines[i + 1][j + 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'S' north-west
                    if lines[i - 1][j - 1] == "S":
                        # Check for 'M' south-east
                        if lines[i + 1][j + 1] == "M":
                            found_instances_of_XMAS += 1
                            continue

            # Check for 'M' north-east
            if lines[i - 1][j + 1] == "M":
                # Check for 'S' south-west
                if lines[i + 1][j - 1] == "S":
                    # Check for 'S' north-west
                    if lines[i - 1][j - 1] == "S":
                        # Check for 'M' south-east
                        if lines[i + 1][j + 1] == "M":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'M' north-west
                    if lines[i - 1][j - 1] == "M":
                        # Check for 'S' south-east
                        if lines[i + 1][j + 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
            
            # Check for 'S' south-east
            if lines[i + 1][j + 1] == "S":
                # Check for 'M' north-west
                if lines[i - 1][j - 1] == "M":
                    # Check for 'M' south-west
                    if lines[i + 1][j - 1] == "M":
                        # Check for 'S' north-east
                        if lines[i - 1][j + 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'S' south-west
                    if lines[i + 1][j - 1] == "S":
                        # Check for 'M' north-east
                        if lines[i - 1][j + 1] == "M":
                            found_instances_of_XMAS += 1
                            continue

            # Check for 'M' south-east
            if lines[i + 1][j + 1] == "M":
                # Check for 'S' north-west
                if lines[i - 1][j - 1] == "S":
                    # Check for 'S' south-west
                    if lines[i + 1][j - 1] == "S":
                        # Check for 'M' north-east
                        if lines[i - 1][j + 1] == "M":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'M' south-west
                    if lines[i + 1][j - 1] == "M":
                        # Check for 'S' north-east
                        if lines[i - 1][j + 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
            
            # Check for 'S' south-west
            if lines[i + 1][j - 1] == "S":
                # Check for 'M' north-east
                if lines[i - 1][j + 1] == "M":
                    # Check for 'M' south-east
                    if lines[i + 1][j + 1] == "M":
                        # Check for 'S' north-west
                        if lines[i - 1][j - 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'S' south-east
                    if lines[i + 1][j + 1] == "S":
                        # Check for 'M' north-west
                        if lines[i - 1][j - 1] == "M":
                            found_instances_of_XMAS += 1
                            continue
            
            # Check for 'M' south-west
            if lines[i + 1][j - 1] == "M":
                # Check for 'S' north-east
                if lines[i - 1][j + 1] == "S":
                    # Check for 'S' south-east
                    if lines[i + 1][j + 1] == "S":
                        # Check for 'M' north-west
                        if lines[i - 1][j - 1] == "M":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'M' south-east
                    if lines[i + 1][j + 1] == "M":
                        # Check for 'S' north-west
                        if lines[i - 1][j - 1] == "S":
                            found_instances_of_XMAS += 1
                            continue

            # Check for 'S' north-west
            if lines[i - 1][j - 1] == "S":
                # Check for 'M' south-east
                if lines[i + 1][j + 1] == "M":
                    # Check for 'M' north-east
                    if lines[i - 1][j + 1] == "M":
                        # Check for 'S' south-west
                        if lines[i + 1][j - 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'S' north-east
                    if lines[i - 1][j + 1] == "S":
                        # Check for 'M' south-west
                        if lines[i + 1][j - 1] == "M":
                            found_instances_of_XMAS += 1
                            continue

            # Check for 'M' north-west
            if lines[i - 1][j - 1] == "M":
                # Check for 'S' south-east
                if lines[i + 1][j + 1] == "S":
                    # Check for 'S' north-east
                    if lines[i - 1][j + 1] == "S":
                        # Check for 'M' south-west
                        if lines[i + 1][j - 1] == "M":
                            found_instances_of_XMAS += 1
                            continue
                    
                    # Check for 'M' north-east
                    if lines[i - 1][j + 1] == "M":
                        # Check for 'S' south-west
                        if lines[i + 1][j - 1] == "S":
                            found_instances_of_XMAS += 1
                            continue
            
    return found_instances_of_XMAS

if __name__ == "__main__":
    print(part_1())
    print(part_2())