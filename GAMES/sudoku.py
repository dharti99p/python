def is_valid_sudoku(puzzle):
    # Check rows, columns, and sub-grids
    for i in range(9):
        row_set = set()
        col_set = set()
        grid_set = set()
        for j in range(9):
            # Check row
            if puzzle[i][j] != 0 and puzzle[i][j] in row_set:
                return False
            row_set.add(puzzle[i][j])
            
            # Check column
            if puzzle[j][i] != 0 and puzzle[j][i] in col_set:
                return False
            col_set.add(puzzle[j][i])
            
            # Check sub-grid
            row_index = (i // 3) * 3 + j // 3
            col_index = (i % 3) * 3 + j % 3
            if puzzle[row_index][col_index] != 0 and puzzle[row_index][col_index] in grid_set:
                return False
            grid_set.add(puzzle[row_index][col_index])
    
    return True

print("Enter the Sudoku board (9 rows, each row containing 9 space-separated digits, use '0' for empty cells):")
sudoku_board = []
for i in range(9):
    row_input = input().strip()
    row = list(map(int, row_input.split()))
    sudoku_board.append(row)

if is_valid_sudoku(sudoku_board):
    print("The Sudoku puzzle is valid.")
else:
    print("The Sudoku puzzle is not valid.")

