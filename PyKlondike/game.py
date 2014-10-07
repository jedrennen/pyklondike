from sys import stdout
from playingCard import PlayingCard
from cardPile import CardPile
from tablePile import TablePile
from drawPile import DrawPile
from discardPile import DiscardPile
from suitPile import SuitPile

class Game(object):
	suits = ['s', 'h', 'c', 'd']
	ranks = ['A', '2', '3', '4', '5', '6', '7', 
		'8', '9', '0', 'J', 'Q', 'K']
	cards = []
	piles = []

	def __init__(self, out=stdout, no_shuffle=False):
		self.out = out
		self._shuffle = not no_shuffle
		#self.table_piles = [TablePile() for _ in range(7)]

		self._seed_cards()
		self._seed_piles()

	def _seed_cards(self):
		self.cards = []
		for i, suit in enumerate(self.suits):
			for j, rank in enumerate(self.ranks):
				self.cards.append(PlayingCard(rank, suit))

	def _seed_piles(self):
		self.piles = []
		self.piles = [DrawPile(), DiscardPile()]
		for i in range(0,4):
			self.piles.append(SuitPile())
		for i in range(0, 7):
			self.piles.append(TablePile())

	def draw(self):
		if self.piles[0].is_empty():
			while not self.piles[1].is_empty():
				card = self.piles[1].pop()
				card.flip()
				self.piles[0].add_card(card)
		else: 
			card = self.piles[0].pop()
			card.pile_number = 1
			card.pile_index = len(self.piles[1])
			self.piles[1].add_card(card)
			if not card.is_face_up():
				card.flip()

	def quit(self):
		self.piles = []
		self.cards = []

	def deal(self):
		for pile in self.piles:
			pile.clear()
		self._seed_cards()
		self._seed_piles()

		z = 0
		j = 0
		for i in range(0, 28):
			pile_index = 6 + j
			card = self.cards[51 - i]
			if j == z:
				card.flip()	 

			card.pile_number = pile_index
			card.pile_index = len(self.piles[pile_index])
			self.piles[pile_index].add_card(card)
			j += 1
			if pile_index == 12:
				z += 1
				j = z

		for i in range(28, 52):
			card = self.cards[51 - i]
			card.pile_number = 0
			card.pile_index = len(self.piles[0])
			self.piles[0].add_card(card)

	def move_card(self, card_from_str, card_to_str=''):
		card_from_index = self._get_card_index(card_from_str)
		card_from = self.cards[card_from_index]

		if not card_from.is_face_up():
			raise ValueError("Invalid move (hidden card) Pile: %r, Index: %r" % (
				card_from.pile_number, card_from.pile_index))

		if card_to_str == '':

			top_card = self.piles[card_from.pile_number].top()

			if card_from.rank_number == 0 and card_from == top_card:
				for i, pile in enumerate(self.piles[2:6]):
					if pile.can_take(card_from):
						moved_card = self.piles[card_from.pile_number].pop()
						moved_card.pile_index = len(pile)
						moved_card.pile_number = i + 2
						pile.add_card(moved_card)				
						return

			elif card_from.rank_number == 12:
				for i, pile in enumerate(self.piles[6:]):
					if pile.can_take(card_from):
						self._move_cards(card_from.pile_number, card_from.pile_index, i + 6)
						#moved_card = self.piles[card_from.pile_number].pop()
						#moved_card.pile_index = len(pile)
						#moved_card.pile_number = i + 6
						#pile.add_card(moved_card)				
						return

			else:
				raise ValueError("Invalid move (no 'TO' card)")

		else:
			to_card_index = self._get_card_index(card_to_str)
			to_card = self.cards[to_card_index]

			to_pile = self.piles[to_card.pile_number]
			if not to_pile.can_take(card_from):
				raise ValueError("Invalid move (can't take)")
			else:
				self._move_cards(card_from.pile_number, card_from.pile_index, to_card.pile_number)
				return


	def won(self):
		result = False
		for pile in self.piles[2:6]:
			result = (len(pile) == 13)
		return result


	def _get_card_index(self, card):
			rank_index = self.ranks.index(card[0:1].upper())
			suit_index = self.suits.index(card[1:2].lower())
			return 13 * suit_index + rank_index

	def _move_cards(self, from_pile_number, card_index, to_pile_number):
		temp_pile = []

		while len(self.piles[from_pile_number]) > card_index:
			temp_pile.append(self.piles[from_pile_number].pop())

		for i in range(0, len(temp_pile)):
			card = temp_pile.pop()
			card.pile_number = to_pile_number
			card.pile_index = len(self.piles[to_pile_number])
			self.piles[to_pile_number].add_card(card)





















