from math import prod
import re

with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  output = list(tuple())

  new_lines = list()
  for line in input:
    line = re.sub('[a-zA-Z:]+', '', line)
    line = line.split(' ')
    line = list(filter(str.strip, line))
    line = [int(n) for n in line]
    new_lines.append(line)

  for i in range(len(new_lines[0])):
    output.append((new_lines[0][i], new_lines[1][i]))

  return output

def count_ways(data):
  ways = list()
  for race in data:
    count = 0
    for i in range(race[0]):
      distance = i * (race[0] - i)
      if distance > race[1]:
        count += 1
    ways.append(count)

  return ways


data = parse_input(input)

print(prod(count_ways(data)))