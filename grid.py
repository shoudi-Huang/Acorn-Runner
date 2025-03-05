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

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    
    i=0
    screen=''
    big_sub_grid=[]
    while i<len(grid):
        x=0
        small_sub_grid=[]
        while x<len(grid[i]):
            # Define player's position in the grid and convert to player's display
            if i==player.row and x==player.col:     
                small_sub_grid.append(player.display) 
                x+=1
                continue
            # Convert each cell in a small list inside the grid to its diaplay
            small_sub_grid.append(grid[i][x].display)
            x+=1     
        big_sub_grid.append(small_sub_grid) 
        # Join all the cell's diaplay to one string 
        big_sub_grid[i]=''.join(big_sub_grid[i])
        # Join the string to the screen to became the final big string
        screen=screen+big_sub_grid[i]+'\n'
        i+=1
    screen=screen+'\n'
    # Add massage of player's number of water bucket to the final string
    if player.num_water_buckets>=0 and player.num_water_buckets!=1:
        screen+=('You have {} water buckets.'.format(player.num_water_buckets))
    elif player.num_water_buckets==1:
        screen+=('You have {} water bucket.'.format(player.num_water_buckets))
    return screen


