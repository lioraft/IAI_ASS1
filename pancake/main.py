from search import search, print_path
from pancake_state import pancake_state
from heuristics import *
import time
import random

if __name__ == '__main__':

    numbers = list(range(1, 11))
    random.shuffle(numbers)
    pancake_input = ','.join(str(x) for x in numbers)
    pancake_state2 = pancake_state(pancake_input)
    goal_state = list(range(10, 0, -1))
    goal_state = ','.join(str(x) for x in goal_state)

    start_time = time.time()
    search_result = search(pancake_state2, advanced_heuristic, goal_state)
    end_time = time.time()
    if search_result is None:
        print("No path found")
    else:
        print_path(search_result)
    print("Time for h1: ", end_time - start_time)





