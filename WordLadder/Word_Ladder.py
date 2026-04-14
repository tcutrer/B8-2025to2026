from collections import defaultdict, deque
import time

def differ_by_one_letter(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return count == 1


def build_graph(words):
    # The defaultdict derives from a dictionary, but creates a new list if getitem does not return a value
    # for example, if you do graph.get_item["cat"] and cat is not in the dictionary,
    # then a cat entry will automatically be entered with an empty list as the value.
    # see https://docs.python.org/3.13/library/collections.html#collections.defaultdict
    graph = defaultdict(list)

    for word1 in words:
        for word2 in words:
            if word1 != word2 and differ_by_one_letter(word1, word2):
                graph[word1].append(word2)
    return graph

def DFSUtil(graph, v, visited, goal):

    if v == goal:
        return

    visited.add(v)

    for neighbour in graph[v]:
        if neighbour not in visited:
            DFSUtil(graph, neighbour, visited, goal)

    

def DFS(graph, v, goal):
    start_time = time.perf_counter()
    visited = set()

    DFSUtil(graph, v, visited, goal)
    end_time = time.perf_counter()
    print(f"DFS execution time: {end_time - start_time:.6f} seconds")

def bfs_shortest_path(graph, start, goal):
    # A deque is like a queue but you can pop from both ends.
    # in doing a breadth first search, the queue stores a list of paths (a list of lists)
    # https://docs.python.org/3.13/library/collections.html#deque-objects
    queue = deque([[start]])  # store paths
    visited = set()

    while queue:
        path = queue.popleft()
        word = path[-1]

        if word == goal:
            return path

        if word not in visited:
            visited.add(word)
            for neighbor in graph[word]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # no path found

def dijkstra_algorithm(graph, start, goal):
    start_time = time.perf_counter()
    # Initialize distances and priority queue
    distances = {word: float('inf') for word in graph}
    distances[start] = 0
    previous_nodes = {word: None for word in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_word = priority_queue.pop(0)

        if current_distance > distances[current_word]:
            continue

        for neighbor in graph[current_word]:
            distance = current_distance + 1  # All edges have weight 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_word
                priority_queue.append((distance, neighbor))

    # Reconstruct path
    path = []
    current_word = goal
    while current_word is not None:
        path.append(current_word)
        current_word = previous_nodes[current_word]
    path.reverse()

    end_time = time.perf_counter()
    print(f"Dijkstra's Algorithm took {end_time - start_time:.6f} seconds")

    return path if path[0] == start else None  # Return path if it starts with the start word

def main():
    words = ["cat", "bat", "bet", "bed", "bad", "had", "hat", "het", "hot", "hog"]

    graph = build_graph(words)

    start = "cat"
    goal = "bed"

    start_time = time.perf_counter()
    path = bfs_shortest_path(graph, start, goal)
    end_time = time.perf_counter()
    print(f"BFS execution time: {end_time - start_time:.6f} seconds")

    DFS(graph, start, goal)
    dijkstra_algorithm(graph, start, goal)



if __name__ == "__main__":
    main()