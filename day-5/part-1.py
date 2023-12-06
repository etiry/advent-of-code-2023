import itertools
from collections import OrderedDict
from numpy import inf

with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

  split_list = [list(y) for x, y in itertools.groupby(input, lambda z: z == '') if not x]

  seeds = [int(n) for n in split_list[0][0].replace(f'seeds: ', '').split(' ')]

  parsed_input = OrderedDict()
  for map in maps:
    for l in split_list:
      if l[0].find(map) > -1:
        new_list = list()
        for item in l[1:]:
          split_item = item.split(' ')
          new_list.append({
          'target': int(split_item[0]),
          'source': int(split_item[1]),
          'range': int(split_item[2])
          })
        parsed_input[map] = new_list

  return seeds, parsed_input

def calculate_mappings(seeds, data):
  mappings = dict()
  for seed in seeds:
    mappings[seed] = [seed]

    for key in data.keys():
      added = False
      for row in data[key]:
        if mappings[seed][-1] in range(row['source'], row['source'] + row['range'] + 1) and added == False:
            diff = mappings[seed][-1] - row['source']
            mappings[seed].append(row['target'] + diff)
            added = True

      if added == False:
        mappings[seed].append(mappings[seed][-1])

  return mappings

def find_lowest(mappings):
  lowest = inf

  for seed in mappings:
    if mappings[seed][-1] < lowest:
      lowest = mappings[seed][-1]

    print(lowest)

  return lowest

seeds, parsed_input = parse_input(input)

mappings = calculate_mappings(seeds, parsed_input)

print(mappings)

print(find_lowest(mappings))
