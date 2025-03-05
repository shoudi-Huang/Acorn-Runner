from game_parser import parse
from game_parser import read_lines
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

# Function for listing cell's type in the grid for further testing.
def find_parse_type(parse_line): 
    parse_line_type = []
    i=0
    while i < len(parse_line):
        sub_section = []
        x=0
        while x < len(parse_line[i]):
            if type(parse_line[i][x]) == Wall:
                sub_section.append('Wall')
            elif type(parse_line[i][x]) == Air:
                sub_section.append('Air')
            elif type(parse_line[i][x]) == Start:
                sub_section.append('Start')
            elif type(parse_line[i][x]) == End:
                sub_section.append('End')
            elif type(parse_line[i][x]) == Fire:
                sub_section.append('Fire')
            elif type(parse_line[i][x]) == Water:
                sub_section.append('Water')
            elif type(parse_line[i][x]) == Teleport_1:
                sub_section.append('Teleport_1')
            elif type(parse_line[i][x]) == Teleport_2:
                sub_section.append('Teleport_2')
            x+=1
        parse_line_type.append(sub_section)
        i+=1
    return parse_line_type

def test_readline_simple():
    expected = ['**X**\n', '*   *\n', '**Y**\n']
    assert read_lines('tests_use_board/board_simple.txt') == expected, 'Test readline: Simple board test case False'
    print('Test readline: Simple board test case pass')

def test_readline_complex():
    expected = ['*X*************\n', '*       2 *   *\n', '* *** ** **** *\n', '* *  W*   1   *\n', '* ***** ***** *\n', '*  2 *   ** *F*\n', '* ** ***  F   *\n', '* 1********F  *\n', '*************Y*\n']
    assert read_lines('tests_use_board/board_hard.txt') == expected, 'Test readline: Complex board test case False'
    print('Test readline: Complex board test case pass')

def test_readline_empty_file():
    expected = []
    # Test with empty file. (edge case)
    assert read_lines('tests_use_board/empty_board.txt') == expected, 'Test readline: Empty board test case False'
    print( 'Test readline: Empty board test case pass')


def test_parse_simple():
    line = read_lines('tests_use_board/board_simple.txt')
    expected = [['Wall', 'Wall', 'Start', 'Wall', 'Wall'], 
    ['Wall', 'Air', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Wall', 'End', 'Wall', 'Wall']]

    parse_line = parse(line)
    # Find each cells's type in the grid
    parse_line_type = find_parse_type(parse_line)
    
    # Test cell's type in the grid
    assert parse_line_type == expected, 'Test parse: Simple board test case False'
    print('Test parse: Simple board test case pass')

def test_parse_complex():
    line = read_lines('tests_use_board/board_hard.txt')
    expected = [['Wall', 'Start', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall'], 
    ['Wall','Air', 'Air', 'Air', 'Air', 'Air', 'Air', 'Air', 'Teleport_2', 'Air', 'Wall', 'Air', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Air', 'Wall','Wall', 'Wall', 'Air', 'Wall', 'Wall', 'Air', 'Wall', 'Wall', 'Wall', 'Wall', 'Air', 'Wall'], 
    ['Wall', 'Air', 'Wall', 'Air', 'Air', 'Water', 'Wall', 'Air', 'Air', 'Air', 'Teleport_1', 'Air', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Air', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Air', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Air', 'Wall'], 
    ['Wall', 'Air', 'Air', 'Teleport_2', 'Air', 'Wall', 'Air', 'Air', 'Air', 'Wall', 'Wall', 'Air', 'Wall', 'Fire', 'Wall'], 
    ['Wall', 'Air', 'Wall', 'Wall', 'Air', 'Wall', 'Wall', 'Wall', 'Air', 'Air', 'Fire', 'Air', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Air', 'Teleport_1', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Fire', 'Air', 'Air', 'Wall'], 
    ['Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'Wall', 'End', 'Wall']]

    parse_line = parse(line)
    parse_line_type = find_parse_type(parse_line)
    
    # Test cells' type in a complex grid
    assert parse_line_type == expected, 'Test parse: Complex board test case False'
    print('Test parse: Complex board test case pass')

def test_parse_empty_file():
    line = read_lines('tests_use_board/empty_board.txt')

    expected = ValueError('Expected 1 starting position, got 0.')

    false_massage = ('Test parse: Empty board test case Flase')
    try:
        parse(lines)
    except ValueError as e:                        # Check function raise correct error for empty file.
        assert str(e) == str(expected) , false_massage
        print('Test parse: Empty board test case pass')
    except Exception:
        print(false_massage)

def test_parse_badletter():
    line = read_lines('tests_use_board/badletter_board.txt')

    expected = ValueError('Bad letter in configuration file: B.')

    false_massage = ('Test parse: Bad letter test case False')
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for unknow letter on the board.
        assert str(e) == str(expected), false_massage
        print('Test parse: Bad letter test case pass')
    except Exception:
        print(false_massage)

def test_parse_no_starting_point():
    line = read_lines('tests_use_board/no_starting_board.txt')

    expected = ValueError('Expected 1 starting position, got 0.')

    false_massage = 'Test parse: No starting point test case False'
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for no starting point on the board.
        assert str(e) == str(expected), false_massage
        print('Test parse: No starting point test case pass')
    except Exception:
        print(false_massage)

def test_parse_many_starting_point():
    line = read_lines('tests_use_board/many_starting_board.txt')

    expected = ValueError('Expected 1 starting position, got 2.')

    false_massage = 'Test parse: More than 1 starting point test case False'
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for more than 1 starting point on the board.
        assert str(e) == str(expected), false_massage     
        print('Test parse: More than 1 starting point test case pass')
    except Exception:
        print(false_massage)

def test_parse_no_end_point():
    line = read_lines('tests_use_board/no_end_board.txt')

    expected = ValueError('Expected 1 ending position, got 0.')

    false_massage = 'Test parse: No End point test case False'
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for no end point on the board.
        assert str(e) == str(expected), false_massage
        print('Test parse: No End point test case pass')
    except Exception:
        print(false_massage)

def test_parse_many_end_point():
    line = read_lines('tests_use_board/many_end_board.txt')

    expected = ValueError('Expected 1 ending position, got 2.')

    false_massage = 'Test parse: More than 1 End point test case False'
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for more than 1 end point on the board.
        assert str(e) == str(expected), false_massage
        print('Test parse: More than 1 End point test case pass')
    except Exception:
        print(false_massage)

def test_parse_no_match_teleport():
    line = read_lines('tests_use_board/no_match_teleport_board.txt')

    expected = ValueError('Teleport pad 1 does not have an exclusively matching pad.')

    false_massage = 'Test parse: No match teleport test case False'
    try:
        parse(line)
    except ValueError as e:         # Check function raise correct error for teleport not in pair.
        assert str(e)==str(expected), false_massage
        print('Test parse: No match teleport test case pass')
    except Exception:
        print(false_massage)




def run_tests():
    test_readline_simple()
    test_readline_complex()
    test_readline_empty_file()
    test_parse_simple()
    test_parse_complex()
    test_parse_empty_file()
    test_parse_badletter()
    test_parse_no_starting_point()
    test_parse_many_starting_point()
    test_parse_no_end_point()
    test_parse_many_end_point()
    test_parse_no_match_teleport()


