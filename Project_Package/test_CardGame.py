from unittest import TestCase, mock
from Project_Package.CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        self.test_game = CardGame('sagi', 'adi')
        # Checking the names are right
        self.assertEqual(self.test_game.player1.PlayerName, 'sagi')
        self.assertEqual(self.test_game.player1.PlayerName, 'adi')
        print('setUP')

    def tearDown(self):
        print('tearDown')

    def test_new_game(self):
        # Checks if flag raises once game starts
        self.assertEqual(self.test_game.new_game(), 1)
        # Checks if the second time we try to call the new game function it returns an error
        self.assertEqual(self.test_game.new_game(), "Error, cannot start a new game while you are already in a game.")
        print("The new_game method can only be called once in a run")

    def test_get_winner(self):
        self.test_game.player1.cardList = []  # checking if player 1 does win if his list is shorter
        self.test_game.player2.cardList = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.test_game.get_winner(), self.test_game.player1)
        self.test_game.player1.cardList = []  # checking if players have equal card amount if return None
        self.test_game.player2.cardList = []
        self.assertIsNone(self.test_game.get_winner())  # checks if it returns None while they are both equal
        print("The method get_winner method returns the expected value")
