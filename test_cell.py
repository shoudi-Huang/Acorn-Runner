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
from game import Game

def test_cell_Start():
    start = Start()  # Create cell
    assert start.display == 'X', 'Test cell: Start test case False' # Check cell's display
    print('Test cell: Start test case pass')

def test_cell_End():
    end = End()
    false_massage = 'Test cell: End test case False'
    assert end.display == 'Y', false_massage

    game = Game('board_simple.txt')
    end.step(game)                  # Step into End.

    assert game.win == True, false_massage   # Check did End's step function change game state to win.
    print('Test cell: End test case pass')

def test_cell_Air():
    air = Air()
    assert air.display == ' ', 'Test cell: Air test case False'
    print('Test cell: Air test case pass')

def test_cell_wall():
    wall = Wall()
    false_massage = 'Test cell: Wall test case False'
    assert wall.display == '*', false_massage
    print('Test cell: Wall test case pass')

def test_cell_fire():
    fire = Fire()
    assert fire.display == 'F', 'Test cell: Fire test case False'
    print('Test cell: Fire test case pass')

def test_cell_water():
    water = Water()
    assert water.display == 'W', 'Test cell: Water test case False'
    print('Test cell: Water test case pass')

def test_cell_teleport_1():
    teleport = Teleport_1()
    assert teleport.display == '1', 'Test cell: Teleport 1 test case False'
    print('Test cell: Teleport 1 test case pass')

def test_cell_teleport_2():
    teleport = Teleport_2()
    assert teleport.display == '2', 'Test cell: Teleport 2 test case False'
    print('Test cell: Teleport 2 test case pass')




def run_tests():
    test_cell_Start()
    test_cell_End()
    test_cell_Air()
    test_cell_wall()
    test_cell_fire()
    test_cell_water()
    test_cell_teleport_1()
    test_cell_teleport_2()



