from game import Game
from test_parser import find_parse_type
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

def test_game_readmap():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()

    expected = [['Wall', 'Wall', 'Start', 'Wall', 'Wall'], 
    ['Wall', 'Air', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Wall', 'End', 'Wall', 'Wall']]
    parse_line_type = find_parse_type(trial.line)
    
    # Check read map successfully convert the board into grid
    assert parse_line_type == expected, 'Test game: Readmap test case False'
    print('Test game: Readmap test case pass')

def test_game_output_map():
    trial = Game('tests_use_board/board_hard.txt')
    trial.read_map()
    trial.player_start()

    expected = expected = ('*A*************' + '\n' + 
    '*       2 *   *' + '\n' + 
    '* *** ** **** *' + '\n' + 
    '* *  W*   1   *' + '\n' + 
    '* ***** ***** *' + '\n' +
    '*  2 *   ** *F*' + '\n' +
    '* ** ***  F   *' + '\n' +
    '* 1********F  *' + '\n' +
    '*************Y*' + '\n' +
    '\n' +
    'You have 0 water buckets.')
    
    assert trial.output_map() == expected, 'Test game: Output map test case False' # Check did game return the correct board                                                                              
    print('Test game: Output map test case pass')                                  # and massage in one string.
    
def test_game_player_starting_point():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()
    
    expected = [0, 2]    # Correct starting point.
    output = [trial.player.row, trial.player.col]
    
    assert output == expected, 'Test game: Correct Starting_point test case False'    # Check did player start in the correct starting point.
    print('Test game: Correct Starting_point test case pass')

def test_game_player_movement():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()

    false_massage = 'Test game: Player movement test case False'

    trial.gameMove('s')
    assert [trial.player.row, trial.player.col] == [1, 2], false_massage    #Check move down.
    
    trial.gameMove('d')
    assert [trial.player.row, trial.player.col] == [1, 3], false_massage    #Check move right.
    
    trial.gameMove('a')
    assert [trial.player.row, trial.player.col] == [1, 2], false_massage    #Check move left.
    
    trial.gameMove('w')
    assert [trial.player.row, trial.player.col] == [0, 2], false_massage    #Check move up.
    
    trial.gameMove('e')
    assert [trial.player.row, trial.player.col] == [0, 2], false_massage    #Check wait a turn.
    print('Test game: Player movement test case pass')

def test_game_all_cap_input():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()

    false_massage = 'Test game: All CAP input test case False'

    trial.gameMove('S')
    assert [trial.player.row, trial.player.col] == [1, 2], false_massage    #Check move down.
    
    trial.gameMove('D')
    assert [trial.player.row, trial.player.col] == [1, 3], false_massage    #Check move right.
    
    trial.gameMove('A')
    assert [trial.player.row, trial.player.col] == [1, 2], false_massage    #Check move left.
    
    trial.gameMove('W')
    assert [trial.player.row, trial.player.col] == [0, 2], false_massage    #Check move up.
    
    trial.gameMove('E')
    assert [trial.player.row, trial.player.col] == [0, 2], false_massage    #Check wait a turn.
    print('Test game: All CAP input test case pass')

def test_game_invalid_input():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()
    trial.gameMove('b')
    expected_massage = 'Please enter a valid move (w, a, s, d, e, q).'
    expected_move_made = []
    false_massage = 'Test game: Invalid input test case False'
    assert trial.massage == expected_massage, false_massage     # Check massage passed into game after the invalid input.
    assert trial.move_made == expected_move_made, false_massage  # Check invalid input not count in the move that player made.
    print('Test game: Invalid input test case pass')

def test_game_end_point():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()
    move_ls = ['s', 's']    
    for move in move_ls:
        trial.gameMove(move)
    assert trial.win == True, 'Test game: Win test case False' # Check game state became win.
    print('Test game: Win test case pass')

def test_game_walk_into_wall():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()

    move_ls = ['s', 'd', 'd']
    for move in move_ls:
        trial.gameMove(move)

    expected_massage = ('You walked into a wall. Oof!')
    expected_move_made = ['s', 'd']
    expected_player_position = [1, 3]
    output_player_position = [trial.player.row, trial.player.col]

    false_massage = 'Test game: Walk into wall test case False'
    assert output_player_position == expected_player_position, false_massage    #Check did player move back after step into wall.
   
    assert trial.massage == expected_massage, false_massage      #Check What massage been passed into game after step into wall.
    
    assert trial.move_made == expected_move_made, false_massage  #Check did game incounter the move for step into wall.
    print('Test game: Walk into wall test case pass')

def test_game_walk_out_of_board():
    trial = Game('tests_use_board/board_simple.txt')
    trial.read_map()
    trial.player_start()

    trial.gameMove('w')       #Try to walk out of board from starting point
    
    expected_massage = ('You walked into a wall. Oof!')
    expected_move_made = []
    expected_player_position = [0, 2]
    output_player_position = [trial.player.row, trial.player.col]

    false_massage = 'Test game: Walk out of board test case False'
    assert output_player_position == expected_player_position, false_massage    #Check did player move back after step out of board.
    
    assert trial.massage == expected_massage, false_massage      #Check What massage been passed into game after step out of boardl.
   
    assert trial.move_made == expected_move_made, false_massage  #Check did game incounter the move for step out of board.
    print('Test game: Walk out of board test case pass')

def test_game_step_into_water():
    trial = Game('tests_use_board/board_hard.txt')
    trial.read_map()
    trial.player_start()

    move_ls = ['s', 'd', 'd', 'd', 'd', 's', 's']      
    for move in move_ls:
        trial.gameMove(move)

    expected_massage = ("Thank the Honourable Furious Forest, you've found a bucket of water!")
    expected_number_water_bucket = 1

    false_massage = 'Test game: Step into water test case False'
    assert trial.massage == expected_massage, false_massage              #Check what massage been passed into game after step into water.
    
    assert trial.player.num_water_buckets == expected_number_water_bucket, false_massage      #Check did player's number of water bucket increase after step into water.
    
    assert type(trial.line[trial.player.row][trial.player.col]) == Air, false_massage     # Check did water became air space after step in.
    print('Test game: Step into water test case pass')

def test_game_step_into_fire():
    trial = Game('tests_use_board/board_medium.txt')
    trial.read_map()
    trial.player_start() 

    move_ls_1 = ['s', 'a', 's', 's', 's', 'd', 'd', 'd']    #Walk into fire with 0 water bucket
    for move in move_ls_1:
        trial.gameMove(move)

    expected_massage_1 = ('\n'+'You step into the fires and watch your dreams disappear :(.')
    
    false_massage = 'Test game: Step into fire test case False'
    assert trial.massage == expected_massage_1, false_massage    #Check massage passed into game after step into fire with no water.
    
    assert trial.lose == True, false_massage        #Check did game state became lose.
    
    # Restart game.
    trial = Game('tests_use_board/board_medium.txt')
    trial.read_map()                     # Restart game.
    trial.player_start()

    move_ls_2 = ['s', 'd', 'd', 's', 's', 's']      #Walk into fire with water bucket.
    for move in move_ls_2:
        trial.gameMove(move)

    expected_massage_2 = ('With your strong acorn arms, you throw a water bucket at the fire. ' +
    'You acorn roll your way through the extinguished flames!')

    # Check massage passed into game after step into fire with water.
    assert trial.massage == expected_massage_2, false_massage     
    
    # Check did player's number of water bucket decrease.
    assert trial.player.num_water_buckets == 0, false_massage     
    
    #Check did fire became air space after step in
    assert type(trial.line[trial.player.row][trial.player.col]) == Air, false_massage   
    print('Test game: Step into fire test case pass')

def test_game_step_into_teleport():
    trial = Game('tests_use_board/board_hard.txt')
    trial.read_map()
    trial.player_start() 

    move_ls = ['s', 's', 's', 's', 's', 's', 's', 'd']
    for move in move_ls:
        trial.gameMove(move)

    expected_position_1 = [3, 10]
    expected_massage = ('Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.')
    output_position_1 = [trial.player.row, trial.player.col]

    false_massage = 'Test game: Step into teleport test case False'
    
    assert output_position_1 == expected_position_1, false_massage    #Check did player been teleport to correct position.
    assert trial.massage == expected_massage, false_massage       #Check masssage passed into game after step into teleport.
    
    trial.gameMove('e')    # Wait a turn on teleport and teleport back.
    
    expected_position_2 = [7, 2]
    output_position_2 = [trial.player.row, trial.player.col]

    assert output_position_2 == expected_position_2, false_massage    # Check did player teleport back by wait a turn.
    print('Test game: Step into teleport test case pass')



def run_tests():
    test_game_readmap()
    test_game_output_map()
    test_game_player_starting_point()
    test_game_player_movement()
    test_game_all_cap_input()
    test_game_invalid_input()
    test_game_walk_into_wall()
    test_game_walk_out_of_board()
    test_game_step_into_water()
    test_game_step_into_fire()
    test_game_step_into_teleport()

