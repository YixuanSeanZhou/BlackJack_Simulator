import Cards    
import random
import copy
kind = ['d', 's', 'h', 'c']

class Deck:
    deck = []

    """"
    Init the deck wth all the cards
    """
    def __init__ (self):
        for i in kind:
            for j in range(1,13 + 1):
                self.deck.append(Cards.Card(i, j))
        self.shuffle()

    def shuffle(self):
        deckTemp = []
        numberOfCards = len(self.deck)
        for i in range (0, numberOfCards):
            randIndex = random.randint(0,len(self.deck) - 1)
            deckTemp.append(self.deck[randIndex])
            self.deck.pop(randIndex)
        self.deck = copy.deepcopy(deckTemp)


    def showDeck(self):
        for card in self.deck:
            print(str(card.kind) + str(card.number))
