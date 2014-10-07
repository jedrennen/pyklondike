from playingCard import PlayingCard
from cardPile import CardPile

class SuitPile(CardPile):
	def __init__(self):
		super(SuitPile, self).__init__()

	def can_take(self, card):
		if self.is_empty():
			return card.rank == 'A'

		top_card = self.top()
		return (top_card.suit == card.suit and
			(top_card.rank_number + 1) == card.rank_number)