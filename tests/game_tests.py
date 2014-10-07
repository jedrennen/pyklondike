from nose.tools import *
import sys
from StringIO import StringIO
from PyKlondike.game import Game
from PyKlondike.cardPile import CardPile
from PyKlondike.playingCard import PlayingCard

def test_move_card_with_valid_move_of_ace_to_suit_pile():
	game = Game(no_shuffle=True)
	game.deal()

	game.move_card('ac')

	assert_equal(1, len(game.piles[2]))
	assert_equal(5, len(game.piles[11]))
	card = game.piles[2][0]
	assert_true(card.is_face_up())
	assert_equal(2, card.pile_number)
	assert_equal(0, card.pile_index)


def test_deal_sets_card_pile_numbers():
	game = Game(no_shuffle=True)

	game.deal()

	for i, pile in enumerate(game.piles):
		for j, card in enumerate(pile._cards):
			assert_equal(i, card.pile_number)
			assert_equal(j, card.pile_index)

def test_move_card_throws_error_for_non_facing_up_card():
	game = Game(no_shuffle=True)
	game.deal()

	with assert_raises(ValueError):
		game.move_card('as')


def test_draw_on_empty_pile_flips_discard_pile_to_draw_pile():
	game = Game(no_shuffle=True)
	card = PlayingCard('A', 's')
	card.flip()
	game.piles[1].add_card(card)

	game.draw()

	assert_equal(1, len(game.piles[0]))
	assert_equal(0, len(game.piles[1]))


def test_move_with_only_non_ace_throws_error():
	game = Game(no_shuffle=True)
	game.deal()

	with assert_raises(ValueError):
		game.move_card('6d')


def test_move_with_non_top_ace_throws_error():
	game = Game(no_shuffle=True)
	game.deal()
	game.draw()
	game.draw()

	with assert_raises(ValueError):
		game.move_card('as')


def test_move_with_king_to_empty_table_pile():
	game = Game(no_shuffle=True)
	card = game.cards[12]
	card.pile_number = 1
	card.pile_index = 0
	game.piles[1].add_card(card)

	game.move_card('ks')

	assert_equal(0, len(game.piles[1]))
	assert_equal(1, len(game.piles[6]))
	top_card = game.piles[6].top()
	assert_equal(card, top_card)


def test_move_invalid_card_suit_raises_error():
	game = Game(no_shuffle=True)
	card_to_move = game.cards[0]
	card_to_move.pile_number = 1
	card_to_move.pile_index = 0
	game.piles[1].add_card(card_to_move)

	card_on_stack = game.cards[1]
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 0
	game.piles[6].add_card(card_on_stack)

	with assert_raises(ValueError):
		game.move_card('as', '2s')


def test_move_invalid_card_rank_raises_error():
	game = Game(no_shuffle=True)
	card_to_move = game.cards[0]
	card_to_move.pile_number = 1
	card_to_move.pile_index = 0
	game.piles[1].add_card(card_to_move)

	card_on_stack = game.cards[15]
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 0
	game.piles[6].add_card(card_on_stack)

	with assert_raises(ValueError):
		game.move_card('as', '3h')


def test_move_to_covered_card_raises_error():
	game = Game(no_shuffle=True)
	card_to_move = game.cards[0]
	card_to_move.pile_number = 1
	card_to_move.pile_index = 0
	game.piles[1].add_card(card_to_move)

	card_on_stack = game.cards[14]
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 0
	game.piles[6].add_card(card_on_stack)
	card_on_stack = game.cards[26]
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 1
	game.piles[6].add_card(card_on_stack)

	with assert_raises(ValueError):
		game.move_card('as', '2h')


def test_move_single_card():
	game = Game(no_shuffle=True)
	card_to_move = game.cards[0]
	card_to_move.pile_number = 1
	card_to_move.pile_index = 0
	game.piles[1].add_card(card_to_move)

	card_on_stack = game.cards[14]
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 0
	game.piles[6].add_card(card_on_stack)

	game.move_card('as', '2h')

	assert_equal(0, len(game.piles[1]))
	assert_equal(2, len(game.piles[6]))


def test_move_stack():
	game = Game(no_shuffle=True)
	card_to_move = game.cards[14]
	card_to_move.flip()
	card_to_move.pile_number = 7
	card_to_move.pile_index = 0
	game.piles[7].add_card(card_to_move)
	card_to_move = game.cards[0]
	card_to_move.flip()
	card_to_move.pile_number = 7
	card_to_move.pile_index = 1
	game.piles[7].add_card(card_to_move)

	card_on_stack = game.cards[2]
	card_to_move.flip()
	card_on_stack.pile_number = 6
	card_on_stack.pile_index = 0
	game.piles[6].add_card(card_on_stack)

	game.move_card('2h', '3s')

	assert_equal(0, len(game.piles[7]))
	assert_equal(3, len(game.piles[6]))


def test_won_true_for_winner():
	game = Game(no_shuffle=True)

	for i, card in enumerate(game.cards):
		game.piles[(i / 13) + 2].add_card(card)

	assert_true(game.won())


def test_won_false_for_non_winner():
	game = Game(no_shuffle=True)
	game.deal()

	assert_false(game.won())

















