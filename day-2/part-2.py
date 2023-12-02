import re

with open('input.txt') as file:
  input = file.read().splitlines()

def extract_numbers(line):
  colors = ['red', 'blue', 'green']
  numbers = {}

  for color in colors:
    numbers[color] = []
    pattern = re.compile(f'([\d]+)( {color})')
    matches = re.findall(pattern, line)
    for match in matches:
      numbers[color].append(int(match[0]))
    
  return numbers

def reformat_data(input_array):
  data = {}
  for line in input_array:
    pattern = re.compile('^(Game )([\d]+)')
    game_id = int(pattern.search(line).group(2))
    data[game_id] = extract_numbers(line)

  return data

def find_min_cubes(game):
  for key, values in game.items():
    game[key] = max(values)
  
  return game

def calculate_power(game):
  power = 1
  for value in game.values():
    power *= value

  return power

def get_game_sum(data):
  sum = 0
  for key in data.keys():
    min_cubes = find_min_cubes(data[key])
    power = calculate_power(min_cubes)
    sum += power
  
  return sum

reformatted_input = reformat_data(input)

print(get_game_sum(reformatted_input))