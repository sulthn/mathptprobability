import random

# N+-+-+-+-+-+-+

# -1 neutral
# 1 positive
# 0 negative

class Player:
    def __init__(self, name):
        self.remaining_spaces = 14
        self.pos = -1   # Start at -1 because the first space (N) is not included in counting.
        self.state = -1
        self.points = 0
        self.name = name
    def print(self):
        print("player =", self.name, \
             "points =", self.points, \
            "pos =", self.pos, \
            "remaining spaces =", self.remaining_spaces)
        print("state =", "+-"[self.state])

    
die = (1, 2, 3, 4, 3, 2)

p1 = Player("sunarno")
p2 = Player("rizki")
p3 = Player("bambang")
p4 = Player("farhan")
remaining_players = 4

players = [p1, p2, p3, p4]

won = []

turns = 1
player_index = 0
current_turn = players[player_index]

while remaining_players > 0:
    if current_turn.remaining_spaces == 0:      # No remaining spaces left
        if (len(won) == 0):                     # If this is the first player to finish
            won.append(current_turn)            # additional two points

        player_index = (player_index + 1) % 4   # Next player
        current_turn = players[player_index]
        remaining_players -= 1                   # Decrease player count

        print(remaining_players)
        continue
    
    roll = die[random.randint(0, 5)]    # Roll die

    # If the roll is more than the available spaces
    if (current_turn.remaining_spaces - roll < 0) and current_turn.remaining_spaces <= 4: # (1, 2, 3, 4, 3, 2) 
        print("roll =", roll)
        current_turn.print()
        input("re-roll")
        continue    # Then re-roll

    if (current_turn.remaining_spaces - roll < 0):
        current_turn.remaining_spaces -= roll       # Decrease the remaining spaces from roll
        current_turn.pos += roll + 1                # Change position
    else:
        current_turn.remaining_spaces -= roll + 1   # Decrease the remaining spaces from roll
        current_turn.pos += roll + 1                # Change position
                        
    
    # If the current state is different than the state on the position then
    if (current_turn.state != ((current_turn.pos - 1) % 2)):
        print("greendot")
        current_turn.points += 1    # Add point to player
    else:
        print("blackdot")           # If not, black dot

    current_turn.state = current_turn.pos % 2   # Set the state

    print("roll =", roll)
    current_turn.print()
    print("=== END OF TURN ===")
    input()
    
    player_index = (player_index + 1) % 4
    current_turn = players[player_index]        

won[0].points += 2    

print(won[0].name)

for i in range(4):
    players[i].print()
