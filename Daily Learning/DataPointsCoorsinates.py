# 1. Write a programe to given data of points x and y coordinates are given as follows points are (1, 2) (1, 3) (2, 4) (5, 7) in 2D oragin at 0,0

# 2. write finction to estimate of position of point in polar coordinate

# 3. A function to move point when displacement is given

# Q: 1:-
point = [(1,2), (1, 3), (2, 4), (5, 7)]

for x, y in point:
    distance = (x**2 +y**2) ** 0.5
    print(distance)

# Q: 2:-
def distance_point(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1) **2) **0.5
points = [(1,2), (1, 3), (2, 4), (5, 7)]
origin = (0,0)
for x, y in points:
    distancess = distance_point(x, y, origin[0], origin[1])
    print(distancess)

