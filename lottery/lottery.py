from robot import Robot
from gamer import Gamer

class Lottery:

    winning_numbers = []    # row of numbers that lottery publishes
    prize = None
    gamers = [Gamer]
    winners = []
   
    def __init__(self, gamers):
        self.gamers = gamers 
        self.prize = 120000000

    def play_lottery(self):
        r = Robot
        self.winning_numbers = r.random_numbers()
        print("Winning numbers: ", self.winning_numbers)
        if len(self.gamers) != 0:
            for gamer in self.gamers:
                game = gamer.get_game()
                # print("Gamer: ", gamer.get_id(), ", gamer numbers: ", game)
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
        print("Lottery is played.")
        print(len(self.winners))

        if len(self.winners) != 0:
            for winner in self.winners:
                print("Gamer: ", winner.get_id(), ", gamer numbers: ", winner.get_game(),"\nhits of 50: ", winner.get_hits_of_50(), "common values of 50: ", winner.get_common_values_of_50(), "\nhits of 12: ", winner.get_hits_of_12(), "common values of 12: ", winner.get_common_values_of_12())
        return self.winners
    
  