from random import choice

def create_tunnel(cfrom, cto):
  """create a tunnel between from and to"""
  caves[cfrom].append(cto)
  caves[cto].append(cfrom)

def visit_cave(number):
  """mark a cave as used"""
  visited_caves.append(number)
  unvisited_caves.remove(number)

def choose_cave(cave_list):
  """pick a cave provided it has less than three tunnels"""
  number=choice(cave_list)
  while len(caves[number]) >=3:
    number = choice(cave_list)
  return number

def print_caves():
  """print cave structure"""
  for number in cave_numbers:
    print number, ":", caves[number]
  print '----------------'


def setup_caves(cave_numbers):
  """create the list of caves"""
  caves = []
  for cave in cave_numbers:
    caves.append([])
  return caves


def link_caves():
  """make two way tunnels between caves"""
  while unvisited_caves !=[]:
    this_cave = choose_cave(visited_caves)
    next_cave = choose_cave(unvisited_caves)
    create_tunnel(this_cave, next_cave)
    visit_cave(next_cave)

def finish_caves():
  """link the rest of the caves with one way tunnels"""
  for cave in cave_numbers:
    while len(caves[cave]) < 3:
      passage_to = choose_cave(cave_numbers)
      caves[cave].append(passage_to)

def print_location(player_location):
  """tell player were they are"""
  print "you are in cave", player_location
  print "from here you can see caves:"
  print caves[player_location]
  if wumpus_location in caves[player_location]:
    print "I smell a wumpus!"

def get_next_location():
  """get player's next location"""
  print "which cave next"
  player_input = raw_input("> ")
  if(not player_input.isdigit() or
     int(player_input) not in caves[player_location]):
    print "the tunnels do no lead there"
    return None
  else:
    return int(player_input)

cave_numbers = range(0,20)
unvisited_caves = range(0, 20)
visited_caves = []
caves = setup_caves(cave_numbers)

visit_cave(0)
##print_caves()
link_caves()
##print_caves()
finish_caves()


wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location):
  player_location = choice(cave_numbers)

while True:
  print_location(player_location)
  new_location = get_next_location()
  if new_location is not None:
    player_location = new_location
  if player_location == wumpus_location:
    print "Aargh! you got eaten by the Wumpus"
    break

    
