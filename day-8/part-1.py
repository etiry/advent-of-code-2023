import re

with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  directions = input[0]

  split_nodes = [n.split(' = ') for n in input[2:]]
  nodes = {x[0]:x[1] for x in split_nodes}

  for key, value in nodes.items():
    value = re.sub('[()]+', '', value)
    value = value.split(', ')
    nodes[key] = value

  return directions, nodes

def find_node(previous_node, direction, nodes):
  if direction == 'L':
    next_node = nodes[previous_node][0]
  else:
    next_node = nodes[previous_node][1]

  return next_node

def traverse_map(directions, data):
  count = 0
  current = 'AAA'
  go = True

  while go == True:
    for direction in directions:
      current = find_node(current, direction, data)
      count += 1
      if current == 'ZZZ':
        go = False

  return count


directions, nodes = parse_input(input)

print(traverse_map(directions, nodes))