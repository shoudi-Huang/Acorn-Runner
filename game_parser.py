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


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        f = open(filename, 'r')
    except FileNotFoundError:       # Handle the situtation when file not find
        print('{} does not exist!'.format(filename))
        exit()
    
    ls=[]
    while True:
        line = f.readline()
        if line == '':
            break
            
        ls.append(line)         #Read file into a list as each line is a string.
    
    f.close()
    return ls
        

def parse(lines):       # Take in the list from read_lines
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    i=0
    ls=[]
    num_X=0             
    num_Y=0             
    num_teleport_1=0
    num_teleport_2=0
    while i<len(lines):
        new_ls=[]
        append_ls=list(lines[i])    # list each string in the initial list to another append_list
        z=0
        while z<len(append_ls):     # Define each string in append_list in a class    
            if append_ls[z]=='X':   
                append_ls[z]=Start()
                num_X+=1
            elif append_ls[z]=='Y':     
                append_ls[z]=End()      # Count the number of staring, ending point and teleport
                num_Y+=1                # for determentation of the validity of the board
            elif append_ls[z]==' ':
                append_ls[z]=Air()
            elif append_ls[z]=='*':
                append_ls[z]=Wall()
            elif append_ls[z]=='F':
                append_ls[z]=Fire()
            elif append_ls[z]=='W':
                append_ls[z]=Water()
            elif append_ls[z]=='1':
                append_ls[z]=Teleport_1()
                num_teleport_1+=1
            elif append_ls[z]=='2':
                append_ls[z]=Teleport_2()
                num_teleport_2+=1
            elif append_ls[z]=='\n':        # Ignore new line character
                z+=1
                continue
            else:                  
                raise ValueError('Bad letter in configuration file: {}.'.format(append_ls[z]))
            z+=1                # Handle unexpected letter appears
       
        x=0
        while x<len(append_ls):
            if append_ls[x]!='\n':
                new_ls.append(append_ls[x])  # Deleted the new line character
            x+=1
        i+=1                # Append this new_list contian different object to the final_list
        ls.append(new_ls)       
                                #Handle the situtation where too many or no start or end
    if num_X!=1:                #and not pair up teleport.
        raise ValueError('Expected 1 starting position, got {}.'.format(num_X))
    if num_Y!=1:
        raise ValueError('Expected 1 ending position, got {}.'.format(num_Y))
    if num_teleport_1>2 or num_teleport_1==1:
        raise ValueError('Teleport pad 1 does not have an exclusively matching pad.')
    if num_teleport_2>2 or num_teleport_2==1:
        raise ValueError('Teleport pad 2 does not have an exclusively matching pad.')
    
    return ls       # Return the final_list
            

