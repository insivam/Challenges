def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")

    for c, row in enumerate(board):
        if 'd' in row:
            dirtr = c
            dirtc = row.index('d')
            break

    if posc < dirtc:
        print("RIGHT")
    elif posc > dirtc:
        print("LEFT")
    
    elif posr < dirtr:
        print("DOWN")
    elif posr > dirtr:
        print("UP")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)