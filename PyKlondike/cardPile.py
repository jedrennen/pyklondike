from playingCard import PlayingCard

class CardPile(object):
	def __init__(self):
		self._cards = []

	def add_card(self, new_card):
		if not isinstance(new_card, PlayingCard):
			raise ValueError("Must be a playing card")
		self._cards.append(new_card)

	def __getitem__(self, index):
		return self._cards[index]

	def __len__(self):
		return len(self._cards)

	def pop(self):
		return self._cards.pop()

	#def __getslice__(self, i, j):
	#	return self.__getitem__(slice(i, j))

	def count_facing_up(self):
		num_face_up = 0
		for i in range(len(self._cards), 0, -1):
			if self._cards[i-1].is_face_up():
				num_face_up += 1
			else:
				break;
		return num_face_up

	def count_facing_down(self):
		return len(self._cards) - self.count_facing_up()

	def clear(self):
		self._cards = []

	def can_take(self, card):
		return False

	def top(self):
		return self._cards[-1]

	def is_empty(self):
		return len(self._cards) == 0