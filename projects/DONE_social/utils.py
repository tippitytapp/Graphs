class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, fromV, toV):
        if fromV in self.vertices and toV in self.vertices:
            self.vertices[fromV].add(toV)
        else:
            raise IndexError('vertex (vertices) do not exist in graph, add to graph first')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    queue.enqueue(next_vertex)

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        if starting_vertex not in self.visited:
            self.visited.add(starting_vertex)
            print(starting_vertex)
            for next_v in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_v)


    def bfs(self, starting_vertex, destination_vertex):
        queue = [[starting_vertex]]
        visited = []
        if starting_vertex == destination_vertex:
            return queue
        while queue:
            path=queue.pop(0)
            vertex = path[-1]
            if vertex not in visited:
                for next_v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_v)
                    queue.append(new_path)
                    if next_v == destination_vertex:
                        return new_path
                visited.append(vertex)
        return 

    def dfs(self, starting_vertex, destination_vertex):
        stack = [[starting_vertex]]
        visited = []
        if starting_vertex == destination_vertex:
            return stack
        while stack:
            path = stack.pop(0)
            vertex = path[-1]
            if vertex not in visited:
                for next_v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_v)
                    stack.insert(0, new_path)
                    if next_v == destination_vertex:
                        return new_path
                visited.append(vertex)
        return

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path=[]):
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                new_path = self.dfs_recursive(next_v, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

