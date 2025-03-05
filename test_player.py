from player import Player

def test_player_initial_attribute():
    player = Player(0, 1)        # Create a player
    false_massage = 'Test player: Initial attribute test case False'
    expected_massage = 'Please enter a valid move (w, a, s, d, e, q).'
    assert player.display == 'A', false_massage
    assert player.num_water_buckets == 0, false_massage    # Check player's initial number of water bucket
    assert [player.row, player.col] == [0, 1], false_massage    # Check Do player in the correct initial position 
    assert player.invalid_input_massage == expected_massage, false_massage   # Check invalid massage is valid
    print('Test player: Initial attribute test case pass')

def test_player_movement():
    player = Player(0, 1)
    player.movement('s')
    false_massage = 'Test player: Move player test case False'
    assert [player.row, player.col] == [1, 1], false_massage      # Check Do player in correct position after move.
    player.movement('d')
    assert [player.row, player.col] == [1, 2], false_massage
    player.movement('w')
    assert [player.row, player.col] == [0, 2], false_massage
    player.movement('a')
    assert [player.row, player.col] == [0, 1], false_massage
    print('Test player: Move player test case pass')

def test_player_add_water():
    player = Player(0, 1)
    false_massage = 'Test player: Water add or subtract test case False '
    
    # Test increase number of water bucket
    player.add_water(1)
    assert player.num_water_buckets == 1, false_massage
    
    # Test decrease number of water bucket
    player.add_water(-1)
    assert player.num_water_buckets == 0, false_massage
    
    # Test decrease number of water bucket to negative: (edge case)
    player.add_water(-1)
    assert player.num_water_buckets == -1, false_massage
    
    # Check do function raise correct error for subtract of add more than 1 water at once
    expected = ValueError('Water can only add or subtract by 1')
    try:
        player.add_water(2)
    except ValueError as e:
        assert str(e) == str(expected), false_massage
    except Exception:
        raise AssertionError(false_massage)
    print('Test player: Water add or subtract test case pass')




def run_tests():
    test_player_initial_attribute()
    test_player_movement()
    test_player_add_water()


