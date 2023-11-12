class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If already at the destination, no need to take the bus
        if source == target:
            return 0

        # Create a graph that uses stops as vertices
        graph = collections.defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route)

        # Initialize a queue with the starting stop and count as 0
        queue = collections.deque([(source, 0)])
        # Keep track of visited stops and visited routes to avoid revisiting
        visited_stops = set()
        visited_route = set()

        while queue:
            # Pop the stop and count from the queue
            stop, count = queue.popleft()
            
            # If reached the destination, return the count
            if stop == target:
                return count

            # Iterate over the routes that go through the current stop
            for route in graph[stop]:
                if route not in visited_route:
                    visited_route.add(route)
                    
                    # Explore the stops in the current route
                    for next_stop in routes[route]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            # Add the next stop and increment the count to the queue
                            queue.append((next_stop, count + 1))

        # If no valid route found, return -1
        return -1
