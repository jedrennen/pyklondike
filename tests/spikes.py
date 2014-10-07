import random

class Card(object):

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.facing_up = False

	def is_face_up(self):
		return self.facing_up

	def flip(self):
		self.facing_up = not self.facing_up

	def add_to_pile(self, pile_index, position_index):
		self.pile_index = pile_index
		self.position_index = position_index

	def remove_from_pile(self):
		pile = (self.pile_index, self.position_index)
		self.pile_index = -1
		self.position_index = -1
		return pile

	def get_pile(self):
		return (self.pile_index, self.position_index)

	def __str__(self):
		return "%r%r" % (self.rank, self.suit)

	def __eq__(self, other):
		if isinstance(other, Card):
			return (self.suit == other.suit and self.rank == other.rank)
		return NotImplemented

	def __ne__(self, other):
		result = self.__eq__(other)
		if result is NotImplemented:
			return result
		return not result

class Game(object):
	suits = ['s', 'h', 'c', 'd']
	ranks = ['A', '2', '3', '4', '5', '6', '7', 
		'8', '9', '0', 'J', 'Q', 'K']
	cards = []
	deck = [];

	def __init__(self):
		for i, suit in enumerate(suits):
			for j, rank in enumerate(ranks):
				cards.append(Card(suit, rank))
		suffle_deck(self)

	def find_card_index(suit, rank):
		return cards.index(Card(suit, rank))

	def set_card_pile(suit, rank, pile_index, position_index):
		card_index = cards.index(Card(suit, rank))
		cards[card_index].add_to_pile(pile_index, position_index)

	def suffle_deck(self):
		temp_deck = []
		for card in cards:
			temp_deck.append(card)

		for i in enumerate(cards):
			rand_index = random.randrange(0, len(temp_deck))
			card = temp_deck.pop(rand_index)
			deck.append(card)
			set_card_pile(card.suit, card.rank, 0, len(deck) - 1)

		for i in range(0, len(cards)):
			card = cards[i]
			pile_index, position_index = card.get_pile()

			print "card[%s]: %s%s, Location: (Pile: %s, Pos: %s)" % (
				i, card.rank, card.suit, pile_index, position_index)

game = Game()