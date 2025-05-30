import random

class Card:
    def __init__(self, number):
        self.number = number

    def value(self):
        if self.number.isdigit():
            return int(self.number)
        elif self.number == 'A':
            return 11
        else:
            return 10

    def __str__(self):
        return self.number


class Deck:
    def __init__(self):
        suits = 4
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(number) for _ in range(suits) for number in numbers]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

    def print_all_cards(self):
        for card in self.cards:
            print(card)


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def value(self):
        value = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.number == 'A')
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


class Player:
    def __init__(self):
        self.hand = Hand()

    def play(self, deck):
        while True:
            print(f"Twoja reka: {self.hand} (wartosc: {self.hand.value()})")
            if self.hand.value() >= 21:
                break
            move = input("Dobierz karte albo nie dobieraj (zostaw/dobierz): ").lower()
            if move == 'zostaw':
                break
            elif move == 'dobierz':
                self.hand.add(deck.deal())


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play(self, deck):
        while self.hand.value() < 17:
            self.hand.add(deck.deal())


def main():
    deck = Deck()
    player = Player()
    dealer = Dealer()

    player.hand.add(deck.deal())
    player.hand.add(deck.deal())

    dealer.hand.add(deck.deal())
    dealer.hand.add(deck.deal())

    print("Dealer pokazuje:", dealer.hand.cards[0])

    player.play(deck)
    if player.hand.value() > 21:
        print("Przegrales.")
        return

    dealer.play(deck)
    print(f"Karty dealera: {dealer.hand} (wartosc: {dealer.hand.value()})")

    if dealer.hand.value() > 21 or player.hand.value() > dealer.hand.value():
        print("Wygrywasz!")
    elif player.hand.value() == dealer.hand.value():
        print("Remis.")
    else:
        print("Dealer wygrywa.")


if __name__ == "__main__":
    main()

