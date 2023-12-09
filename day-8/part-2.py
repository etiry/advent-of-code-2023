import re
from sympy.ntheory import factorint
from numpy import prod

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

def least_common_multiple(array):
  prime_array = list()
  for num in array:
    primes = factorint(num)
    for prime in primes:
      if prime not in prime_array:
        prime_array.append(prime)

  return prod(prime_array)

def traverse_map(directions, data):
  current = list()
  moves = list()

  for key in data.keys():
    if re.search('[A]$', key):
      current.append(key)

  for index in range(len(current)):
    count = 0
    go = True
    while go == True:
      for direction in directions:
        current[index] = find_node(current[index], direction, data)
        count += 1
        if re.search('[Z]$', current[index]):
          go = False
    moves.append(count)

  return moves


directions, nodes = parse_input(input)

moves = traverse_map(directions, nodes)

print(least_common_multiple(moves))