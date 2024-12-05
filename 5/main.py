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

        for i in range(len(pages)):
            page = pages[i]
            sorted_pages = sorted(pages, key=lambda page: len([rule for rule in rules.get(page, []) if rule in pages]))

            if pages != sorted_pages:
                break
            
            middle_page = pages[len(pages) // 2]
            if page == middle_page:
                sum += int(page)
                break

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

        for _ in range(len(pages)):
            sorted_pages = sorted(pages, key=lambda page: len([rule for rule in rules.get(page, []) if rule in pages]))

            if pages != sorted_pages:
                incorrectly_ordered_updates.append(update)
                break

    sum = 0
    for update in incorrectly_ordered_updates:
        pages = update.split(",")
        sorted_pages = sorted(pages, key=lambda page: len([rule for rule in rules.get(page, []) if rule in pages]))

        middle_page = sorted_pages[len(sorted_pages) // 2]
        sum += int(middle_page)
        
    return sum

if __name__ == "__main__":
    print(part_1())
    print(part_2())