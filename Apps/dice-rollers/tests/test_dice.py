from dice_rollers.dice import Dice

class TestDice():
    def test_one_roll(self):
        dice = Dice()
        roll = dice.roll()
        assert type(roll) == int
        assert roll > 0
        assert roll < 7
