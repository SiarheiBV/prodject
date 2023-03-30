def distance(*points: tuple[int, ...]) -> float:
    dist = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        dist += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist


you_coords = input("Enter coords in the format x1,y1 x2,y2... xn,yn: ")
list_coords = [tuple(map(int, coord.split(",")))
               for coord in you_coords.split()]
print(round(distance(*list_coords), 2))
