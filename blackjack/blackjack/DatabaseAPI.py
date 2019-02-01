class DatabaseAPI :
    """Data"""

    @staticmethod
    def load_members():
        """open data"""
        file = open("members.txt","r")
        members = {}
        for line in file:
            name,passwd,tries,wins,chips = line.strip('\n').split(',')
            members[name] = [passwd,int(tries),float(wins), int(chips)]
        file.close()
        return members

    @staticmethod
    def store_members(members):
        """save data"""
        file = open("members.txt", "w")
        names = members.keys()
        for name in names:
            passwd, tries, wins, chips = members[name]
            line = name + ',' + passwd + "," + \
            str(tries) + ',' + str(wins) + "," + \
            str(chips) + '\n'
            file.write(line)
        file.close()

    @staticmethod
    def login(members):
        """login"""
        members = members
        username = input("Enter your name : (4 letters max) ")
        while len(username) > 4:
            username = input("Enter your name : (4 letters max) ")
        trypasswd = input("Enter your password : ")
        if username in members.keys():
            if trypasswd == members[username][0]:
                tries = members[username][1]
                wins = members[username][2]
                print("You played", tries, "games and won", wins, "of them")
                wpercent = 100 * wins/tries if tries >0 else 0
                print("Your all-time winning percentage is",\
                    "{0:.1f}".format(wpercent), "%")
                chips = members[username][3]
                if chips >= 0:
                    print("You have", chips, "chips.")
                else:
                    print("You owe", -chips, "chips.")
                return username, tries, wins, chips, members
            else:
                return DatabaseAPI.login(members)
        else:
            members[username] = (trypasswd, 0, 0, 0)
            return username, 0, 0, 0, members

    @staticmethod
    def show_top5(members):
        """show top 5 - by chips"""
        print('-----')
        sorted_members = sorted(members.items(),\
            key=lambda x: x[1][3],\
            reverse=True)
        print("All-time Top 5 based on the number of chips earned")
        rank = 1
        for member in sorted_members[:5]:
            chips = member[1][3]
            if chips <= 0 :
                break
            print(rank,".",member[0],":",chips)
            rank += 1

    @staticmethod
    def top5(members):
        """return top 5 - by chips"""
        
        sorted_members = sorted(members.items(),\
            key=lambda x: x[1][3],\
            reverse=True)
        result = "All-time Top 5 based on the number of chips earned\n"
        rank = 1
        for member in sorted_members[:5]:
            chips = member[1][3]
            if chips <= 0 :
                break
            result += str(rank) + "." + member[0] + ":" + str(chips) + "\n"
            rank += 1            
        return result