def print_floor(floor, curr_row, curr_col): 
    """Prints the floor matrix with the location of the AI agent

    Args:
        floor (array): 2D array of the floor state
        curr_row (int): current row index
        curr_col (int): current column index
    """
    for row in range(len(floor)):
        for col in range(len(floor[row])):
            if (curr_row, curr_col) == (row, col):
                print(" >", floor[row][col], "<", end='', sep='')
            else:
                print("  ", floor[row][col], " ", end='', sep='')
        print()
    print()
def notClean(floor):
    """Function to check if the floor is not clean

    Args:
        floor (array): 2D array of the floor state

    Returns:
        boolean: True if the floor is not clean, else False 
    """
    for row in floor:
        if 1 in row:
            return True;
    return False
def clean(floor, i, j):
    """The function that does the cleaning of the floor. This can be thought of as the brain of the AI agent

    Args:
        floor (array): 2D array of the floor state
        i (int): starting row index of the AI agent
        j (int): starting column index of the AI agent
    """
    goRight = True
    
    while notClean(floor):
        print_floor(floor, i, j)

        # Clean
        if floor[i][j]:
            floor[i][j] = 0

        # Decide Direction
        if j == len(floor[i])-1 and goRight:
            i = (i + 1) % len(floor)
            goRight = False

        elif j == 0 and not goRight:
            i = (i + 1) % len(floor)
            goRight = True
        
        else:
            if goRight:
                j = j + 1
            else:
                j = j - 1
        
    # Cleaned Floor
    print_floor(floor, -1, -1)
n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))

floor = []
print('Enter the rows. 1 for dirt on block, 0 for clean block.')
for i in range(n):
    row = list(map(int, input().split()))[:m]
    floor.append(row)
    

# Hardcoded test
floor = [[0, 0, 1, 0],
         [0, 1, 1, 1],
         [0, 0, 1, 1]]

clean(floor, 0, 0)
