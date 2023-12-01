import re

source_path = "resources/1.txt"
total_1 = 0
with open(source_path) as f:
    for line in f.readlines():
        numbers = re.findall("\d", line)
        first, last = numbers[0], numbers[-1]
        this_total = first + last
        total_1 += int(this_total)
print(f"Total 1: {total_1}")

digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
          "nine": "9"}
total_2 = 0
with open(source_path) as f:
    for line in f.readlines():
        numbers = re.findall(fr"(?=(\d|{f'|'.join(digits.keys())}))", line)
        first, last = numbers[0], numbers[-1]
        this_total = digits.get(first, first) + digits.get(last, last)
        total_2 += int(this_total)
print(f"Total 2: {total_2}")
