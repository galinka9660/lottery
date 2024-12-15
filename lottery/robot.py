import random

class Robot:
     
    def random_numbers():
        range1_numbers = random.sample(range(1, 51), 5)
        range2_numbers = random.sample(range(1, 13), 2)
        all_numbers_robot = range1_numbers + range2_numbers
        return all_numbers_robot