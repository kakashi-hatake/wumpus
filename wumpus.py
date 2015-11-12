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

def ask_for_cave():
  """ask the player to choose a cave"""
  print "which cave next"
  player_input = raw_input("> ")
  if(not player_input.isdigit() or
     int(player_input) not in caves[player_location]):
    print "the tunnels do no lead there"
    return None
  else:
    return int(player_input)

def get_action():
  """find out what the player wants to do next"""
  print "What do you do next"
  print "  m) move"
  print "  f) fire"
  action = raw_input("> ")
  if action in ["m", "f", "c"]:
    return action
  else:
    print "I do not know that action"
    return None

def do_movement():
  print "moving..."
  new_location = ask_for_cave()
  if new_location is None:
    return player_location
  else:
    return new_location

def do_shooting():
  print "firing"
  shoot_at = ask_for_cave()
  if shoot_at is None:
    return False

  if shoot_at == wumpus_location:
    print "twang ... mwaah! You shoot the wumpus"
    print "well ddne mighty wumpus hunter"
    print "the cave has now bee closed to outsiders because the wompi are now endangered"
  else:
    print "twang ... clatter, clatter"
    print "you wasted your arrow!"
    print "You lef the cave in descrace and returned home"
  return True



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
  
  action = get_action()
  if action is None:
    continue
  if action == "m":
    player_location = do_movement()
    if player_location == wumpus_location:
      print "Aargh! you got eaten by the Wumpus"
      break

  if action == "f":
    game_over = do_shooting()
    if game_over:
      break

  if action == "c":
    print wumpus_location
    

    
