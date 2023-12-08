with open('input.txt') as file:
  input = file.read().splitlines()

def parse_input(input):
  parsed_input = list()
  for line in input:
    parsed_line = line.split(' ')
    parsed_input.append([parsed_line[0], int(parsed_line[1])])
  
  return parsed_input

def get_hand_type(hand):
  cards = dict()
  for card in hand:
    if card in cards:
      cards[card] += 1
    else:
      cards[card] = 1

  if 5 in cards.values():
    return "7"
  elif 4 in cards.values():
    return "6"
  elif 3 in cards.values() and 2 in cards.values():
    return "5"
  elif 3 in cards.values():
    return "4"
  elif list(cards.values()).count(2) == 2:
    return "3"
  elif 2 in cards.values():
    return "2"
  else:
    return "1"

def rank_hands(data):
  points = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    '1': 0
  }

  for hand in data:
    score = 0
    hand[0] = f'{get_hand_type(hand[0])}{hand[0]}'
    print(hand)
    for index, card in enumerate(reversed(list(hand[0]))):
      score += points[card] * ((index + 1) ** 40)
    hand.append(score)

  sorted_data = sorted(data, key=lambda x: x[2])

  return sorted_data

def get_total_winnings(data):
  total = 0

  for index, hand in enumerate(data):
    total += hand[1] * (index + 1)

  return total

parsed_input = parse_input(input)

print(parsed_input)

ranked_data = rank_hands(parsed_input)

print(ranked_data)

print(get_total_winnings(ranked_data))