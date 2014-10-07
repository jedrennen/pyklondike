from nose.tools import *
from PyKlondike.playingCard import PlayingCard
from PyKlondike.tablePile import TablePile

def test_push_and_get_card():
	card = PlayingCard('A', 's')
	card.flip()
	pile = TablePile()
	pile.add_card(card)

	assert_equal(1, len(pile))
	assert_equal(card.rank, pile[0].rank)
	assert_equal(card.suit, pile[0].suit)


def test_get_face_up_card():
	cards = [PlayingCard('A', 's'), PlayingCard(3, 's'), PlayingCard(2, 'h')]
	cards[1].flip()
	cards[2].flip()
	pile = TablePile()

	for card in cards:
		pile.add_card(card)

	for i in range(0, 1):
		result_card = pile.get_face_up_card(i)
		assert_true(result_card != None)
		assert_true(result_card.is_face_up())
		assert_equal(cards[i+1].rank, result_card.rank)
		assert_equal(cards[i+1].suit, result_card.suit)

	result_card = pile.get_face_up_card(2)
	assert_true(result_card == None)

def test_pop_flips_card_if_last_facing_up():
	cards = [PlayingCard('A', 's'), PlayingCard(3, 's'), PlayingCard(2, 'h')]
	cards[2].flip()
	pile = TablePile()

	for card in cards:
		pile.add_card(card)

	pile.pop()

	assert_true(pile[-1].is_face_up())



def test_can_take_returns_false_if_card_is_same_color():
	pile = TablePile()
	pile.add_card(PlayingCard('K', 's'))

	assert_false(pile.can_take(PlayingCard('Q', 's')))
	assert_false(pile.can_take(PlayingCard('Q', 'c')))



def test_can_take_returns_false_if_card_is_not_next_lower_rank():
	pile = TablePile()
	pile.add_card(PlayingCard('K', 's'))

	assert_false(pile.can_take(PlayingCard('J', 'h')))
	assert_false(pile.can_take(PlayingCard('K', 'h')))



def test_can_take_returns_true_if_card_is_next_lower_rank_and_opposite_color():
	pile = TablePile()
	pile.add_card(PlayingCard('K', 's'))
	pile[-1].flip()

	queen_hearts = PlayingCard('Q', 'h')
	assert_equal(pile.top().rank_number - 1, queen_hearts.rank_number)
	assert_true(pile.top().rank_number - 1 == queen_hearts.rank_number and 
		pile.top().color != queen_hearts.color)
	assert_false(pile.is_empty() and queen_hearts.rank_number == 12)

	assert_true(pile.can_take(queen_hearts))
	assert_true(pile.can_take(PlayingCard('Q', 'd')))

def test_can_take_returns_true_if_card_is_king_and_pile_is_empty():
	pile = TablePile()

	assert_true(pile.can_take(PlayingCard('K', 's')))


def test_can_take_returns_false_if_card_is_not_king_and_pile_is_empty():
	pile = TablePile()

	assert_false(pile.can_take(PlayingCard('Q', 's')))






















