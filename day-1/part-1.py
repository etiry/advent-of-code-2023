with open('input.txt') as file:
  input = file.read().splitlines()

digits = []

def find_digit(str, last = False):
  if last:
    str = reversed(str)

  for char in str:
    if char.isdigit():
      return char

def find_sum(input):
  for line in input:
    line_digits = find_digit(line) + find_digit(line, last = True)

    digits.append(int(line_digits))

  return sum(digits)

print(find_sum(input))