# Blackjack Game Contoller
from bjcard import Deck
from bjhand import *
from bjview import Reader
from DatabaseAPI import *

class BlackjackController:
    """defines Blackjack game controller class"""
    def __init__(self, name, chips):
        """creates player/dealer's empty hand and a deck of cards
        argument: name -- player' name in string (default: 'Dealer')
        """
        self.__player = PlayerHand(name, chips)
        self.__dealer = Hand()
        self.__deck = Deck()
        
    def play(self):
        """plays a round of blackjack game"""
        print("== new game ==")
        player = self.__player
        dealer = self.__dealer
        deck = self.__deck
        player.get(deck.next())
        dealer.get(deck.next())
        player.get(deck.next())
        dealer.get(deck.next(open=False))
        print("Dealer :", dealer)
        print(player.name, ":", player)
        if player.total == 21:
            print("Blackjack! You won.")
            player.earn_chips(2)
        else:
            while player.total < 21 and \
                  Reader.ox( "Hit?(o/x) "):
                player.get(deck.next())
                print(player.name, ":", player)
            if player.total > 21:
                print("You bust! I won.")
                player.lose_chips(1)
            else:
                while dealer.total <= 16:
                    dealer.get(deck.next())
                if dealer.total > 21:
                    print("I bust! You won.")
                    player.earn_chips(1)
                elif dealer.total == player.total:
                    print("We draw.")
                elif dealer.total > player.total:
                    print("I won.")
                    player.lose_chips(1)
                else:
                    print("You won.")
                    player.earn_chips(1)
            dealer.open()
            print("Dealer :", dealer)
        player.clear()
        dealer.clear()

def main():
    # main procedure
    print("Welcome to SMaSH Casino!")
    members = DatabaseAPI.load_members()
    username,tries,wins,chips,members = DatabaseAPI.login(members)
    game = BlackjackController(username, members[username][3])
    while True:
        game.play()
        if not Reader.ox("Play more, " + username + "? (o/x) "):
            break
    DatabaseAPI.show_top5(members)
    # print(DatabaseAPI.top5(members))
    print("Bye, " + username + "!")

# launch blackjack game
main()