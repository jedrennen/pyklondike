from playingCard import PlayingCard
from cardPile import CardPile

class DiscardPile(CardPile):
	def __init__(self):
		super(DiscardPile, self).__init__()

	def add_card(self, card):
		if not card.is_face_up():
			card.flip()
		super(DiscardPile, self).add_card(card)

	def can_take(self, card):
		return True