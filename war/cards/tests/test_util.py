from django.test import TestCase
from ..models import Card
from ..utils import create_deck

class UtilTest(TestCase):
    def test_create_deck(self):
        self.assertEqual(Card.objects.count(), 0)
        create_deck()
        self.assertEqual(len(Card.objects.all()), 52)


def my_max(number_one, number_two):
    if number_one >= number_two:
        return number_one
    else:
        return number_two