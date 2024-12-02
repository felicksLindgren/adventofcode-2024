input = open("input.txt", "r").read()
lines = [line.split(" ") for line in input.split("\n")]
reports = [[int(y) for y in x] for x in lines]

def is_report_safe(report):
    # Get the unique differences between the levels in the report
    diff_subset = set([report[i + 1] - report[i] for i in range(len(report) - 1)])

    # Check if diff_subset is a subset of the set of safe differences
    return diff_subset <= {1, 2, 3} or diff_subset <= {-1, -2, -3}

def part_1():
    amount_of_safe_reports = 0

    for report in reports:
        if is_report_safe(report):
            amount_of_safe_reports += 1

    return amount_of_safe_reports

def part_2():
    amount_of_safe_reports = 0

    for report in reports:
        for i in range(len(report)):
            if is_report_safe(report[:i] + report[i + 1:]):
                amount_of_safe_reports += 1
                break

    return amount_of_safe_reports

if __name__ == "__main__":
    print(part_1())
    print(part_2())