def print_grid(matrix):
    state = matrix.copy()
    state[state.index(-1)] = "_"
    print(
        f"""
{state[0]} {state[1]} {state[2]}
{state[3]} {state[4]} {state[5]}
{state[6]} {state[7]} {state[8]}
        """
    )
def gen(state, b, d):
    """Generates the list of outcome of each move in d
    
    args:
        state(list): The state matrix of the 8puzzle, with a -1 in it, which corresponds to the current position
        b(int): The current position
        d(list): List of moves, made up of "up", "down", "left", "right"
    
    return:
        list: List containing the outcome of each move
    """
    x = []
    for i in d:
        temp = state.copy()
        if i == "up":
            temp[b-3], temp[b] = temp[b], temp[b-3]
        elif i == "down":
            temp[b+3], temp[b] = temp[b], temp[b+3]
        elif i == "right":
            temp[b+1], temp[b] = temp[b], temp[b+1]
        elif i == "left":
            temp[b-1], temp[b] = temp[b], temp[b-1]
        x.append(temp)
    return x
  
  
  def possible_moves(state, visited_states):
    """Generates the list of all possible moves, avoiding the previous states in visited_states
    
    args:
        state(list): The state matrix of the 8puzzle, with a -1 in it, which corresponds to the current position
        visited_states(set): Set consisting of states already visited
        
    return:
        list: list of all valid / feasible / possible moves
        
    """
    b = state.index(-1)
    d = []
    if b not in (0, 1, 2):
        d.append("up")
    if b not in (6, 7, 8):
        d.append("down")
    if b not in (0, 3, 6):
        d.append("left")
    if b not in (2, 5, 8):
        d.append("right")
    return [ move for move in gen(state, b, d) if tuple(move) not in visited_states]
def bfs(src, target):
    """8Puzzle problem implementation using BFS algorithm
    
    args:
        src(list): The initial state matrix of the 8Puzzle
        target(list): The expected final state matrix of the 8Puzzle
    """
    frontier = [src]
    visited_states = set()
    while len(frontier):
        state = frontier.pop(0)
        print_grid(state)
        visited_states.add(tuple(state))
        if(state == target):
            print("Success")
            return 
        else:
            for move in possible_moves(state, visited_states):
                if move not in frontier:
                    frontier.append(move)
    print("Fail")
#Test 1
src = [1, 2, 3, -1, 4, 5, 6, 7, 8] 
target=[1, 2, 3, 4, 5, 6, 7, 8, -1]
