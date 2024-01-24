# function that takes in a state and returns the heuristic value of the state based
# on demands of the exercise: when reaching a cell that is not in place, add the sum of the cells from that cell to the end of the array

def base_heuristic(_pancake_state):
    # get the state string
    str = _pancake_state.get_state_str()
    # split the string into an array
    arr = str.split(',')
    # heuristic value
    h = 0
    # iterate over the array until reaching a cell that is not in place
    notInPlace = False
    i = 0
    while i < len(arr) and not notInPlace:
        if int(arr[i]) != len(arr) - i:
            notInPlace = True
        else:
            i += 1
    # when reaching a cell that is not in place, add the sum of the cells from that cell to the end of the array
    for i in range(i, len(arr)):
        h += int(arr[i])
    return h

# function that takes in a state and returns the heuristic value of the state based
# on demands of the exercise: when reaching a cell that is not in place, add the sum of the cells from that cell to the end of the array
# and add the difference between each pancake and its following pancake, if the difference is greater than 1
def advanced_heuristic(_pancake_state):
    # Convert state string to an array of integers
    pancakes = list(map(int, _pancake_state.get_state_str().split(',')))
    # if list is sorted, return 0
    if pancakes == sorted(pancakes):
        return 0
    h = 0  # Initialize heuristic value
    notInPlace = False  # Flag to identify the first out-of-place pancake
    length = len(pancakes)
    # Find the first out-of-place pancake
    for i in range(length):
        if pancakes[i] != length - i:
            notInPlace = True
            break
    # If an out-of-place pancake is found, calculate the heuristic
    if notInPlace:
        # Add the sum of the values from the first out-of-place pancake to the end
        h = sum(pancakes[i:length])
        # Add the difference between each pancake and its following pancake, if the difference is greater than 1
        for j in range(i, length - 1):
            diff = abs(pancakes[j] - pancakes[j + 1])
            if diff > 1:
                h += diff
    return h