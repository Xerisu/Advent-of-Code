input_file = open("./cavern.txt", "r")

maze = input_file.readlines()

input_file.close()

maze = [[int(x) for x in row.strip()] for row in maze]

y_max = len(maze)
x_max = len(maze[0])

bigger_maze = [[0 for _ in range(x_max*5)] for _ in range(y_max*5)]

for i in range(5):
    for j in range(5):
        for y in range(y_max):
            for x in range(x_max):
                bigger_maze[i*y_max + y][j*x_max + x] = (maze[y][x] + i + j) % 10
                if maze[y][x] + i + j > 9:
                    bigger_maze[i * y_max + y][j * x_max + x] += 1


def finding_lowest(distances, queue):
    min_dist = float('inf')
    y = None
    x = None
    for elem in queue:
        if distances[elem[0]][elem[1]] < min_dist:
            min_dist = distances[elem[0]][elem[1]]
            y = elem[0]
            x = elem[1]
    return y, x, min_dist


def dijkstra(graph, start, end):
    distances = [[float('inf') for _ in row] for row in graph]
    queue = []
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            queue.append([y, x])
    distances[start[0]][start[1]] = 0

    while len(queue) != 0:
        (y, x, _) = finding_lowest(distances, queue)
        queue.remove([y, x])
        if y == end[0] and x == end[1]:
            return distances[y][x]

        neighbours = [n for n in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]] if n in queue]
        for n in neighbours:
            alt_distance = distances[y][x] + graph[n[0]][n[1]]
            if alt_distance < distances[n[0]][n[1]]:
                distances[n[0]][n[1]] = alt_distance


def print_list(l):
    for row in l:
        for n in row:
            print(str(n) + " ", end="")
        print("")


print(dijkstra(bigger_maze, [0, 0], [5*y_max - 1, 5*x_max - 1])) # I swear it works
print(dijkstra(maze, [0, 0], [y_max - 1, x_max - 1]))

