with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  parsed_input = dict()
  for index, line in enumerate(input):
    card_numbers = [int(n) for n in line[10:40].split(' ') if n != '']
    my_numbers = [int(n) for n in line[42:].split(' ') if n != '']

    parsed_input[index] = {
      'card_numbers': card_numbers,
      'my_numbers': my_numbers
    }

  return parsed_input

def calculate_points(data):
  total_points = 0

  for line in data.keys():
    line_points = 0
    match = False
    for num in data[line]['my_numbers']:
      if num in data[line]['card_numbers']:
        if not match:
          line_points = 1
          match = True
        else:
          line_points *= 2
    print(line_points)
    total_points += line_points

  return total_points
    

print(calculate_points(parse_input(input)))