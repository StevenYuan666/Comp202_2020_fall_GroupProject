# Three Thirteen Card Game
Three Thirteen is a rummy variant for two or more players (we will play with four or more). It uses two decks of 52 playing cards (104 in total). (The following rules have been adapted from https://www.pagat. com/rummy/3- 13.html.)

The game has eleven rounds. In the first round, three cards are dealt to each player; in the second round, four cards are dealt; this continues until the last round where thirteen cards are dealt to each player. The remainder of the cards in each round are placed face down in a pile called the stock. The top card of the stock is flipped face up and put in a separate pile called the discard pile.

The object of the game is to arrange all the cards in your hand into combinations. There are two types of combinations.

• a group of three or more cards of the same rank, such as Five of Hearts, Five of Clubs, Five of Spades. It is possible for a set to contain identical cards as we are playing with more than one deck (such as Six of Clubs, Six of Clubs, Six of Hearts).

• a sequence of three or more cards of the same suit with consecutive rank, such as Five of Hearts, Six of Hearts, Seven of Hearts.
Combinations can contain more than three cards (such as four sevens, or the 8-9-10-Jack-Queen of Clubs). However, you cannot count the same card as part of more than one combination. If the Five of Spades is included in a group, it cannot be included in a sequence (unless there are two Five of Spades in your hand).

Aces rank high in this game, so Q-K-A of a suit is a valid sequence, but A-2-3 is not.

In each round there is a wildcard rank. It is the rank equal to the number of cards dealt that round. For example, in round 1, where three cards are dealt to each player, all Three’s are wild cards. In round 8, Ten’s are wild cards; in round 9, 10 and 11, Jacks, Queens, and Kings are wild, respectively.

A wildcard can be included into any group or sequence. For example, if the wildcard rank is King, and the hand currently contains a Two of Hearts, Two of Clubs and King of Hearts, then these three cards can be put into a group, because the King can stand in for another Two. Or, if the wildcard rank is Seven, and the hand contains a Two of Hearts, Four of Hearts and Seven of Spades, then these three cards can be put into a group, because the Seven can stand in for the Three of Hearts. Note that we are providing you with updated is_valid_group and is_valid_sequence functions that recognize groups/sequences that contain wildcards.

The starting player of the first round is chosen randomly. Players take turns clockwise around the table. A turn consists of drawing one card (either the top card of the face down stock pile, or the top card of the discard pile), and then discarding one card to the top of the discard pile. In each successive round, the starting player will be the player to the right of the previous starting player.

A player can finish the round (also known as ‘going out’) if, after drawing, they are able to arrange all the cards in their hand except one into separate groups/sequences, and then discard the final card. Each of the other players is then allowed one more turn. When they finish and it is the winning player’s turn again, the round ends and the round scores are calculated.

At the end of a round, each player arranges as much of their hand as possible into groups and sequences. Any cards that they cannot include in a group or sequence are counted as penalty points against them. An Ace is 1 penalty point; Twos through Tens are their numeric value; and Jacks, Queens and Kings are 10 penalty points each.

These scores are accumulated from round to round. Whoever has the lowest score (the lowest amount of penalty points) at the end of the eleventh round is the winner.
