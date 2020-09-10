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

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = [], path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        visited.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path + [starting_vertex]
        
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                path_found = self.dfs_recursive(vertex, destination_vertex, visited, path + [starting_vertex])
                if path_found is not None:
                    return path_found




def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    vertexes = set()

    for i in range(len(ancestors)):
        vertexes.add(ancestors[i][0])
        vertexes.add(ancestors[i][1])

    for vertex in vertexes:
        graph.add_vertex(vertex)

    for i in range(len(ancestors)):

        graph.add_edge(ancestors[i][0],ancestors[i][1])

    vertexes_except_starting = vertexes

    vertexes_except_starting.remove(starting_node)

    final_path = []

    for vertex in vertexes_except_starting:

        path = graph.dfs_recursive(vertex, starting_node,visited = [], path = [])

        if path:

            if len(path) > len(final_path):

                final_path = path

    if len(final_path) == 0:

        return -1



    return final_path[0]


if __name__ == "__main__":
    
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors,1))
    print(earliest_ancestor(test_ancestors,2))
    print(earliest_ancestor(test_ancestors,3))
    print(earliest_ancestor(test_ancestors,4))
    print(earliest_ancestor(test_ancestors,5))
    print(earliest_ancestor(test_ancestors,6))
    print(earliest_ancestor(test_ancestors,7))
    print(earliest_ancestor(test_ancestors,8))
    print(earliest_ancestor(test_ancestors,9))
    print(earliest_ancestor(test_ancestors,10))
    print(earliest_ancestor(test_ancestors,11))

    