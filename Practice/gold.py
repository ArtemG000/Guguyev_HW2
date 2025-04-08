lvl_1 = [7]
dungeon = {
    "lvl_2": [5, 8],
    "lvl_3": [9, 8, 2],
    "lvl_4": [1, 3, 5, 6],
    "lvl_5": [6, 2, 4, 4, 5],
    "lvl_6": [9, 5, 3, 5, 5, 7],
    "lvl_7": [7, 4, 6, 4, 7, 6, 8]
}
res = lvl_1
s = 0
for i in range(2, 8):
    current = dungeon[f"lvl_{i}"]
    if current[s] > current[s + 1]:
        res.append(current[s])
    else:
        res.append(current[s + 1])
        s += 1

print(sum(res))