import re

pathi= 'regex_sum_2066152.txt'
file = open(pathi, 'r')

numbers = []

for line in file:
    numbers_in = re.findall("([0-9]+)[^0-9]", line)
    if len(numbers_in) == 0:
        continue
    numbers += numbers_in

value = 0
for number in numbers:
    number_float = int(number)
    value += number_float

print(f"The sum is {value}")


