from CONFIG import TILE
import random
textmap = [["", "", "", ""],
           ["W", "W", "W", "W"],
           ["W", "W", "W", "W"],
           ["W", "W", "W", "W"],
           ["W", "W", "W", "W"],
           ["W", "W", "W", "W"],
           ["W", "W", "W", "W"]]
coords = []
points = []
for i in range(1, len(textmap)):
    what_to_destroy = [random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)]
    textmap[i][what_to_destroy[0]] = ""
    textmap[i][what_to_destroy[1]] = ""
    textmap[i][what_to_destroy[2]] = ""
for i in range(len(textmap)):
    for j in range(len(textmap[i])):
        if textmap[i][j] == "W":
            coords.append([j * TILE, i * TILE]) #calculating where wall blocks should be
for wall in coords:
    x1 = wall[0]
    y1 = wall[1]
    x4 = x1 + TILE
    y4 = y1 + TILE
    points.append([x1, y1, x4, y4]) # packing list with thirst and fourth point of every wall (needed for knowing if a point is in/on a wall)