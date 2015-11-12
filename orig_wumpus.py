from random import choice


cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
  caves.append([])

for i in cave_numbers:
  for j in range(3):
    passage_to = choice(cave_numbers)
    caves[i].append(passage_to)
    caves[passage_to].append(i)

wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location):
  player_location = choice(cave_numbers)

print 'Welcome To Hunt The Wumpus'
print 'You can see', len(cave_numbers), "caves"
print "To play type the number of the cave you want to enter"

while True:
  print ' you are in cave', player_location
  print "You can see caves", caves[player_location]
  if wumpus_location in caves[player_location]:
    print 'I smell a Wumpus!'
  if wumpus_friend_location in caves[player_location]:
    print 'I smell a Wumpus!'

  print 'Which cave next?'
  player_input = raw_input("> ")
  if (not player_input.isdigit() or
      int(player_input) not in caves[player_location]):
    print player_input, "is not a cave that I can see"

  else:
    player_location = int(player_input)
    if (player_location == wumpus_location or
        player_location == wumpus_friend_location):
      print "Yay! You got hugged by a wumpus!"
      break
    
