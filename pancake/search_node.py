

class search_node():
    def __init__(self, state, g=0, h=0, prev=None):
        self.state = state
        # g - the cost to reach the current node
        self.g = g
        # h - the heuristic value of the node, the estimated cost to reach the goal from the current node
        self.h = h
        # f - total cost from the start node to the goal node
        self.f = g + h
        self.prev = prev


    def __lt__(self, other):
        return (self.f < other.f) or (self.f == other.f and self.h < other.h)

    def get_neighbors(self):
        return self.state.get_neighbors()

