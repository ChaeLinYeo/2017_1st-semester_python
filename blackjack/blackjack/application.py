
from tkinter import *
from DatabaseAPI import *
from bjhand import *
from bjcard import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx = 20,pady = 20)
        self.create_widget()
        self.username = ""
        self.members = {}
        self.tries = 0
        self.wins = 0
        self.wpercent = 0
        self.chips = 0
        self.playerHand = None
        self.dealerHand = None
        self.deck = None
        self.player_num_of_cards = 0

    
    def create_widget(self):
        Label(self, text = "Welcome to SMaSH Casino!").grid(row = 0, columnspan = 3)

        """ID PW"""
        Label(self, text = "ID").grid(row = 1, column = 0)
        self.entryID = Entry(self, width = 20 )
        self.entryID.grid(row=1, column=1)
        Label(self, text = "ID는 영어로 최대 4글자 입니다.").grid(row = 1, column = 7)

        """Login & Logout"""
        Label(self, text = "PW").grid(row = 2, column = 0)
        self.entryPW = Entry(self, width = 20)
        self.entryPW.grid(row=2, column=1)
        self.btnIn = Button(self, text="Login", command=self.login, state = NORMAL)
        self.btnIn.grid(row=2, column=2)
        self.btnOut = Button(self, text="Logout", command=self.logout, state = DISABLED)
        self.btnOut.grid(row=2, column=3)

        """Newgame"""
        self.btnNewgame = Button(self, text="New Game", command=self.new_game, state=DISABLED)
        self.btnNewgame.grid(row=3, columnspan = 3)

        """Dealer, Player's Cards"""
        Label(self, text = "Dealer").grid(row = 4, column = 0)
        self.entryDealer = Entry(self, width = 50)
        self.entryDealer.grid(row=4, column=1)       

        self.labelPlayer = Label(self, text = "Player")
        self.labelPlayer.grid(row = 5, column = 0)
        self.entryPlayer = Entry(self, width = 50)
        self.entryPlayer.grid(row=5, column=1)       

        """Hit & Stand"""
        self.btnHit = Button(self, text="Hit", command=self.hit_card, state=DISABLED)
        self.btnHit.grid(row=5, column = 2)
        self.btnStand = Button(self, text="Stand", command=self.stand_card, state=DISABLED)
        self.btnStand.grid(row=5, column = 3)
        Label(self, text = "chips=").grid(row = 5, column = 4)
        self.labelChips = Label(self, text = "")
        self.labelChips.grid(row = 5, column = 5)

        self.labelGameResult = Label(self, text = "Game Result")
        self.labelGameResult.grid(row = 7, column = 0)
        self.entryGameResult = Entry(self, width = 50)
        self.entryGameResult.grid(row=7, column=1)       
    
    def login(self):
        """login"""
        self.username = self.entryID.get()
        if (len(self.username) >4) :
            # self.entryID.insert(0,"4 letters max")
            self.entryID.delete(0,END)
            self.entryID.insert(0,"")
        
        trypasswd = self.entryPW.get()
        self.members = DatabaseAPI.load_members()
        if self.username in self.members.keys() :
            if trypasswd != self.members[self.username][0] :
                # self.entryPW.insert(0,"Wrong PW")
                self.entryPW.delete(0,END)
                self.entryID.insert(0,"")
            self.btnOut.config(state = NORMAL)
            self.btnIn.config(state = DISABLED)
        else :
            self.members[self.username] = [trypasswd, 0, 0, 0]
            self.btnOut.config(state = NORMAL)
            self.btnIn.config(state = DISABLED)
        
        tries = self.members[self.username][1]
        wins = self.members[self.username][2]
        wpercent = round(100 * wins/tries,1) if tries>0 else 0
        chips = self.members[self.username][3]

        self.btnNewgame.config(state=NORMAL)
        self.playerHand = PlayerHand(self.username, self.members[self.username][3])
        self.dealerHand = Hand()
        self.labelPlayer.config(text=self.username)
        self.labelChips.config(text=self.playerHand.get_chips())
        messagebox.showinfo("info","You played " + str(tries) +" games and won " + str(wins) + " of them.\n Your all-time winning percentage is " + str(wpercent) +" %.\n You have " + str(chips) + " chips.")

    def display_cards(self):
        self.entryDealer.delete(0,END)
        self.entryDealer.insert(0,self.dealerHand)
        self.entryPlayer.delete(0,END)
        self.entryPlayer.insert(0,self.playerHand)
        self.labelChips.config(text=self.playerHand.get_chips())
    
    def new_game(self):
        self.members[self.username][1] += 1
        self.deck = Deck()
        self.playerHand.clear()
        self.dealerHand.clear()
        self.entryDealer.delete(0,END)
        self.entryDealer.insert(0,"")
        self.entryPlayer.delete(0,END)
        self.entryPlayer.insert(0,"")
        self.entryGameResult.delete(0,END)
        self.entryGameResult.insert(0,"")
        self.btnHit.config(state=NORMAL)
        self.btnStand.config(state=NORMAL)

        self.playerHand.get(self.deck.next())
        self.dealerHand.get(self.deck.next())
        self.playerHand.get(self.deck.next())
        self.dealerHand.get(self.deck.next(open=False))
        self.display_cards()
        self.player_num_of_cards = 2
        self.btnNewgame.config(state = DISABLED)


    def hit_card(self):
        if self.playerHand.total < 21:
            self.playerHand.get(self.deck.next())
            self.display_cards()
        if self.playerHand.total >= 21:
            self.game_result()

    def stand_card(self):
        self.game_result()
        self.btnNewgame.config(state = NORMAL)
    
    def game_result(self):
        while self.dealerHand.total <= 16:
            self.dealerHand.get(self.deck.next())
        if self.playerHand.total == 21:
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"Blackjack! You won.")
            self.playerHand.earn_chips(2)
            self.members[self.username][2] += 1
            self.btnNewgame.config(state = NORMAL)
        elif self.dealerHand.total == 21 :
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"Blackjack! I won.")
            self.playerHand.lose_chips(2)
            self.btnNewgame.config(state = NORMAL)
        elif self.dealerHand.total > 21 :
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"I bust! You won.")
            self.playerHand.earn_chips(1)
            self.btnNewgame.config(state = NORMAL)
            self.members[self.username][2] += 1
        elif self.playerHand.total > 21:
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"You bust! I won.")
            self.playerHand.lose_chips(1)
            self.btnNewgame.config(state = NORMAL)
        elif self.dealerHand.total == self.playerHand.total:
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"We draw.")
        elif (self.dealerHand.total > self.playerHand.total) and (21> self.dealerHand.total):
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"I won.")
            self.playerHand.lose_chips(1)
        else:
            self.entryGameResult.delete(0,END)
            self.entryGameResult.insert(0,"You won.")
            self.playerHand.earn_chips(1)
            self.members[self.username][2] += 1

        self.dealerHand.open()
        self.display_cards()
        self.btnHit.config(state=DISABLED)
        self.btnStand.config(state=DISABLED)

    def logout(self):
        self.btnOut.config(state = DISABLED)
        self.btnIn.config(state = NORMAL)
        self.members[self.username][3] = self.playerHand.get_chips()
        DatabaseAPI.store_members(self.members)
        self.entryID.delete(0,END)
        self.entryID.insert(0,"")
        self.entryPW.delete(0,END)
        self.entryPW.insert(0,"")
        self.entryDealer.delete(0,END)
        self.entryDealer.insert(0,"")
        self.labelPlayer.config(text="Player")
        self.entryPlayer.delete(0,END)
        self.entryPlayer.insert(0,"")
        self.labelChips.config(text="")
        self.entryGameResult.delete(0,END)
        self.entryGameResult.insert(0,"")
        messagebox.showinfo("info", DatabaseAPI.top5(self.members) + "Bye, " + self.username + "!")
        self.btnNewgame.config(state = DISABLED)


root = Tk()
root.geometry("1000x500")
root.title("Blackjack")
app = Application(master=root)
app.mainloop()
            