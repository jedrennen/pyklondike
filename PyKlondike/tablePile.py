from playingCard import PlayingCard
from cardPile import CardPile

class TablePile(CardPile):
	def __init__(self):
		super(TablePile, self).__init__()

	def get_face_up_card(self, index):
		pile_index = self.count_facing_down() + index
		if pile_index >= len(self._cards):
			return None
		else:
			return self._cards[pile_index]

	def pop(self):
		result = super(TablePile, self).pop()
		if len(self._cards) > 0 and self.count_facing_up() == 0:
			self._cards[-1].flip()
		return result

	def can_take(self, card):
		if self.is_empty():
			return card.rank_number == 12

		top_card = self.top()
		return (top_card.rank_number - 1 == card.rank_number and 
			top_card.color != card.color)