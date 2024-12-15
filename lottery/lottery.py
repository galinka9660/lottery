from robot import Robot
from gamer import Gamer

class Lottery:

    winning_numbers = []    # row of numbers that lottery publishes
    prize = None
    gamers = [Gamer]
    winners = [Gamer]
   
    def __init__(self, gamers):
       self.gamers = gamers 
       self.prize = 120000000
       r = Robot
       self.winning_numbers = r.random_numbers()

    def play_lottery(self):
        if len(self.gamers) != 0:
            for gamer in self.gamers:
                game = gamer.get_game()
                common_values1 = []
                common_values2 = []
                hits_of_50 = 0
                hits_of_12 = 0
                for item in game[:5]:
                    if item in self.winning_numbers[:5]:
                        common_values1.append(item)
                        hits_of_50 += 1
                for item in game[5:]:
                    if item in self.winning_numbers[5:]:
                        common_values2.append(item)
                        hits_of_12 += 1
                if hits_of_50 == 2 and hits_of_12 == 1:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 1 and hits_of_12 == 2:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 3 and hits_of_12 == 0:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 3 and hits_of_12 == 1:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 2 and hits_of_12 == 2:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 4 and hits_of_12 == 0:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 3 and hits_of_12 == 2:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 4 and hits_of_12 == 1:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 4 and hits_of_12 == 2:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 5 and hits_of_12 == 0:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 5 and hits_of_12 == 1:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
                if hits_of_50 == 5 and hits_of_12 == 2:
                    gamer.set_hits_of_50(hits_of_50)
                    gamer.set_hits_of_12(hits_of_12)
                    gamer.set_common_values1(common_values1)
                    gamer.set_common_values2(common_values2)
                    self.winners.append(gamer)
        else:
            print("List of gamers[] is empty.")   
        return self.winners
    
  