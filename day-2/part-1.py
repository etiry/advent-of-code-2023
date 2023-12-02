import re

with open('input.txt') as file:
  input = file.read().splitlines()

possible_cubes = {
  'red': 12,
  'green': 13,
  'blue': 14
}

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

def assess_possibility(game):
  for key, values in game.items():
    if any(i > possible_cubes[key] for i in values):
      return False
  
  return True

def get_game_sum(data):
  sum = 0
  for game in data:
    if assess_possibility(data[game]):
      sum += game
  
  return sum

reformatted_input = reformat_data(input)

print(get_game_sum(reformatted_input))