import regex as re

with open('input.txt') as file:
  input = file.read().splitlines()

digits = []

def replace_text_digits(digit_list):
  text_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }

  for i in range(len(digit_list)):
    for key, value in text_digits.items():
      if digit_list[i] == key:
        digit_list[i] = value

  return digit_list

def find_digits(string):
  return re.findall("\d|one|two|three|four|five|six|seven|eight|nine", string, overlapped=True)

def find_sum(input):
  for line in input:
    int_digits = replace_text_digits(find_digits(line))
    first_and_last = int_digits[0] + int_digits[-1]
    digits.append(int(first_and_last))

  return sum(digits)

print(find_sum(input))