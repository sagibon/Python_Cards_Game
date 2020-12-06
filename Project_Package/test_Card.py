from unittest import TestCase
from Project_Package.Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("setUp")
        self.card1 = Card(5, 3)
        self.card2 = Card(5, 2)

    def tearDown(self):
        print("tearDown")

    def test_who_higher(self):
        self.card2 = Card(1, 3)
        self.assertEqual(self.card1.who_higher(self.card2), self.card2)
        self.card2 = Card(2, 3)
        self.assertEqual(self.card1.who_higher(self.card2), self.card1)
        self.card1 = Card(1, 2)
        self.assertEqual(self.card1.who_higher(self.card2), self.card1)
        self.card1 = Card(2, 2)
        self.card2 = Card(4, 3)
        self.assertEqual(self.card1.who_higher(self.card2), self.card2)
        self.card1 = Card(4, 4)
        self.assertEqual(self.card1.who_higher(self.card2), self.card1)
        self.card1 = Card(4, 1)
        self.assertEqual(self.card1.who_higher(self.card2), self.card2)
        self.card1 = Card(4, 3)
        self.assertEqual(self.card1.who_higher(self.card2), "tie")
        a = [(1, 1), [1, 1], "1,1", {1: 1}, 11, 1.1]
        for i in a:
            with self.assertRaises(AttributeError):
                self.card1.who_higher(i)
        with self.assertRaises(TypeError):
            self.card1.who_higher()
