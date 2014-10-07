from nose.tools import *
from PyKlondike.playingCard import PlayingCard

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_new_card_has_rank_suit_and_is_face_down():
	card = PlayingCard('A', 's')
	assert_equals(card.rank, 'A')
	assert_equals(card.suit, 's')
	assert_equals(card.is_face_up(), False)

def test_invalid_rank_throws_valueException():
	with assert_raises(ValueError):
		PlayingCard(10, 's')
	with assert_raises(ValueError):
		PlayingCard(1, 's')
	with assert_raises(ValueError):
		PlayingCard('z', 's')

def test_valid_ranks():
	valid_ranks = ['A', '2', '3', '4', '5', '6', '7', 
		'8', '9', '0', 'J', 'Q', 'K']
	for rank in valid_ranks:
		card = PlayingCard(rank, 's')
		assert_equals(card.rank, rank)

def test_rank_stored_as_uppdercase():
	rank = 'a'
	card = PlayingCard(rank, 's')
	assert_equals(card.rank, rank.upper())

def test_invalid_suit_throws_valueExcepiton():
	with assert_raises(ValueError):
		PlayingCard(2, 'z')
	with assert_raises(ValueError):
		PlayingCard(2, 1)

def test_valid_suits():
	valid_suits = ['s', 'h', 'h', 'h']
	for suit in valid_suits:
		card = PlayingCard(2, suit)
		assert_equals(card.suit, suit)

def test_suit_stored_as_lowercase():
	suit = 'S'
	card = PlayingCard(2, suit)
	assert_equals(card.suit, suit.lower())

def test_flip_toggles_card_facing_direction():
	card = PlayingCard(2, 's')

	card.flip()
	assert_true(card.is_face_up())

	card.flip()
	assert_false(card.is_face_up())


def test_rank_index():
	ranks = ['A', '2', '3', '4', '5', '6', '7', 
		'8', '9', '0', 'J', 'Q', 'K']
	cards = []
	for rank in ranks:
		cards.append(PlayingCard(rank, 's'))

	for i, rank in enumerate(ranks):
		card = cards[i]
		assert_equal(i, card.rank_number)


def test_color():
	spade = PlayingCard(2, 's')
	heart = PlayingCard(2, 'h')
	club = PlayingCard(2, 'c')
	diamond = PlayingCard(2, 'd')

	assert_equal('Black', spade.color)
	assert_equal('Black', club.color)
	assert_equal('Red', heart.color)
	assert_equal('Red', diamond.color)




















