# coding: utf-8

name=raw_input('请输入你的名字:')
lines=f.readlines()

scores={}

for l in lines:
    s=l.split()
    score[s[0]]=s[1:]


score=scores.get(name)

if score is None:
    score=[0,0,0]

scores[name]=[str(game_times),str(min_times),str(total_times)]

result=''

for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'

    result+=line
