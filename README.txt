//  Python Solitaire v0.01b  
//  
//  by Justin E. Drennen  
//  
//  Klondike solitare game using one draw card at a time.  
//  

Commands:

newgame
	Shuffles deck and redeals a new game of solitaire.

newcard
	Flips a card from the draw pile.  If draw pile is empty, 
	moves discard pile to draw pile and flips top card to the
	discard pile.  Does not shuffle the discard pile when
	moved to back to the draw pile.

move <source_card> [to <destination_card>]
	Moves a card (source_card) or pile to the pile with the
	destination_card on top.  If moving an Ace to a suit pile
	or a King to an empty pile on the table the destination
	card is not necessary.

	source_card and destination_card must be in the following
	format: "rs" (no quotes used) where 'r' stands for the 
	single letter representation  of the card rank (A, 2, 3,
	 4, 5, 6, 7, 8, 9, 1, J, Q, K); 's' stands for the single
	letter representation of the suit (S, H, C, D). The case
	and suit are NOT case specific.

	EXAMPLES:
	move as
		moves the Ace of Spades to an empty suit pile

	move kd
		moves the King of Diamonds to an empty table pile

	move 5h to 6c
		moves the 5 of Hearts (and any card piled on top of
		it) to the 6 of Clubs

quit
	Quits the game.
