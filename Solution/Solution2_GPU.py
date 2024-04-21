import torch

# Check if a GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    print("没有启用GPU，采用默认CPU运行!")
    device = torch.device("cpu")


# Function to solve N-Queens problem on GPU
def n_queen_gpu(n):
    if n == 0:
        return []

    # Create the chessboard on the GPU
    board = torch.full((n, n), ord('#'), dtype=torch.long, device=device)

    result = []

    def convert_to_board(board):
        return [[chr(cell) for cell in row] for row in board]

    def put(row):
        if row == n:
            result.append(convert_to_board(board.cpu().numpy()))
            return
        for i in range(n):
            if board[row][i] == ord('#') and all(board[j][i] == ord('#') for j in range(row)) and all(board[j][k] == ord('#') for j, k in zip(range(row, -1, -1), range(i, -1, -1))) and all(board[j][k] == ord('#') for j, k in zip(range(row, -1, -1), range(i, n))):
                board[row][i] = ord('Q')
                put(row + 1)
                board[row][i] = ord('#')

    put(0)
    return result


def Run(i: int):
    return n_queen_gpu(i)
