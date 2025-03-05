from game import Game
import os
import sys

# Function for printing player's move made
def move_massage():
    if len(trial.move_made)>1:
        massage=('Your moves: ')
        print('You made {} moves.'.format(len(trial.move_made)))
    else:
        massage=('Your move: ')
        print('You made {} move.'.format(len(trial.move_made)))
    i=0
    move_made_massage=''
    while i<len(trial.move_made):
        if i==0:
            move_made_massage+=trial.move_made[i]
            i+=1
            continue
        # Convert move made massage to the format eg.(a, w, s, d)
        move_made_massage=move_made_massage+', '+trial.move_made[i]
        i+=1
    massage+=move_made_massage
    print(massage)

# Function for print the massage for lose the game
def lose_process():
    print()
    print('The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.')
    print()
    move_massage()  # Print player's move made
    print()
    print('====================='+'\n'+
    '===== GAME OVER ====='+'\n'+
    '=====================')

# Function for print the massage for win the game
def win_process():
    print()
    print('You conquer the treacherous maze set up by the Fire Nation and reclaim the '+
    'Honourable Furious Forest Throne, restoring your hometown back to its former '+
    'glory of rainbow and sunshine! Peace reigns over the lands.')
    print()
    move_massage()  # Print player's move made
    print()
    print('====================='+'\n'+
    '====== YOU WIN! ====='+'\n'+
    '=====================')

file_name = sys.argv[1] # Determine file name of the board
trial = Game(file_name) # Create a game call trial
trial.read_map()        # Convert the board in the file to grid
trial.player_start()    # Determine player's staring position 
while True:
    print(trial.output_map())   # Output the final string for the game in terminal
    
    if trial.massage!=None:     
        print()
        print(trial.massage)    # print the massage game receive for step in a cell
    
    if trial.lose:
        lose_process()          
        break
    
    print()                     # Check game state, if lose or win go for its corresponding process
    
    if trial.win:
        win_process()
        break
    
    move = input('Input a move: ')  # Ask input for player's move
    if move == 'q' or move == 'Q':     
        print()
        print('Bye!')       # quite the game if receive input for quite
        break
    trial.gameMove(move)  
