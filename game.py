from game_parser import read_lines
from game_parser import parse
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport_1,
    Teleport_2
)

class Game:
    def __init__(self, filename):       
        self.filename = filename        # Take the board's filename
        self.move_made = []
        self.line = None            
        self.player = None
        self.massage = None         
        self.win = False            # Determent lose or win
        self.lose = False

    def gameMove(self, move): 
        move = move.lower()     # Convert all move instraction to lower case        
        self.massage = None
        if self.player.movement(move):      # If is the valid input. (w, a, s, d, e)
            self.move_made.append(move)             # Move the player
            if self.player.col<0 or self.player.col>= len(self.line[self.player.row]) or self.player.row< 0 or self.player.row>len(self.line):
                if self.move_made[-1]=='w':
                    move_back='s'
                elif self.move_made[-1]=='s':       # If the player walk out of board move back the player 
                    move_back='w'                   # and treat it as step into wall.
                elif self.move_made[-1]=='a':
                    move_back='d'
                elif self.move_made[-1]=='d':
                    move_back='a'
                self.player.movement(move_back)
                self.move_made.pop()
                self.massage = ('You walked into a wall. Oof!')

            else:  
                self.massage = self.line[self.player.row][self.player.col].step(self)  
                # Received massage which correspond to the cell player step in.
        else:
            self.massage = self.player.invalid_input_massage
            # Received massage for invalid input.

    def read_map(self):
        line = read_lines(self.filename)       # Convert the board into grid 
        self.line = parse(line)             

    def player_start(self):
        i=0
        find = False
        while i<len(self.line):
            x=0
            while x<len(self.line[i]):
                if type(self.line[i][x])==Start:        # Determent player's starting point 
                    player = Player(i, x)               # by searching the cell Start.
                    find = True
                    break
                x+=1 
            if find:
                break
            i+=1
        self.player = player

    def output_map(self):
        return grid_to_string(self.line, self.player)       # Convert the grid to string for final output





    




    
