import factory
from ..models import Player, WarGame


class WarGameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.WarGame'
    result = WarGame.TIE

class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.Player'
        #django_get_or_create = ('username', 'password', 'email')
    #email = factory.lazy_attribute(lambda o:'%s@gmail.com' % (o.username))
    #username = 'test_user'
    #password = 'password'
    #email = 'test_user@web.de'
