input_file = open("./path.txt","r")

paths = input_file.readlines()
paths = [elem.strip() for elem in paths]
paths = [elem.split('-') for elem in paths]
input_file.close()

cave_system = {}

for path in paths:
    if path[0] not in cave_system:
        cave_system[path[0]] = set()
    cave_system[path[0]].add(path[1])
    if path[1] not in cave_system:
        cave_system[path[1]] = set()
    cave_system[path[1]].add(path[0])

def dfs(graph, start, end, small_visited=False, visited=None):
    possible_paths = 0
    if visited is None:
        visited = set()
    if not start.isupper():
        visited.add(start)
    
    if start == end:
        return 1
    
    for next in graph[start] - visited:
        possible_paths += dfs(graph, next, end, small_visited, visited.copy())

    if not small_visited:
        for next in (visited.intersection(graph[start])) - set(['start']):
            possible_paths += dfs(graph, next, end, True, visited.copy())
    return possible_paths 

print(dfs(cave_system, 'start', 'end'))