
theBoard = {
    'top-L': '', 'top-M': '', 'top-R':'',
    'mid-L': '', 'mid-M': '', 'mid-R':'',
    'low-L': '', 'low-M': '', 'low-R':'',
}

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

print_board(theBoard)

def isWinner(bo, le):
    return (
            (bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or
            (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or
            (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or
            (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or
            (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or
            (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le)
            )

print("Welcome to Tic Tac Toe!")
turn = "X"

for i in range(9):
    print_board(theBoard)
    print("Turn for " + turn + ". Move on which space? ")
    move = input()
    theBoard[move] = turn

    if isWinner(theBoard, turn):
        print_board(theBoard)
        print("Hoorayy! You have won the game!")
        break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

