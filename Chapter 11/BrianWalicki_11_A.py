# This program is a game of poker where you can play 1 hand,
# then replace some cards in that hand, then prints the hand

import random


class Deck:

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def play_and_replace():
    # Creates a player with its deck of 52
    player = Deck(52)

    # Deals 5 cards for the player
    for i in range(5):
        player.deal()
    print('The cards in play are:', player.cards_in_play_list)

    # Tries to get proper format from user and replaces cards based off
    # what the user specifies
    try:

        # Gets user input
        replace = input('Enter what cards in play are to be replaced '
                        '(separated by commas): ')

        # Cleans input from user, removing spaces and commas
        replace = replace.replace(' ', '')
        replace = replace.split(',')

        # Creates a numerical list from the user input
        replace_as_int = [int(num) for num in replace]

        # Puts cards that user requested for replacement into
        # the discard pile and draws replacements
        for i in replace_as_int:
            if i in player.cards_in_play_list:
                player.discards_list.append(i)
                player.cards_in_play_list.remove(i)
                player.deal()
    except ValueError:
        print('Only numbers, commas, and spaces please.')
    print('Cards in play', player.cards_in_play_list)


play_and_replace()
