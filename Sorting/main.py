vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


num = list(range(len(vertices)))


add = [[] for _ in range(len(vertices))]


add[0].append(1)
add[1].append(0)
add[1].append(2)
add[2].append(1)
add[2].extend([3, 4])
add[3].extend([2, 4, 5, 6])
add[4].extend([2, 3, 5])
add[5].extend([3, 4])
add[6].append(6)


for i in range(len(vertices)):
    vertex = vertices[i]
    neighbors = [num[index] for index in add[i]]
    print(f"{vertex}: {neighbors}")
