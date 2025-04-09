import random


lvl_quan = int(input('Enter quantity of levels in this dungeon = '))
dungeon = {}
lvl_act = 0
while lvl_act < lvl_quan:
    gold_quan = [random.randint(0,9) for i in range(lvl_act + 1)]
    dungeon[f'lvl_{lvl_act + 1}'] = gold_quan
    lvl_act += 1
for i in dungeon.keys():
    print(dungeon[i])
res = dungeon['lvl_1']
s = 0
for i in range(1, (len(dungeon))):
    current = dungeon[f"lvl_{i+1}"]
    if current[s] > current[s + 1]:
        res.append(current[s])
    else:
        res.append(current[s + 1])
        s += 1
print(res, 'summa -' , sum(res))