input = open("input.txt", "r").read()
lines = input.split("\n")
lines = [line.split("   ") for line in lines]

def calculate_distance():
    col0 = [line[0] for line in lines]
    col1 = [line[1] for line in lines]

    sorted_col0 = sorted(col0)
    sorted_col1 = sorted(col1)

    sum = 0
    for i in range(len(sorted_col0)):
        sum += abs(int(sorted_col0[i]) - int(sorted_col1[i]))
        
    return sum

def calculate_similarity_score():
    col0 = [line[0] for line in lines]
    col1 = [line[1] for line in lines]

    sum = 0
    for i in range(len(col0)):
        key = col0[i]
        sum_of_key_in_col1 = 0

        for j in range(len(col1)):
            if col1[j] == key:
                sum_of_key_in_col1 += int(col1[j])

        sum += sum_of_key_in_col1

    # print(product)
    return sum


if __name__ == "__main__":
    print(calculate_distance())
    print(calculate_similarity_score())