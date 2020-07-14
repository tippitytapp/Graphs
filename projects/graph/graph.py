"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        # set the index of the vertices dict to a vertex id
        # make the value of that index a set to hold the values of the edges
        self.vertices[vertex_id] = set()

    def add_edge(self, fromV, toV):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        # check that both the from vertex and the to vertex both exist in the graph
        if fromV in self.vertices and toV in self.vertices:
            # add the edge
            self.vertices[fromV].add(toV)
        else:
            # if the vertices dont exist, raise error to add
            raise IndexError('vertex (vertices) do not exist in graph, add to graph first')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        # return the vertex listing
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # create empty queue using the Queue class provided
        queue = Queue()
        # created empty set to house the visited nodes
        visited = set()
        # plac the starting_vertex in the queue
        queue.enqueue(starting_vertex)
        # while the queue is not empty
        while queue.size() > 0:
            # take the vertex out of the queue
            vertex = queue.dequeue()
            # if the vertex has not already been visited
            if vertex not in visited:
                # add the vertex to the visited set
                visited.add(vertex)
                print(vertex)
                # loop through all the next vertices of the neighbors of the vertex
                for next_vertex in self.get_neighbors(vertex):
                    # add those neighbors to the queue and then loop
                    queue.enqueue(next_vertex)
        # return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # create an epty stack using the Stack class provided
        stack = Stack()
        # create empty set to house all of the visited nodes
        visited = set()
        # push the starting vertex into the stack
        stack.push(starting_vertex)
        # while the stack is not empty
        while stack.size() > 0:
            # pop the vertex out of the queue
            vertex = stack.pop()
            # if the vertex is not already in the visited set
            if vertex not in visited:
                # add the vertex to the visited stack
                visited.add(vertex)
                print(vertex)
                # check the next vertx using get neighbors 
                for next_vertex in self.get_neighbors(vertex):
                    # add those neighbors to the stack and then loop
                    stack.push(next_vertex)
        # return visited

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO

        if starting_vertex not in self.visited:
            self.visited.add(starting_vertex)
            print(starting_vertex)
            for next_v in self.get_neighbors(starting_vertex):
                # self.visited.add(next_v)
                self.dft_recursive(next_v)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # # pass  # TODO
        # create empty queue using the Queue class provided
        queue = [[starting_vertex]]
        # created empty set to house the visited nodes
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
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
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
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # pass  # TODO
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





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
