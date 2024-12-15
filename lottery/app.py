from lottery import Lottery
from gamer import Gamer
import time

cnt = 0
gamers = []

start = int(time.time()*1000)
while cnt < 1000000:
    g = Gamer(cnt)
    gamers.append(g)
    cnt += 1
end = int(time.time()*1000)
timer = end - start
print(timer)

start = int(time.time()*1000)
for cnt in range(1,1000000):
    g = Gamer(cnt)
    gamers.append(g)
end = int(time.time()*1000)
timer = end - start
print(timer)

    
""" l = Lottery(gamers)
while len(l.winners) == 0:
    l.play_lottery()"""
    