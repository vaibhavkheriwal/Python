"""
You have a 3x3 grid. Each cell in the grid can either be empty or contain a number from 1 to 9. Write a Python function that checks if the numbers in the grid form a valid Sudoku subgrid. A valid Sudoku subgrid contains each number from 1 to 9 exactly once.

grid = [
    [5, 3, 4],
    [6, 7, 2],
    [1, 9, 8]
]
Expected output: True (This is a valid Sudoku subgrid)

grid = [
    [5, 3, 4],
    [6, 7, 2],
    [1, 1, 8]
]
Expected output: False (The number 1 is repeated)
"""

def valid_sudoku_subgrid(grid):
    find_one_time = 0

    for l in range(3):

        for k in range(3):

            for i in range(3):

                for j in range(3):

                    if grid[l][k] == grid[i][j]:

                        if find_one_time == 0:
                            find_one_time += 1
                        
                        else:
                            return False
            
            find_one_time = 0

    return True

grid_a = [[5, 3, 4],
        [6, 7, 2],
        [1, 9, 8]]

grid_b = [[5, 3, 4],
        [6, 7, 2],
        [1, 5, 8]]

grid_c = [[5, 3, 4],
        [9, 7, 2],
        [1, 9, 8]]

print(valid_sudoku_subgrid(grid_a))
print(valid_sudoku_subgrid(grid_b))
print(valid_sudoku_subgrid(grid_c))