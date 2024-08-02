class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def place_soldier(self, x, y):
        self.board[x][y] = 'S'

    def place_castle(self, x, y):
        self.board[x][y] = 'C'

    def is_soldier(self, x, y):
        return self.board[x][y] == 'S'

    def remove_soldier(self, x, y):
        self.board[x][y] = '.'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

def find_paths(board, start_x, start_y, path, paths):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    current_dir = 0  # Start by moving right
    current_x, current_y = start_x, start_y
    home = (start_x, start_y)

    while True:
        next_x, next_y = current_x + directions[current_dir][0], current_y + directions[current_dir][1]

        if 0 <= next_x < board.size and 0 <= next_y < board.size:
            if board.is_soldier(next_x, next_y):
                path.append(f"Kill ({next_x},{next_y}). Turn Left")
                board.remove_soldier(next_x, next_y)
                current_x, current_y = next_x, next_y
                current_dir = (current_dir + 3) % 4  # Turn left
            else:
                current_x, current_y = next_x, next_y

            if (current_x, current_y) == home:
                path.append(f"Arrive ({home[0]},{home[1]})")
                paths.append(path.copy())
                break
        else:
            break

def main():
    size = 10  # Chessboard size
    num_soldiers = int(input("Enter the number of soldiers: "))
    board = Board(size)

    soldiers = []
    for i in range(num_soldiers):
        x, y = map(int, input(f"Enter coordinates for soldier {i + 1}: ").split(','))
        soldiers.append((x, y))
        board.place_soldier(x, y)

    start_x, start_y = map(int, input("Enter the coordinates for your “special” castle: ").split(','))
    board.place_castle(start_x, start_y)
    board.print_board()

    paths = []
    find_paths(board, start_x, start_y, [f"Start ({start_x},{start_y})"], paths)

    print("Thanks. There are", len(paths), "unique paths for your ‘special_castle’")
    for i, path in enumerate(paths):
        print(f"\nPath {i + 1}:\n{'='*7}")
        for step in path:
            print(step)

if __name__ == "__main__":
    main()
