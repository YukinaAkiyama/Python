import random
#随机数模块
suits = [ "Spades ", "Hearts", "Diamonds" , "Clubs "]
ranks = [ "A","2","3","4","5","6","7","8" , "9", "10", "J", "Q","K"]
cards = [x+y for x in suits for y in ranks] + [ "Red Joker", "Black Joker"]
cardsHold = []
random.shuffle(cards)
for x in range(17):
    cardsHold.append( cards.pop())
print(cardsHold)
