# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 4:10 2020

@author: fisherv
"""

import Dominion
import testUtility

# Get player names
player_names = testUtility.getNames()

# Set up number of curses and victory cards
nV = testUtility.getNV(player_names)
nC = testUtility.getNC(player_names)

# Set up boxes
box = testUtility.getBoxes(nV)

# Set up supply order
supply_order = testUtility.getSupplyOrder()

# Put all cards in supply
supply = testUtility.getSupply(box, nC, nV, player_names)

# initialize the trash
trash = testUtility.getTrash()

# Construct the Player objects
players = testUtility.getPlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)