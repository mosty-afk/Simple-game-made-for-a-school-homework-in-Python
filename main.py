import random as r
import time as t

player1 = 0
player2 = 0
objective = 100
counter = 0
buff = 15
nerf = 5
buff2= 90
nerf2= 90
while player1 < objective and player2 < objective:
    dice = r.randint(2, 12)
    
    if counter % 2 == 0:
        player1 = player1 + dice
        print(f"Player 1 rolled: {dice}")
        print(f"Player 1 advanced to: {player1} spaces")
        t.sleep(1)

        if player1 == 15:
            print(f"Player 1 received a buff: +{buff}")
            player1 += buff
        elif player1 == 27:
            print(f"Player 1 received a nerf: -{nerf}")
            player1 -= nerf
        elif player1 == 6:
            print(f"Player 1 has received a super buff: +{buff2}")
            player1 += buff2
        elif player1 == 94:
            print(f"Player 1 has received a super nerf:  -{nerf2}")
            player1 -= nerf2
    else:
        player2 = player2 + dice
        print(f"Player 2 rolled: {dice}")
        print(f"Player 2 advanced to: {player2} spaces")
        t.sleep(1)
    
        if player2 == 15:
            print(f"Player 2 received a buff: +{buff}")
            player2 += buff
        elif player2 == 6:
            print(f"Player 2 received a nerf: -{nerf}")
            player2 -= nerf
        elif player2 == 5:
            print(f"Player 2 has received a super buff:  +{buff2}")
            player2 += buff2
        elif player2 == 94:
            print(f"Player 2 has received a super nerf:  -{nerf2}")
            player2 -= nerf2

    counter += 1

print("End game")

if player1 >= objective:
    print("Player 1 won!")
else:
    print("Player 2 won!")