import random
players=random.sample(range(300,325),10)
for i in range(0,10):
	print("Player",i+1,":",players[i])
num=players.index(max(players))+1
print("The winner is Player",num,":",max(players))