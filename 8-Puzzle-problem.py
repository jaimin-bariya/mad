from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Puzzle:
    def __init__(self,board):
        self.board = board
        self.size = 3   # 3x3 puzzle

    def get_blank_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return -1, -1

    def is_goal(self):
        target = [[1,2,3],[4,5,6],[7,8,0]]
        return self.board == target

    def get_neighbors(self,x,y):
        neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board))
            return neighbors

    def __str__(self):
        return '\n'.join(''.join(map(str,row)) for row in self.board)

def dfs(initial_puzzle):
    stack = [initial_puzzle]
    visited = set()

    while stack:
        current_puzzle = stack.pop()
        print(f"Visiting node:\n{current_puzzle}\n")

        if current_puzzle.is_goal():
            print("Goal state reached!")
            return True

        blank_x,blank_y = current_puzzle.get_blank_position()
        for neighbor in current_puzzle.get_neighbors(blank_x,blank_y):
            board_tuple = tuple(tuple(row) for row in neighbor.board)
            if board_tuple not in visited:
                visited.add(board_tuple)
                stack.append(neighbor)

    print("No solution found!")
    return False

    # Initial state of the puzzle
initial_board = [
    [1,2,3],
    [4,5,6],
    [0,7,8]
]

initial_puzzle = Puzzle(initial_board)
dfs(initial_puzzle)