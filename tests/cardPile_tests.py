from nose.tools import *
from PyKlondike.playingCard import PlayingCard
from PyKlondike.cardPile import CardPile

def test_push_and_get_card():
	card = PlayingCard('A', 's')
	pile = CardPile()
	pile.add_card(card)

	assert_equal(1, len(pile))
	assert_equal(card.suit, pile[0].suit)
	assert_equal(card.rank, pile[0].rank)

def test_get_count_facing_up():
	cards = [PlayingCard('A', 's'), PlayingCard(3, 's'), PlayingCard(2, 'h')]
	cards[1].flip()
	cards[2].flip()
	pile = CardPile()

	for card in cards:
		pile.add_card(card)

	assert_equal(2, pile.count_facing_up())

def test_get_count_facing_down():
	cards = [PlayingCard('A', 's'), PlayingCard(3, 's'), PlayingCard(2, 'h')]
	cards[2].flip()
	pile = CardPile()

	for card in cards:
		pile.add_card(card)

	assert_equal(2, pile.count_facing_down())

def test_clear():
	cards = [PlayingCard('A', 's'), PlayingCard(3, 's'), PlayingCard(2, 'h')]
	cards[2].flip()
	piles = [CardPile(), CardPile(), CardPile()]

	for pile in piles:
		for card in cards:
			pile.add_card(card)

	for pile in piles:
		pile.clear()
		assert_equal(0, len(pile))

def test_can_take_returns_false():
	pile = CardPile()
	card = PlayingCard('A', 's')

	result = pile.can_take(card)

	assert_false(result)


def test_top_returns_last_card_without_removing():
	card = PlayingCard('A', 's')
	pile = CardPile()
	pile.add_card(card)

	result = pile.top()

	assert_equal(1, len(pile))
	assert_equal(card.suit, result.suit)
	assert_equal(card.rank, result.rank)

def test_is_empty():
	pile = CardPile()

	assert_true(pile.is_empty())

	pile.add_card(PlayingCard('A', 's'))
	assert_false(pile.is_empty())

def test_pop_returns_last_card_and_removes_it():
	card = PlayingCard('A', 's')
	pile = CardPile()
	pile.add_card(card)

	result = pile.pop()

	assert_equal(0, len(pile))
	assert_equal(card.suit, result.suit)
	assert_equal(card.rank, result.rank)






