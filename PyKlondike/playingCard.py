class PlayingCard(object):
	_valid_ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'j', 'q', 'k']
	_valid_suits = ['s', 'h', 'c', 'd']

	def __init__(self, rank, suit):
		if (len(str(rank)) > 1 or 
			str(rank).lower() not in self._valid_ranks):
			raise ValueError("Invalid playing card rank %s" % rank)
		self._rank = str(rank).upper()

		if (len(str(suit)) > 1 or 
			str(suit).isdigit() or 
			suit.lower() not in self._valid_suits):
			raise ValueError("Invalid plaing card suit %s" % suit)
		self.suit = suit.lower()

		self.is_face_up_flag = False

		self.pile_number = -1
		self.pile_index = -1

	def is_face_up(self):
		return self.is_face_up_flag == True

	def flip(self):
		self.is_face_up_flag = not self.is_face_up_flag

	@property
	def rank(self):
		return self._rank

	@property
	def rank_number(self):
		return self._valid_ranks.index(self._rank.lower())

	@property
	def color(self):
		if self.suit == 's' or self.suit == 'c':
			return 'Black'
		elif self.suit == 'h' or self.suit == 'd':
			return 'Red'
		else:
			raise ValueError("Suit is invalid")