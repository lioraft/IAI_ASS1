

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search


    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        # initialize the neighbors array
        neighbors = []
        # split the state string into an array
        arr = self.state_str.split(',')
        # sum the array
        sum = 0
        for i in range(len(arr)):
            sum += int(arr[i])
        # iterate over the array and create a neighbor for each cell
        for i in range(len(arr)-1):
            # create a neighbor
            neighbor = arr.copy()
            # flip the pancakes
            neighbor = neighbor[:i] + neighbor[i:][::-1]
            # calculate the sum of the neighbor
            if i > 0:
                sum -= int(arr[i-1])
            # add the neighbor to the neighbors array
            neighbors.append((pancake_state(','.join(neighbor)), sum))
        # return the neighbors array
        return neighbors




    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str
