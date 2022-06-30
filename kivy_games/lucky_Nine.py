from random import shuffle

# The deck of cards
def createDeck():
    Deck = []
    faces = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2, 11):
            Deck.append(str(card))
        for card in faces:
            Deck.append(card)

    shuffle(Deck)
    return Deck

cardDeck = createDeck()

class Player:
    
    def __init__(self,name,hand = []):
        self.name = input("Please enter your name: ")
        self.hand = hand
        self.score = self.setScore()
        self.bet = 0
        self.money = int(input(f"How much money do you have {self.name}: "))

    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "

        final_status = f"{self.name}'s cards {currentHand} score: {self.score}  Money: {self.money}  Bet: {self.bet}"
        return final_status

    def setScore(self):
        self.score = 0
        CardDict = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":0,"J":0,"Q":0,"K":0}
        for card in self.hand:
            self.score += CardDict[card]
        if self.score % 10 == 0:
            self.score = 0
        if self.score > 20:
            self.score -= 20
        if self.score > 10:
            self.score -= 10
        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self,amount):
        self.money -= amount
        self.bet += amount

    def win(self,result):
        if result == True:
            self.money += self.bet*2
            Banker.Bankmoney -= self.bet
            self.bet = 0
        else:
            Banker.Bankmoney += self.bet
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def lucky_nine(self):
        if self.score == 9 and len(self.hand) == 2:
            Banker.Bankmoney -= self.bet * 2
            self.money += (self.bet * 3)
            self.bet = 0


class House_Player(Player):
    def __init__(self, name,money = 1000):
        self.name = input("The Banker's name is: ")
        self.Bankmoney = money

    def printHouse(House):
        for card in range(len(House.hand)):
            if card == 0:
                print("X",end=" ")
            elif card == len(House.hand) - 1:
                print(House.hand[card])
            else:
                print(House.hand[card], end=" ")

    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        final_status = f"{self.name}'s cards {currentHand} score: {self.score}  Money: {self.Bankmoney}"
        return final_status


def deal_hand():
    dealCard = [cardDeck.pop(),cardDeck.pop()]
    return dealCard

deal1 = deal_hand()
deal2 = deal_hand()
deal5 = deal_hand()

Player1 = Player(deal1)
Player2 = Player(deal2)
Banker = House_Player(deal5)


if __name__ == '__main__':

    while (True):

        if len(cardDeck) < 20:
            cardDeck = createDeck()

        def deal_hand():
            dealCard = [cardDeck.pop(),cardDeck.pop()]
            return dealCard

        deal1 = deal_hand()
        deal2 = deal_hand()
        deal3 = deal_hand()

        Player1.play(deal1)
        Bet = int(input(f"Please enter your bet {Player1.name}: "))
        Player1.betMoney(Bet)

        Player2.play(deal2)
        Bet = int(input(f"Please enter your bet {Player2.name}: "))
        Player2.betMoney(Bet)

        Banker.play(deal3)

        print(Player1)
        print(Player2)
        print(House_Player.printHouse(Banker))
        print("\n")


        if Player1.score == 9:
            print(f"{Player1.name} got a LUCKY 9...")
            print(Player1)

        else:
            print("\n")
            if Player1.score < 9:
                print(Player1)
                hint = input(f"{Player1.name} do you want another card? (y/n): ")
                if hint == "y":
                    Player1.hit(cardDeck.pop())
                    print(Player1)
                
        if Player2.score == 9:
            print(f"{Player2.name} got a LUCKY 9...")
            print(Player2)
        else:
            print("\n")
            if Player2.score < 9:
                print(Player2)
                hint = input(f"{Player2.name} do you want another card? (y/n): ")
                if hint == "y":
                    Player2.hit(cardDeck.pop())
                    print(Player2)

        if Banker.score == 9:
            print(Banker)
            print("Banker got a LUCKY 9. Better luck next time...")

            if Player1.score == 9:
                Player1.draw()
                print(f"It's a Draw with {Player1.name}...")
            else:
                Player1.money -= Player1.bet
                Banker.Bankmoney += Player1.bet
                Player1.win(False)

            if Player2.score == 9:
                Player2.draw()
                print(f"It's a Draw with {Player2.name}...")
            else:
                Player2.money -= Player2.bet
                Banker.Bankmoney += Player2.bet
                Player2.win(False)

        else:
            print("\n")
            print(Banker)
            if Banker.score < 9:
                Hit = input("Will the Banker Hit:(y/n) ")
                if Hit == "y":
                    Banker.hit(cardDeck.pop())
                    print(Banker)
                else: 
                    print("Banker will pass. Open cards...")

        if Player1.score == 9 and len(Player1.hand) < 3:
            Player1.lucky_nine()
        else:
            if Player1.score > Banker.score:
                Player1.win(True)
                print(f"{Player1.name} Wins...")
            elif Player1.score == Banker.score:
                Player1.draw
                print(f"{Player1.name} has a Draw...")
            else:
                Player1.win(False)
                print(f"{Player1.name} Lost...")

        if Player2.score == 9 and len(Player2.hand) < 3:
            Player2.lucky_nine()
        else:
            if Player2.score > Banker.score:
                Player2.win(True)
                print(f"{Player2.name} Wins...")
            elif Player2.score == Banker.score:
                Player2.draw
                print(f"{Player2.name} has a Draw...")
            else:
                Player2.win(False)
                print(f"{Player2.name} Lost...")

        print(Player1)
        print(Player2)
        print(Banker)
