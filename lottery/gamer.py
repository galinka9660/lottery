from robot import Robot

class Gamer:
    id = None
    game = []           # numbers from a gamer
    hits_of_50 = None
    hits_of_12 = None
    common_values_of_50 = []
    common_values_of_12 = []

    def __init__(self, id):
        self.id = id
        r = Robot
        self.game = r.random_numbers()
    
    def get_game(self):
        return self.game 
    
    def get_id(self):
        return self.id
    
    def get_hits_of_50(self):
        return self.hits_of_50
    
    def get_hits_of_12(self):
        return self.hits_of_12
    
    def get_common_values_of_50(self):
        return self.common_values_of_50
    
    def get_common_values_of_12(self):
        return self.common_values_of_12
    
    def set_hits_of_50(self, hits):
        self.hits_of_50 = hits

    def set_hits_of_12(self, hits):
        self.hits_of_12 = hits
    
    def set_common_values1(self, common_values_of_50):
        self.common_values_of_50 = common_values_of_50

    def set_common_values2(self, common_values_of_12):
        self.common_values_of_12 = common_values_of_12

    
        
        

      
    