from nose.tools import *
import sys
from StringIO import StringIO
from PyKlondike.game import Game
from PyKlondike.cardPile import CardPile
from PyKlondike.playingCard import PlayingCard
#from PyKlondike.main import *

def foo(out=sys.stdout):
	out.write("hello")

def setup():
	pass

def test_std_output():
	out = StringIO()
	foo(out = out)
	output = out.getvalue().strip()
	assert_equal(output, "hello")

#
#def foo(out=sys.stdout):
#    out.write("hello, world!")
#Then the test is much simpler:
#
#def test_foo():
#    from foomodule import foo
#    from StringIO import StringIO
#
#    out = StringIO()
#    foo(out=out)
#    output = out.getvalue().strip()
#   assert output == 'hello world!'

@nottest
def test_new_game_prints_board():
	new_board = """
24--- \033[31;40m|___|\033[0m       \033[37;40m|___|\033[0m \033[37;40m|___|\033[0m \033[37;40m|___|\033[0m \033[37;40m|___|\033[0m

0---- 1---- 2---- 3---- 4---- 5---- 6----
\033[31;47m K d \033[0m \033[31;47m 6 d \033[0m \033[30;47m K c \033[0m \033[30;47m 8 c \033[0m \033[30;47m 4 c \033[0m \033[30;47m A c \033[0m \033[31;47m Q h \033[0m

"""
	out = StringIO()
	game = Game(out=out, no_shuffle=True)
	slice_start = 0
	slice_end = min((slice_start + 9), len(new_board))

	game.deal()
	output = out.getvalue()

#	assert_equal(output[slice_start:slice_end], 
#		new_board[slice_start:slice_end])


@nottest
def test_deal():
	out = StringIO()
	game = Game(out=out, no_shuffle=True)
	game.deal()

	assert_equal(13, len(game.piles))
	assert_equal(24, len(game.piles[0]))
	for i, pile in enumerate(game.piles[1:6]):
		assert_equal(0, len(pile))
	for i, pile in enumerate(game.piles[6:]):
		assert_equal(i + 1, len(pile))


@nottest
def test_draw_flips_one_card_from_draw_pile_to_discard_pile():
	out = StringIO()
	game = Game(out=out, no_shuffle=True)
	game.deal()
	expected_draw_pile_size = len(game.piles[0]) - 1

	game.draw()

	assert_equal(expected_draw_pile_size, len(game.piles[0]))
	assert_equal(1, len(game.piles[1]))
	assert_true(game.piles[1][0].is_face_up())


@nottest
def test_quit_ends_game():
	out = StringIO()
	game = Game(out=out, no_shuffle=True)
	game.deal()

	game.quit()
	output = out.getvalue()[-22:]

	assert_equal(0, len(game.piles))
#	assert_equal(output, "\n\tThanks for Playing!\n")


@nottest
def test_draw_non_table_pile_with_no_face_up_cards():
	pile = CardPile()
	cards = [PlayingCard('A', 's'), PlayingCard(2, 's'), PlayingCard(3, 's')]
	for card in cards:
		pile.append(card)

	result = draw_non_table_pile(pile)

	assert_equal('3---', result)


@nottest
def test_draw_non_table_pile_with_ace_up_card():
	pile = CardPile()
	cards = [PlayingCard('A', 's'), PlayingCard(2, 's'), PlayingCard(3, 's')]
	for card in cards:
		card.flip()
		pile.append(card)

	result = draw_non_table_pile(pile)

	assert_equal('\033[30;47m 3 s \033[0m', result)


@nottest
def test_draw_non_table_pile_with_empty_pile():
	pile = CardPile()

	result = draw_non_table_pile(pile)

	assert_equal('\033[37;40m|___|\033[0m', result)


@nottest
def test_draw_card():
	cards = [PlayingCard('A', 's'), PlayingCard(0, 'h')]

	result = draw_card(cards[0])
	assert_equal('\033[30;47m A s \033[0m', result)

	result = draw_card(cards[1])
	assert_equal('\033[31;47m 0 h \033[0m', result)


@nottest
def test_draw_table_pile_summary_row():
	card = PlayingCard('A', 's')
	card1 = PlayingCard(2, 's')
	card1.flip()
	pile0 = TablePile()
	pile1 = TablePile()
	pile1.append(card)
	pile2 = TablePile()
	pile2.append(card)
	pile2.append(card1)
	piles = [pile0, pile1, pile2, pile0, pile1, pile2, pile0]

	result = draw_table_pile_summary_row(piles)

	assert_equal('0---- 1---- 1---- 0---- 1---- 1---- 0----', result)


@nottest
def test_draw_table_pile_row():
	card = PlayingCard('A', 's')
	card1 = PlayingCard(2, 's')
	card1.flip()
	pile0 = TablePile()
	pile1 = TablePile()
	pile1.append(card)
	pile2 = TablePile()
	pile2.append(card)
	pile2.append(card1)
	piles = [pile0, pile1, pile2, pile0, pile1, pile2, pile0]

	result = draw_table_pile_row(piles, 0)

	assert_equal('            \033[30;47m 2 s \033[0m             \033[30;47m 2 s \033[0m      ', result)
















