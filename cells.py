class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        pass
        


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        game.win = True   # Change game state to win after step in


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        if game.move_made[-1] == 'w':
            move_back='s'
        elif game.move_made[-1] == 's':
            move_back='w'
        elif game.move_made[-1] == 'a':
            move_back='d'
        elif game.move_made[-1] == 'd':
            move_back='a'
        game.player.movement(move_back)     # Move back the player after step in
        game.move_made.pop()            # Not inclue this move in player's move made list
        wall_massage=('You walked into a wall. Oof!')
        return wall_massage


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        if game.player.num_water_buckets >= 1:
            game.player.add_water(-1)           # subtract player's number of water bucket
            game.line[game.player.row][game.player.col] = Air()     # Change current position to Air as Fire been put out
            f_message_1 = ('With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!')
            return f_message_1 
        else:
            game.lose = True        # Change game state to lose
            f_message_2 = ('\n'+'You step into the fires and watch your dreams disappear :(.')
            return f_message_2
        


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        game.player.add_water(1)
        game.line[game.player.row][game.player.col] = Air()
        w_message = ("Thank the Honourable Furious Forest, you've found a bucket of water!")
        return w_message

class Teleport_1:
    def __init__(self):
        self.display = '1'  

    def step(self, game):
        i=0
        find = False
        while i<len(game.line):
            x=0
            while x<len(game.line[i]):
                if type(game.line[i][x]) == Teleport_1:     # Search another teleport 1 in the grid as teleport are in pair
                    if i == game.player.row and x == game.player.col:  # Ensure the teleport find is not the one player
                        x+=1                                           # currently in, else keep searching
                        continue
                    else:
                        game.player.row = i     #change player's position to another teleport 1.
                        game.player.col = x
                        find = True
                        break
                x+=1
            if find:
                break
            i+=1
        T_massage = ('Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.')
        return T_massage


class Teleport_2:
    def __init__(self):
        self.display = '2'  

    def step(self, game):
        i=0
        find = False
        while i<len(game.line):
            x=0
            while x<len(game.line[i]):
                if type(game.line[i][x]) == Teleport_2:   # Search another teleport 2 in the grid as teleport are in pair
                    if i == game.player.row and x == game.player.col: # Ensure the teleport find is not the one player
                        x+=1                                          # currently in, else keep searching
                        continue
                    else:
                        game.player.row = i     #change player's position to another teleport 2.
                        game.player.col = x
                        find = True
                        break
                x+=1
            if find:
                break
            i+=1
        T_massage = ('Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.')
        return T_massage


