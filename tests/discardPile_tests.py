from nose.tools import *
from PyKlondike.playingCard import PlayingCard
from PyKlondike.cardPile import CardPile
from PyKlondike.discardPile import DiscardPile

def test_add_card():
	pile = DiscardPile()
	card = PlayingCard('A', 's')

	pile.add_card(card)

	assert_equal(1, len(pile))
	assert_equal(card.suit, pile.top().suit)
	assert_equal(card.rank, pile.top().rank)
	assert_true(pile.top().is_face_up())

def test_can_take_card_always_returns_true():
	pile = DiscardPile()

	assert_true(pile.can_take(PlayingCard('A', 's')))