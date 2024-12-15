from lottery import Lottery
from gamer import Gamer

g = Gamer(1)
gamers = [g]
l = Lottery(gamers)
l.play_lottery()