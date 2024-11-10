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
        self.turn = 0
        self.logs = []

    def print(self):
        print("player =", self.name, \
            "points =", self.points, \
            "pos =", self.pos, \
            "remaining spaces =", self.remaining_spaces)
        print("state =", "+-"[self.state])
    
    def log(self, land, roll, dot):
        self.turn += 1
        self.logs.append((f"turn = {self.turn}", \
            f"Player = {self.name}", \
            f"Rolled = {roll}", \
            f"Landed on = {land}", \
            f"Position = {self.pos}", \
            f"Points = {self.points}", \
            f"Remaining Spaces = {self.remaining_spaces}", \
            f"State = {"+-"[self.state]}", \
            f"Dot = {dot}"))

    
die = (1, 2, 3, 4, 3, 2)

p1 = Player("sunarno")
p2 = Player("rizki")
p3 = Player("bambang")
p4 = Player("farhan")
remaining_players = 4

players = [p1, p2, p3, p4]

winner = Player("")

turns = 1
player_index = 0
current_turn = players[player_index]

while remaining_players > 0:
    if current_turn.remaining_spaces <= 0:  # No remaining spaces left
        if (winner is not None):            # If this is the first player to finish
            winner = current_turn           # additional two points to the finisher

        player_index = (player_index + 1) % 4   # Next player index
        current_turn = players[player_index]    # Change the turn to the next player
        remaining_players -= 1                  # Decrease player count
        continue
    
    roll = die[random.randint(0, 5)]    # Roll die

    # If the roll is more than the available spaces
    if (current_turn.remaining_spaces - roll < 0) and current_turn.remaining_spaces <= 4: # (1, 2, 3, 4, 3, 2) 
        current_turn.log("re-roll", roll, "no dot") # Log turn
        layer_index = (player_index + 1) % 4        # Next player index
        current_turn = players[player_index]        # Change the turn to the next player
        continue                                    # Continue to the next player

    temp_pos = current_turn.pos

    if (current_turn.remaining_spaces - roll <= 0):
        current_turn.remaining_spaces -= roll       # Decrease the remaining spaces from roll
        current_turn.pos += roll + 1                # Change position
    else:
        current_turn.remaining_spaces -= roll + 1   # Decrease the remaining spaces from roll
        current_turn.pos += roll + 1                # Change position
                        
    
    # If the current state is different than the state on the position then
    if (current_turn.state != ((current_turn.pos - 1) % 2)):
        dot = "greendot"
        current_turn.points += 1    # Add point to player
    else:
        dot = "blackdot"            # If not, black dot

    current_turn.state = current_turn.pos % 2       # Set the state
    current_turn.log(temp_pos + roll, roll, dot)    # Log turn
    
    player_index = (player_index + 1) % 4   # Next player index
    current_turn = players[player_index]    # Change the turn to the next player

winner.points += 2

print(winner.name, "finished first!")

for i in range(4):
    for i in players[i].logs:
        print(i)
    print()
