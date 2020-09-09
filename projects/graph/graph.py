"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        if vertex_id not in self.vertices:

            self.vertices[vertex_id] = set()
        else:

            raise Exception("The vertex you're trying to add, already exists in the graph.")


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        if v1 in self.vertices and v2 in self.vertices:

            if v2 not in self.vertices[v1]:

                self.vertices[v1].add(v2)
            
            else:

                raise Exception('The edge you are trying to add, already exists in the graph.')

        elif v1 not in self.vertices or v2 not in self.vertices:

            raise Exception('Some of the vertex are not in the graph, please double check.')



    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        queue = Queue()
        visited = []

        queue.enqueue(starting_vertex)

        while queue.size() > 0:

            current = queue.dequeue()

            if current not in visited:

                visited.append(current)


                for vertex in self.get_neighbors(current):

                    queue.enqueue(vertex)

        [print(vertex) for vertex in visited]


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        stack = Stack()
        visited = []

        stack.push(starting_vertex)

        while stack.size() > 0:

            current = stack.pop()

            if current not in visited:

                visited.append(current)

                for vertex in self.get_neighbors(current):

                    stack.push(vertex)

        [print(vertex) for vertex in visited]


    def dft_recursive(self, starting_vertex,visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.append(starting_vertex)

        print(starting_vertex)

        if self.get_neighbors(starting_vertex):

            for vertex in self.get_neighbors(starting_vertex):

                if vertex not in visited:

                    self.dft_recursive(vertex,visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = []

        queue.enqueue([starting_vertex])

        while queue.size() > 0:

            path  = queue.dequeue()
            current = path[-1]

            if current == destination_vertex:

                return path

            if current not in visited:

                visited.append(current)

                for vertex in self.get_neighbors(current):

                    temp_path = path

                    queue.enqueue(temp_path + [vertex])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        visited = []

        stack.push([starting_vertex])

        while stack.size() > 0:

            path  = stack.pop()
            current = path[-1]

            if current == destination_vertex:

                return path

            if current not in visited:

                visited.append(current)

                for vertex in self.get_neighbors(current):

                    temp_path = path

                    stack.push(temp_path + [vertex])


    def dfs_recursive(self, starting_vertex, destination_vertex, visited = [], path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # visited.append(starting_vertex)

        # if starting_vertex == destination_vertex:

        #     return path + [starting_vertex]
        
        # if self.get_neighbors(starting_vertex):

        #     for vertex in self.get_neighbors(starting_vertex):

        #         if vertex not in visited:

        #             if self.dfs_recursive(vertex,destination_vertex,visited,path + [starting_vertex]):

        #                 return self.dfs_recursive(vertex,destination_vertex,visited,path + [starting_vertex])

        # return None
        visited.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path + [starting_vertex]
        
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                path_found = self.dfs_recursive(vertex, destination_vertex, visited, path + [starting_vertex])
                if path_found is not None:
                    return path_found
        

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
