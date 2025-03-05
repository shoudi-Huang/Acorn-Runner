from grid import grid_to_string
from player import Player
from game_parser import read_lines
from game_parser import parse

def test_grid_simple():
    # Test read_lines in simply board
    line = read_lines('tests_use_board/board_simple.txt')
    line = parse(line)
    player = Player(0, 2)

    expected = ('**A**' + '\n' + '*   *' + '\n'+'**Y**' + '\n'*2 +'You have 0 water buckets.')
    
    assert grid_to_string(line, player) == expected, 'Test grid: Simple test case False'
    print('Test grid: Simple test case pass')

def test_grid_complex():
    # Test read_lines in complex board
    line = read_lines('tests_use_board/board_hard.txt')
    line = parse(line)
    player = Player(1, 1)

    expected = ('*X*************' + '\n' + 
    '*A      2 *   *' + '\n' + 
    '* *** ** **** *' + '\n' + 
    '* *  W*   1   *' + '\n' + 
    '* ***** ***** *' + '\n' +
    '*  2 *   ** *F*' + '\n' +
    '* ** ***  F   *' + '\n' +
    '* 1********F  *' + '\n' +
    '*************Y*' + '\n' +
    '\n' +
    'You have 0 water buckets.')

    assert grid_to_string(line, player) == expected, 'Test grid: Complex test case False'
    print('Test grid: Complex test case pass')

def test_grid_player_out_board():
    line = read_lines('tests_use_board/board_simple.txt')
    line = parse(line)

    player = Player(1, 6)   # Set player's position out of board

    # Expecte the player will not be print out as not on the board
    expected = ('**X**' + '\n' + '*   *' + '\n'+'**Y**' + '\n'*2 +'You have 0 water buckets.')

    assert grid_to_string(line, player) == expected, 'Test grid: Player out of board test case False'
    print('Test grid: Player out of board test case pass')

def test_grid_many_water_bucket():
    line = read_lines('tests_use_board/board_simple.txt')
    line = parse(line)
    player = Player(1, 2)

    player.num_water_buckets = 8   
    expected = ('**X**' + '\n' + '* A *' + '\n' + '**Y**' + '\n'*2 + 'You have 8 water buckets.')

    assert grid_to_string(line, player) == expected, 'Test grid: More than 1 water bucket test case False'
    print('Test grid: More than 1 water bucket test case pass')

def test_grid_one_water_bucket():
    line = read_lines('tests_use_board/board_simple.txt')
    line = parse(line)

    player = Player(1, 2)
    player.add_water(1)
    expected = ('**X**' + '\n' + '* A *' + '\n' + '**Y**' + '\n'*2 + 'You have 1 water bucket.')

    # Expecte 'bucket' without 's' for 1 water.
    assert grid_to_string(line, player) == expected, 'Test grid: One water bucket test case False'
    print('Test grid: One water bucket test case pass')

def test_grid_empty_grid():
    line = []
    player = Player(1, 1)
    expected = '\n' + 'You have 0 water buckets.'
    # Test grid with empty board (edge case)
    assert grid_to_string(line, player) == expected, 'Test grid: Empty grid test case Fasle'
    print('Test grid: Empty grid test case pass')



def run_tests():
    test_grid_simple()
    test_grid_complex()
    test_grid_player_out_board()
    test_grid_many_water_bucket()
    test_grid_one_water_bucket()
    test_grid_empty_grid()

