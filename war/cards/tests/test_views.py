from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver

from ..models import Card, Player, WarGame
from ..utils import create_deck
from ..forms import EmailUserCreationForm



class ViewTestCase(TestCase):
    def create_war_game(self, user, result=WarGame.LOSS):
        WarGame.objects.create(result=result, player=user)

    def setUp(self):
        create_deck()

    # def test_home_page(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertIn('<p>Suit: spade, Rank: two</p>', response.content)
    #     self.assertEqual(response.context['cards'].count(), 52)

    def test_faq_page(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('Can I win real money', response.content)

    def test_filters_page(self):
        response = self.client.get(reverse('filters'))
        self.assertIn('Capitalized Suit', response.content)
        self.assertIn('TWO', response.content)
        self.assertIn('THREE', response.content)
        self.assertIn('FOUR', response.content)
        self.assertIn('FIVE', response.content)
        self.assertIn('SIX', response.content)
        self.assertIn('SEVEN', response.content)
        self.assertIn('EIGHT', response.content)
        self.assertEqual(response.context['cards'].count(), 52)

    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(Player.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))

    def test_login_page(self):
        Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        data = { 'username' : 'test-user',
                 'password' : 'password'
                }
        response = self.client.post(reverse('login'), data)
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))


    def test_profile_page(self):
        # Create user and log them in
        password = 'passsword'
        user = Player.objects.create_user(username='test-user', email='test@test.com', password=password)
        self.client.login(username=user.username, password=password)

        # Set up some war game entries
        self.create_war_game(user)
        self.create_war_game(user, WarGame.WIN)

        # Make the url call and check the html and games queryset length
        response = self.client.get(reverse('profile'))
        self.assertInHTML('<p>Your email address is {}</p>'.format(user.email), response.content)
        self.assertEqual(len(response.context['games']), 2)


    # def test_war_page(self):
    #     # Create user and log them in
    #     password = 'passsword'
    #     user = Player.objects.create_user(username='test-user', email='test@test.com', password=password)
    #     self.client.login(username=user.username, password=password)
    #
    #     self.user_card = Card.objects.create(suit=Card.CLUB, rank="jack")
    #     self.dealer_card = Card.objects.create(suit=Card.CLUB, rank="king")
    #     result = self.user_card.get_war_result(self.dealer_card)
    #
    #     response = self.client.post(reverse('login'), data)
    #     self.assertIsInstance(response, HttpResponseRedirect)
    #     self.assertTrue(response.get('location').endswith(reverse('profile')))

#         @login_required()
# def war(request):
#     cards = list(Card.objects.order_by('?'))
#     user_card = cards[0]
#     dealer_card = cards[1]
#
#     result = user_card.get_war_result(dealer_card)
#     WarGame.objects.create(result=result, player=request.user)
#
#     return render(request, 'war.html', {
#         'user_cards': [user_card],
#         'dealer_cards': [dealer_card],
#         'result': result
#     })