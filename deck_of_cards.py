import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def show_card(self):
        print('{} of {}'.format(self.value, self.suit))

class Deck():

    def __init__(self):
        self.card_list = []
        self.construct_deck()


    def construct_deck(self):
        for s in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for v in ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.card_list.append(Card(v,s))

    def show_deck(self):
        for card in self.card_list:
            card.show_card()

    # def show_playing_pile(self):
    #     for card in self._playing_pile:
    #         card.show_card()

    # def show_discard_pile(self):
    #     for card in self._discard_pile:
    #         card.show_card()

    def shuffle_deck(self):
        random.shuffle(self.card_list)

    def draw_card_from_deck(self):
        return self.card_list.pop()

    # def return_card_to_deck(self):
    #     self._return_to_deck = self.card_list.append(self._draw_from_deck)
    #     return self._return_to_deck

    # def put_card_in_playing_pile(self):
    #     self._put_in_playing_pile = self._playing_pile.append(self._draw_from_deck)
    #     return self._put_in_playing_pile

    # def put_card_in_discard_pile(self):
    #     self._put_in_discard_pile = self._discard_pile.append(self._draw_from_deck)
    #     return self._put_in_discard_pile

class Hand():
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card_from_deck())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show_card()

my_deck = Deck()
my_deck.shuffle_deck()
hand = Hand()

hand.draw(my_deck).draw(my_deck)
for i in range(3):
    hand.draw(my_deck)

hand.show_hand()

# print('The deck has {} cards'.format(len(hand)))
# print('The top card is the {} of {}'.format(Card[0].v, Card[0].s))
# class Player(Deck):

#     def __init__(self, name):
#         self.name = name
#         self._players_hand = []

#     def player_draws_card_from_deck(self, deck):
#         self._players_hand.append(deck.draw_card_from_deck())

#     def player_returns_card_from_hand_to_deck(self, deck):
#         self.card_list.append(self._players_hand.pop())

#     def player_returns_card_from_playing_pile_to_deck(self, deck):
#         self.card_list.append(self._playing_pile.pop())

#     def player_returns_card_from_discard_pile_to_deck(self, deck):
#         self.card_list.append(self._discard_pile.pop())

#     def show_players_hand(self):
#         for card in self._players_hand:
#             card.show_card()


# player1 = Player("Bob")
# player2 = Player("Jim")

# deck = Deck(shuffled=true) # deck used by all players
# discard_pile = Deck()

# player1.draw_from(hand_size=5, deck)
# discard_pile.add(player1.hand())
# player2.draw_from(hand_size=5, deck)
# discard_pile.add(plater2.hand())
