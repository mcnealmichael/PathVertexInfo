class PathVertexInfo:
    def __init__(self, vertex = None):
        self.vertex = vertex
        self.distance = float("inf")
        self.predecessor = None

    # Utility method to remove and return the list's PathVertexInfo item that
    # has the minimum distance
    @staticmethod
    def remove_min(items):
        if 0 == len(items):
            return None

        min_index = 0
        for i in range(1, len(items)):
            if items[i].distance < items[min_index].distance:
                min_index = i

        # Get the info with the minimum distance
        info_with_min_distance = items[min_index]

        # Remove the info with the minimum distance
        del items[min_index]

        return info_with_min_distance

    def dijkstra_shortest_path(self, start_vertex):
        # Initialize a dictionary and a list for vertex information
        info = dict()
        unvisited = []

        # Put a PathVertexInfo for each vertex in info and unvisited
        for vertex in self.get_vertices():
            new_info = PathVertexInfo(vertex)
            info[vertex] = new_info
            unvisited.append(new_info)

        # start_vertex has a distance of 0 from itself
        info[start_vertex].distance = 0.0

        # Iterate through all unvisited vertices
        while len(unvisited) > 0:
            # Remove info with minimum distance
            current_info = PathVertexInfo.remove_min(unvisited)
            # check potential path lengths from current vertex to all neighbors
            for edge in self.get_edges_from(current_info.vertex):
                adjacent_vertex = edge.to_vertex
                alternative_path_distance = current_info.distance + edge.weight
                # If a shorter path from start_vertex to adjacent_vertex is 
                # found, update adjacent_vertex's distance and predecessor
                adjacent_info = info[adjacent_info]
                if alternative_path_distance < adjacent_info.distance:
                    adjacent_info.distance = alternative_path_distance
                    adjacent_info.predecessor = current_info.vertex
        