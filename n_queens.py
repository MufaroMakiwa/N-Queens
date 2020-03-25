def create_board(n):
    '''
    Creates a board with the given dimension
    '''

    return [[' ' for i in range(n)] for j in range(n)]


def isvalid(covered, pos):
    '''
    Checks to see if the empty position is a valid space or not
    Covered is as set that contains all the cells covered so far by the placed queens
    '''
    
    return pos not in covered
   


def traversed_cells(pos, n):
    '''
    Given a position, return a generator for all the cells that a
    queen a pos can attack
    '''

    r, c = pos
    cells = []
    cells.append(((r-i, c+i) for i in range(1, n) if all(0 <= j < n for j in (r-i, c+i))))
    cells.append(((r+i, c-i) for i in range(1, n) if all(0 <= j < n for j in (r+i, c-i))))
    cells.append(((r-i, c-i) for i in range(1, n) if all(0 <= j < n for j in (r-i, c-i))))
    cells.append(((r+i, c+i) for i in range(1, n) if all(0 <= j < n for j in (r+i, c+i))))
    cells.append(((i, c) for i in range(0, n)))
    cells.append(((r, i) for i in range(0, n)))

    return cells


def print_board(n):
    '''
    Prints the chess board in a specific format
    '''

    board = place_queens(n)
    if not board:
        print(None)
    else:
        for i in range(n):
            if i==0:
                print(' - -' * n + ' -')
        
            for j in range(n + 1):
                if j == n:
                    print(' | ')
                    break
                else:
                    print(' | '+str(board[i][j]), end='')
            print(' - -' * n + ' -')

def set_position(board, pos, val):
    '''
    Given a board, change the element at pos to val
    '''
    board[pos[0]][pos[1]] = val


def place_queens(n):
    '''
    Solves the N queens problem. Will try to count the number of possible solutions
    '''

    if n == 0: return None
    board = create_board(n)
    queen_positions = []
   

    def solve(covered = set(), row = 0):
        '''
        Recursively places queens on the board using the backtracking algorithm
        Return the board object if a solution exist else return None
        '''
        
        original_covered = set(covered)
        if row == n:
            return True

        else:
            for cell in empty_cells(n, row):
                if not isvalid(covered, cell):
                    continue

                for generator in traversed_cells(cell, n):
                    for pos in generator:
                        covered.add(pos)
    
                queen_positions.append(cell)
                set_position(board, cell, 'Q')

                if solve(covered, row + 1):
                    return board
                
                covered = set(original_covered)
                queen_positions.remove(cell)
                set_position(board, cell, ' ')
            return None
    return solve()
    

def empty_cells(n, row):
    '''
    Yield an empty cell from the board
    '''
    for col in range(n):
        yield (row, col)

if __name__ == '__main__':
    print_board(15)



