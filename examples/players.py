players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])

print(players[-3:]) # -3, -2, -1

for player in players[:3] :
    print(player.title())