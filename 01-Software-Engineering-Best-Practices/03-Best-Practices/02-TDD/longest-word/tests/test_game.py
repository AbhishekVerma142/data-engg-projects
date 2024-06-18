import string
from longest_word.game import Game

class TestGame:
    def test_game_initialization(self):
        '''
        setup
        exercise
        verify
        teardown
        '''
        new_game = Game()
        grid = new_game.grid
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        '''
        Testing empty word is invalid
        '''
        new_game = Game()
        assert new_game.is_valid("") is False

    def test_is_valid(self):
        '''
        Is Valid Scenario
        '''
        new_game = Game()
        new_game.grid = list("QWERTYKEY")
        assert new_game.is_valid("QWERTY") is True
        assert new_game.grid == list(
            "QWERTYKEY"
        )

    def test_is_invalid(self):
        '''
        Is invalid scenario
        '''
        new_game = Game()
        new_game.grid = list("QWERTYKEY")
        assert new_game.is_valid("QUEEN") is False
        assert new_game.grid == list(
            "QWERTYKEY"
        )
