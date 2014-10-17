from django.test import TestCase
from ..models import Card, Player, WarGame
from factories import WarGameFactory


class ModelTestCase(TestCase):
    def setUp(self):
        self.card = Card.objects.create(suit=Card.CLUB, rank="jack")
        self.my_card = Card.objects.create(suit=Card.CLUB, rank="jack")
        self.my_second_card = Card.objects.create(suit=Card.CLUB, rank="king")
        self.my_third_card = Card.objects.create(suit=Card.CLUB, rank="three")

    def test_get_ranking(self):
        """Test that we get the proper ranking for a card"""
        self.assertEqual(self.card.get_ranking(), 11)

    def test_get_war_result(self):
        """Test that we get the proper results for war game"""
        self.assertEqual(self.card.get_war_result(self.my_card), 0)
        self.assertEqual(self.card.get_war_result(self.my_second_card), -1)
        self.assertEqual(self.card.get_war_result(self.my_third_card), 1)

    def create_war_game(self, user, result=WarGame.LOSS):
        WarGame.objects.create(result=result, player=user)

    def test_get_losses(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        self.assertEqual(user.get_losses(), 3)

    def test_get_ties(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
        self.assertEqual(user.get_ties(), 4)

    def test_get_record_display(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
        self.assertEqual(user.get_record_display(), "2-3-4")

            # def test_badges(self):
            #     user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
            #     wins = 0
            #     while wins <= 5:
            #         self.create_war_game(user, WarGame.LOSS)
            #         wins += 1
            #     self.assertEqual(get_badges(user), 1)



