from sys import argv
from sys import stdout
from playingCard import PlayingCard
from cardPile import CardPile
from tablePile import TablePile
from discardPile import DiscardPile
from drawPile import DrawPile
from suitPile import SuitPile
from game import Game

_COLOR_RESET = '\033[0m'
_BLACK_CARD_COLOR = '\033[30;47m'
_RED_CARD_COLOR = '\033[31;47m'
_EMPTY_PILE_COLOR = '\033[37;40m'

#class SuitPile(CardPile):
#	def __init__(self):
#		pass

#class DiscardPile(CardPile):
#	def __init__(self):
#		pass

class Controller(object):
	def __init__(self):
		self.table_piles = []
		#for i in (0,7)

class ConsolePrinter(object):
	def __init__(self):
		pass

	def draw_table(self):
		pass


def draw_card(card):
	if card.is_face_up == False:
		return _EMPTY_PILE_COLOR + '-<*>-' + _COLOR_RESET
	elif card.suit == 'c' or card.suit == 's':
		text_color = _BLACK_CARD_COLOR	# Black text on White Background
	else:
		text_color = _RED_CARD_COLOR	# Red text on White Background

	return "%s %s %s %s" % (text_color, card.rank, card.suit, _COLOR_RESET)

def draw_empty_pile():
	return '%s|___|%s' % (_EMPTY_PILE_COLOR, _COLOR_RESET)

def draw_non_table_pile(pile):
	if len(pile) == 0:
		return draw_empty_pile()
	elif pile.count_facing_up() > 0:
		return draw_card(pile[-1])
	else:
		return '%s---' % len(pile)

def draw_table_pile_summary_row(piles):
	result = ''
	for i, pile in enumerate(piles):
		result += '%s----' % pile.count_facing_down()
		if i < 6:
			result += ' '
	return result;

def draw_table_pile_row(piles, row_index):
	result = ''
	for i, pile in enumerate(piles):
		card_to_print = pile.get_face_up_card(row_index)
		if card_to_print == None:
			result += '     '
		else:
			result += draw_card(card_to_print)

		if i < 6:
			result += ' '

	return result

def draw_board(piles, out=stdout):
	table_pile_rows = 0
	for pile in piles[6:13]:
		pile_rows = pile.count_facing_up()
		if pile_rows > table_pile_rows:
			table_pile_rows = pile_rows

	pile_row_output = ''
	for i in range(0, table_pile_rows):
		pile_row_output += draw_table_pile_row(piles[6:13], i)
		pile_row_output += '\n'

	output = """
%s %s       %s %s %s %s

%s
%s

\033[0m""" % (draw_non_table_pile(piles[0]), draw_non_table_pile(piles[1]), 
		draw_non_table_pile(piles[2]), draw_non_table_pile(piles[3]),
		draw_non_table_pile(piles[4]), draw_non_table_pile(piles[5]),
		draw_table_pile_summary_row(piles[6:13]),
		pile_row_output)
	out.write(output)

klondike = Game()
klondike.deal()
continue_game = True

while continue_game:
	if klondike.won():
		print "\n\t CONGRATULATIONS! \n"
		klondike.quit()
		continue_game = False
		continue

	draw_board(klondike.piles)

	command = raw_input('> ')

	if command == 'newcard':
		klondike.draw()

	elif command == 'newgame':
		klondike.quit()
		klondike.deal()

	elif command[0:5] == 'move ' and command[8:10] == 'to' and len(command) == 13:
		try:
			klondike.move_card(command[5:7], command[11:13])
		except ValueError:
			print '\n\tInvalid move\n'

	elif command[0:5] == 'move ' and len(command) == 7:
		try:
			klondike.move_card(command[5:7])
		except ValueError:
			print '\n\tInvalid move\n'

	elif command == 'quit':
		klondike.quit()
		continue_game = False











