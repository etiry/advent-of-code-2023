from collections import defaultdict

with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  parsed_input = list()
  for line in input:
    card_numbers = [int(n) for n in line[10:40].split(' ') if n != '']
    my_numbers = [int(n) for n in line[42:].split(' ') if n != '']

    parsed_input.append({
      'card_numbers': card_numbers,
      'my_numbers': my_numbers
    })

  return parsed_input

def find_matches(line):
  matches = 0
  for num in line['my_numbers']:
    if num in line['card_numbers']:
      matches += 1

  return matches

def calculate_points(data):
  total_points = 0
  N = defaultdict(int)

  for index, line in enumerate(data):
    N[index] += 1
    matches = len(set(line['card_numbers']) & set(line['my_numbers']))
    if matches > 0:
      total_points += 2 ** (matches - 1)
    for j in range(matches):
      N[index + 1 + j] += N[index]

  return total_points, sum(N.values())



print(calculate_points(parse_input(input)))




