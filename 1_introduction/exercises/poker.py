import random 

class Deck():
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.deck = [Card(random.choice(self.suits), random.choice(self.card_ranks)) for _ in range(self.number_of_cards)]

    def new_deck(self):
        self.deck = [Card(random.choice(self.suits), random.choice(self.rank)) for _ in range(self.number_of_cards)]

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    def draw_card(self):
        if self.deck:
            drawn_card = self.deck[0]
            # remove card from deck
            self.deck = self.deck[1:]
            return drawn_card
        else:
            print('Deck is empty')
        
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

if __name__ == "__main__":
    test = Deck(45)
    print(test.deck)


    print([(card.rank, card.suit) for card in test.deck])
    
    