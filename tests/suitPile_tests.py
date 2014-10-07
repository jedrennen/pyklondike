from nose.tools import *
from PyKlondike.playingCard import PlayingCard
from PyKlondike.cardPile import CardPile
from PyKlondike.suitPile import SuitPile

def test_can_take_returns_true_if_pile_is_empty_and_card_is_an_ace():
	pile = SuitPile()
	card = PlayingCard('A', 's')

	result = pile.can_take(card)

	assert_true(result)


def test_can_take_returns_false_if_card_is_not_same_suit():
	pile = SuitPile()
	first_card = PlayingCard('A', 's')
	pile.add_card(first_card)
	second_card = PlayingCard(2, 'd')

	result = pile.can_take(second_card)

	assert_false(result)


def test_can_take_false_if_pile_is_empty_and_card_is_not_an_ace():
	pile = SuitPile()
	card = PlayingCard(2, 's')

	result = pile.can_take(card)

	assert_false(result)


def test_can_take_returns_false_if_card_is_not_next_rank():
	pile = SuitPile()
	first_card = PlayingCard('A', 's')
	pile.add_card(first_card)
	second_card = PlayingCard(3, 's')

	result = pile.can_take(second_card)

	assert_false(result)


def test_can_take_returns_true_if_card_is_same_suit_and_next_rank():
	pile = SuitPile()
	first_card = PlayingCard('A', 's')
	pile.add_card(first_card)
	second_card = PlayingCard(2, 's')

	result = pile.can_take(second_card)

	assert_true(result)






















