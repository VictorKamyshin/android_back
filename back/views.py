# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from models import *
import json


def hello_world(request):
    return HttpResponse('Hello World!')


def get_from_db(request):
    words = []
    words = Words.objects.all()
    word = words[1].json_format()
    return HttpResponse(json.dumps(word, 2), content_type='application/json')


def words_list(request):
    words = list(Words.objects.all())
    words_json = []
    for word in words:
        words_json.append(word.json_format())
    return HttpResponse(json.dumps(words_json, 2), content_type='application/json')


def decks_list(request):
    decks = list(Decks.objects.all())
    decks_json = []
    for deck in decks:
        decks_json.append(deck.json_format())
    return HttpResponse(json.dumps(decks_json, 2), content_type='application/json')


def deck_content(request):
    if request.method=='GET':
        deck_name = request.GET.get('deck_name')
        deck = get_object_or_404(Decks, name = deck_name)
        words = list(DecksContent.objects.filter(deck=deck))
        words_json = []
        for word in words:
            words_json.append(word.word.json_format())
        return HttpResponse(json.dumps(words_json, 2), content_type='application/json')
    else:
        return HttpResponseBadRequest('Method not supported')


def fill_db(request):
    word1 = Words.objects.create(eng_word=u'cat', rus_word=u'кот')
    word2 = Words.objects.create(eng_word=u'bird', rus_word=u'птица')
    word3 = Words.objects.create(eng_word=u'dog', rus_word=u'собака')
    deck1 = Decks.objects.create(name=u'Animals')

    DecksContent.objects.create(word=word1, deck=deck1)
    DecksContent.objects.create(word=word2, deck=deck1)
    DecksContent.objects.create(word=word3, deck=deck1)

    word4 = Words.objects.create(eng_word=u'knife', rus_word=u'нож')
    word5 = Words.objects.create(eng_word=u'spoon', rus_word=u'ложка')
    word6 = Words.objects.create(eng_word=u'fork', rus_word=u'вилка')
    deck2 = Decks.objects.create(name=u'Cutlery')

    DecksContent.objects.create(word=word4, deck=deck2)
    DecksContent.objects.create(word=word5, deck=deck2)
    DecksContent.objects.create(word=word6, deck=deck2)

    return HttpResponse('Db filled!')
