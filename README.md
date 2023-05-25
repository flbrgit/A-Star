# A* Algorithm Implementation in Python
This code implements the A* algorithm for finding the shortest path between two points on a grid. The algorithm uses a heuristic function to estimate the cost of moving from each node to the goal node, and 
combines this with the actual cost of moving from the start node to each node to determine the best path.

The code defines two classes: _NODE_ and _ASTAR_. The _NODE_ class represents a single node on the grid, and stores its position, actual cost (_g_), estimated cost to the goal (_h_), total cost (_f_), and parent node (_old_). The 
_ASTAR_ class represents the entire search space, and contains methods for creating nodes, computing neighbors, selecting the best node to visit next, and updating the open list.

To use the code, create an instance of the ASTAR class with the start and end positions, dimensions of the grid, and any optional parameters such as a custom neighbor function. Then call the run method to run the algorithm 
and return the shortest path as a list of positions.
