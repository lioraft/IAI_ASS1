from search_node import search_node
import heapq
# search class - implementation of A* algorithm

# according to A* algorithm, the open set is a priority queue
def create_open_set():
    #return an min heap (priority queue) and an empty dictionary
    return [], {}

# according to A* algorithm, the closed set is a set
def create_closed_set():
    #return empty dictionary
    return {}

# add the node to the open set which is a priority queue
def add_to_open(vn, open_set):
    # add the node to the min heap
    heapq.heappush(open_set[0], vn)
    # add the node to the dictionary, the key is the state string and the value is the node
    open_set[1][vn.state.get_state_str()] = vn


# returns True if the open set is not empty
def open_not_empty(open_set):
    # return True if the length of the min heap is greater than 0
    return len(open_set[0]) > 0

# returns the node with the lowest f value from the open set
def get_best(open_set):
    return heapq.heappop(open_set[0])

# add the node to the closed set which is a set
def add_to_closed(vn, closed_set):
    # add the node to the dictionary, the key is the state string and the value is the node
    closed_set[vn.state.get_state_str()] = vn

#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
def duplicate_in_open(vn, open_set):
    # check if the state string is in the dictionary
    state_str = vn.state.get_state_str()
    if state_str in open_set[1]:
        # if the node is in the dictionary, get the node from the dictionary
        node = open_set[1][state_str]
        # if the node in the heap has lower g than the node we want to add, return True
        if node.g <= vn.g:
            return True
    return False


#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
def duplicate_in_closed(vn, closed_set):
    # check if the state string is in the dictionary
    state_str = vn.state.get_state_str()
    if state_str in closed_set:
        # if the node is in the dictionary, get the node from the dictionary
        node = closed_set[state_str]
        # if the node in the heap has lower g than the node we want to add, return True
        if node.g <= vn.g:
            return True
    return False

def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




