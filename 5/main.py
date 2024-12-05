input = open("input.txt", "r").read()
sections = input.split("\n\n")

page_ordering_rules = sections[0].split("\n")
pages_to_be_produced = sections[1].split("\n")

def part_1():
    rules = {}
    sum = 0

    for rule in page_ordering_rules:
        pages = rule.split("|")
        if pages[1] not in rules:
            rules[pages[1]] = [pages[0]]
        else:
            rules[pages[1]].append(pages[0])

    for update in pages_to_be_produced:
        pages = update.split(",")
        valid = True

        for i in range(len(pages)):
            page = pages[i]
            rules_for_page = [rule for rule in rules.get(page, []) if rule in pages]
            preceding_pages = pages[:i]

            if len(rules_for_page) == 0:
                continue

            for rule in rules_for_page:
                if rule not in preceding_pages:
                    valid = False
                    break

        if valid:
            middle_page = pages[len(pages) // 2]
            sum += int(middle_page)

    return sum

def part_2():
    rules = {}
    incorrectly_ordered_updates = []

    for rule in page_ordering_rules:
        pages = rule.split("|")
        if pages[1] not in rules:
            rules[pages[1]] = [pages[0]]
        else:
            rules[pages[1]].append(pages[0])

    for update in pages_to_be_produced:
        pages = update.split(",")
        valid = True

        for i in range(len(pages)):
            page = pages[i]
            rules_for_page = [rule for rule in rules.get(page, []) if rule in pages]
            preceding_pages = pages[:i]

            if len(rules_for_page) == 0:
                continue

            for rule in rules_for_page:
                if rule not in preceding_pages:
                    valid = False
                    break
            
            if not valid:
                incorrectly_ordered_updates.append(update)
                break

    sum = 0
    for update in incorrectly_ordered_updates:
        pages = update.split(",")
        # Sort the pages by the length of rules
        sorted_pages = sorted(pages, key=lambda page: len([rule for rule in rules.get(page, []) if rule in pages]))

        middle_page = sorted_pages[len(sorted_pages) // 2]
        sum += int(middle_page)
        

    return sum


if __name__ == "__main__":
    print(part_1())
    print(part_2())