import time
def move(shift, board):
    for i in range(shift):
        board.append(board[0])
        board.remove(board[0])
    return board
shift1 = int(input('Сдвиг: '))
board1 = list(input('Ведите список: '))

while True:
    print(''.join(map(str, move(shift1, board1))))
    time.sleep(1)