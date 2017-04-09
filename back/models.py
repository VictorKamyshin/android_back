from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Words(models.Model):
    eng_word = models.CharField(max_length=255, verbose_name=u'English word', null=False, unique=True)
    rus_word = models.CharField(max_length=255, verbose_name=u'Russian word', null=False)

    def json_format(self):
        return {'word': self.eng_word, 'translation': self.rus_word}


class Decks(models.Model):
    code = models.CharField(max_length=8, verbose_name=u'Link code for deck', null=True)
    name = models.CharField(max_length=255, verbose_name=u'Deck name', null=False, unique=True)

    def json_format(self):
        return {'code': self.code, 'name': self.name, 'size': DecksContent.objects.filter(deck=self).count()}


class DecksContent(models.Model):
    word = models.ForeignKey(Words, on_delete=models.CASCADE, verbose_name=u'Single word in deck',
                            related_name=u'word_in_deck', default=None)
    deck = models.ForeignKey(Decks, on_delete=models.CASCADE, verbose_name=u'Deck, containing the word',
                             related_name=u'deck_with_word', default=None)
