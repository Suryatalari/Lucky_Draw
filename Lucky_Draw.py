import random
players=random.sample(range(300,325),10)                #Choosing 10 random numbers between 300 and 325.
for i in range(0,10):                                   
	print("Player",i+1,":",players[i])                  #Display the random numbers assigned to each player.
num=players.index(max(players))+1                       #Determine the maximum draw among the players.
print("The winner is Player",num,":",max(players))