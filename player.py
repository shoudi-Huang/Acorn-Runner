class Player:
    def __init__(self,row,col):
        self.display = 'A'
        self.num_water_buckets = 0  
        self.row = row              # Determine player's position 
        self.col = col
        # Massage that can pass into game after invalid input
        self.invalid_input_massage = 'Please enter a valid move (w, a, s, d, e, q).'

    def movement(self, move):
        if move=='w' or move=='a' or move=='s' or move=='d' or move=='e':
            if move=='w':
                self.row-=1        
            elif move=='a':         # Move player's position by its row and column
                self.col-=1
            elif move=='s':
                self.row+=1
            elif move=='d':
                self.col+=1
            return True
        else:
            return False
    # Function for add or subtract player's number of water buckets
    def add_water(self, num_water):     
        if num_water!=1 and num_water!=-1:      # Player can only add or subtract 1 water at a time.
            raise ValueError('Water can only add or subtract by 1')
        self.num_water_buckets+=num_water


