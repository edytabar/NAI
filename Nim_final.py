
# -*- coding: utf-8 -*-
"""
@authors: Marcin Grelewicz (s17692), Edyta Bartos (s17699)

This is a modified version of the NIM game: https://pl.wikipedia.org/wiki/Nim 
with rules described below:
    
    In turn, 2 players remove from one to five coins, from first, second or 
    third heap of coins. The player who removes the last coin from one of the 
    heaps looses. Players can remove coins from one heap at time.
    Example of player's move: "what do you play ? 1,3", where first number 
    means heap and second number of coins.

To run the game you need to install easyAI framework: 
https://zulko.github.io/easyAI/installation.html

In this game we use The Negamax algorithm: 
https://en.wikipedia.org/wiki/Negamax, which always look for the shortest 
path to victory, or the longest path to defeat.

"""

from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax
"""From easyAI framework there are imported 4 classes"""

class NIM(TwoPlayersGame):
    """This is a subclass of the class easyAI.TwoPlayersGame"""
    
    #Methods:
        
    #Initializes a game:
    def __init__(self, players, heap = None): 
        """The __init__ method initialize parameters: self, players, heap"""

        self.players = players 
        #Stores players (which must be a list of two Players) into 
        self.heap = [11, 16, 13]
        #Stores the values and longitude of the heap
        self.nplayer = 2
        #Tells which player plays first with self.nplayer = 1 # or 2 (here AI starts)
    
    #Returns all allowed moves:
    def possible_moves(self): 
        return ["%d,%d" % (i + 1, j) for i in range(len(self.heap))  
                for j in range(1, 6)]
    
    def make_move(self, move):
        """Method which transforms the game according to the move"""
        move = list(map(int, move.split(',')))
        self.heap[move[0] - 1] -= move[1]
    
    def win(self): 
        """Method which returns the conditions of winning the game"""
        return self.heap[0]<=0 or self.heap[1]<=0 or self.heap[2]<=0 
    
    def is_over(self): 
        """Methid which checks whether the game has ended"""
        return self.win() # Game stops when someone wins.
        
    def show(self):
        """Method to displays the game"""
        print(self.heap)
        
    def scoring(self): 
        """Method which gives a score to the current game (for the AI)"""
        return 100 if self.win() else 0 # For the AI

ai = Negamax(6)
#Variable ai stores the number of moves which ai is able to think about in advance
game = NIM([Human_Player(), AI_Player(ai)])
#Variable game stores the plaers which participate in the game
history = game.play()
#Variable history stores the moves in the game

if game.nplayer ==2:
    print('AI wins!')
else:
    print('You won!')
