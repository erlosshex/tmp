# coding: utf-8

f=open('game.txt')
score=f.read().split()

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])

avg_times=float(total_times)/game_times

if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0

print "你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案" % (game_times,min_times,avg_times)
