"""
2333133121414131402
"""

from itertools import batched

input = list(map(int, open('input.txt').readline().strip()))

def part_1():
    blocks = []

    index = 0

    for i, char in enumerate(input):
        char = int(char)
        if i % 2 == 0:
            blocks.extend([index] * char)
            index += 1
        else:
            blocks.extend(["."] * char)

    left = 0
    right = len(blocks) - 1

    while left < right:
        while blocks[left] != ".":
            left += 1
        while blocks[right] == ".":
            right -= 1
        while (left < right and blocks[left] == "." and blocks[right] != "."):
            blocks[left], blocks[right] = blocks[right], blocks[left]
            left += 1
            right -= 1

    checksum = 0

    for i, c in enumerate(blocks):
        if c == ".":
            continue
        checksum += i * int(c)

    return checksum

def part_2():
    data_blocks = []
    free_blocks = []

    for i, batch in enumerate(batched(input, 2)):
        data_size, *rest = batch
        empty_size = rest[0] if len(rest) == 1 else 0

        data_blocks.append([i] * data_size)
        free_blocks.append([[], empty_size])

    # Defragment
    candidate_id = len(data_blocks)
    while candidate_id > 1:
        candidate_id -= 1
        candidate_data = data_blocks[candidate_id]
        candidate_len = len(candidate_data)

        # Find a free block with enough space for current candidate
        for i in range(candidate_id):
            # Skip if this free block is too small to hold the candidate data
            if free_blocks[i][1] < candidate_len:
                continue

            # Move candidate data into the free block, and update its size
            free_blocks[i][0].extend(candidate_data)
            free_blocks[i][1] -= candidate_len

            # Null the original data block
            data_blocks[candidate_id] = [None] * candidate_len
            break

    # Calculate checksum
    checksum, position = 0, 0
    for i in range(len(data_blocks)):
        for block in data_blocks[i]:
            checksum += (block or 0) * position
            position += 1
        for block in free_blocks[i][0]:
            checksum += block * position
            position += 1
        position += free_blocks[i][1]

    return checksum

if __name__ == "__main__":
    print(part_1())
    print(part_2())