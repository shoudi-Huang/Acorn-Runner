from game import Game
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
import sys

# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)

def DFS(file_name):
    move_made = []
    extra_move_made = []
    dead_end = []
    water_find = False
    pervious_number_water_bucket = 0

    while True:
        visited_ls = []
        #print(move_made)
        trial = Game(file_name)
        trial.read_map()
        trial.player_start()
        visited_ls.append(trial.line[trial.player.row][trial.player.col])

        if len(move_made)>0:
            for move in move_made:
                trial.gameMove(move)
                if not water_find:
                    visited_ls.append(trial.line[trial.player.row][trial.player.col])
        
        if len(extra_move_made)>0:
            #print(extra_move_made)
            for extra_move in extra_move_made:
                trial.gameMove(extra_move)
                visited_ls.append(trial.line[trial.player.row][trial.player.col])
        
        if pervious_number_water_bucket+1 == trial.player.num_water_buckets:
            if len(extra_move_made)>0:
                move_made = move_made + extra_move_made
                extra_move_made = []
            dead_end = []
            visited_ls = []
            #print(water_find)

        pervious_number_water_bucket = trial.player.num_water_buckets

        if len(dead_end)>0:
            i=0
            while i<len(dead_end):
                visited_ls.append(trial.line[dead_end[i][0]][dead_end[i][1]])
                i+=1

        row = trial.player.row
        col = trial.player.col
         
        if trial.win:
            return trial.move_made

        
        if type(trial.line[row+1][col]) != Wall and trial.line[row+1][col] not in visited_ls and row+1 < len(trial.line):
            if type(trial.line[row+1][col]) == Fire:
                if trial.player.num_water_buckets>0:
                    if water_find:
                        extra_move_made.append('s')
                        continue
                    else:
                        move_made.append('s')
                        continue
            else:
                if water_find:
                    extra_move_made.append('s')
                    continue
                move_made.append('s')
                if type(trial.line[row+1][col]) == Water:
                    water_find = True
                continue
            
        if type(trial.line[row][col+1]) != Wall and trial.line[row][col+1] not in visited_ls and col+1 < len(trial.line[row]):
            if type(trial.line[row][col+1]) == Fire:
                if trial.player.num_water_buckets>0:
                    if water_find:
                        extra_move_made.append('d')
                        continue
                    else:
                        move_made.append('d')
                        continue
            else:
                if water_find:
                    extra_move_made.append('d')
                    continue
                move_made.append('d')
                if type(trial.line[row][col+1]) == Water:
                    water_find = True
                continue
                
        if type(trial.line[row-1][col]) != Wall and trial.line[row-1][col] not in visited_ls and row-1 >= 0:
            if type(trial.line[row-1][col]) == Fire:
                if trial.player.num_water_buckets>0:
                    if water_find:
                        extra_move_made.append('w')
                        continue
                    else:
                        move_made.append('w')
                        continue
            else:
                if water_find:
                    extra_move_made.append('w')
                    continue
                move_made.append('w')
                if type(trial.line[row-1][col]) == Water:
                    water_find = True
                continue
                
        if type(trial.line[row][col-1]) != Wall and trial.line[row][col-1] not in visited_ls and col-1 >= 0:
            if type(trial.line[row][col-1]) == Fire:
                if trial.player.num_water_buckets>0:
                    if water_find:
                        extra_move_made.append('a')
                        continue
                    else:
                        move_made.append('a')
                        continue
            else:
                if water_find:
                    extra_move_made.append('a')
                    continue
                move_made.append('a')
                if type(trial.line[row][col-1]) == Water:
                    water_find = True
                continue
        
        if type(trial.line[row][col]) == Teleport_1 or type(trial.line[row][col]) == Teleport_2:
            i=0
            while i<len(trial.line):
                x=0
                while x<len(trial.line[i]):
                    if type(trial.line[i][x]) == type(trial.line[row][col]):
                        if i == row and x == col:
                            x+=1
                            continue
                        dead_end.append([i, x])
                    x+=1
                i+=1
        dead_end.append([row, col])
        if type(trial.line[row][col]) == Start:
            return []
        if water_find:
            extra_move_made.pop()
        else:
            move_made.pop()
        continue


        
def solve(mode, file_name):
    if mode == 'DFS':
        return DFS(file_name)
        
    #elif mode == 'BFS':



if __name__ == "__main__":
    mode = sys.argv[2]
    file_name = sys.argv[1]
    solution_found = False
    solution = solve(mode, file_name)
    if len(solution)>0:
        solution_found = True
    if solution_found:
        print('Path has {} moves.'.format(len(solution)))
        i=0
        move_made_massage=''
        while i<len(solution):
            if i==0:
                move_made_massage+=solution[i]
                i+=1
                continue
            move_made_massage=move_made_massage+', '+solution[i]
            i+=1
        
        begin_massage = ('Path: ')
        final_massage = begin_massage + move_made_massage
        print(final_massage)
        # Print your solution...
    else:
        print("There is no possible path.")


