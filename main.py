from card import Card
from atm import Atm

# Database of cards with ID, PIN and account balance
card1 = Card(1, 1234, 3000)
card2 = Card(2, 1234, 2400)
card3 = Card(3, 1234, 6600)
cards = [card1, card2, card3]

# populate atm with cards database
atm1 = Atm(cards)

atm1.runAtm()