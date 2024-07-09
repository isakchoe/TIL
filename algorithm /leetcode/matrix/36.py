


def check_row(board):
    for i in range(9):
        temp = {}
        for j in range(9):
            value = board[i][j]
            if value != ".":
                if value not in temp:
                    temp[value] = 1
                else:
                    return False

    return True

def check_col(board):
    for i in range(9):
        temp = {}
        for j in range(9):
            value = board[j][i]
            if value != ".":
                if value not in temp:
                    temp[value] = 1
                else:
                    return False
    return True


def check_matrix(board):
    for k in range(0,9,3):
        for m in range(0,9,3):
            dic = {}
            for i in range(k, k+3):
                for j in range(m, m+3):
                    temp = board[i][j]
                    if temp != ".":
                        if temp not in dic:
                            dic[temp] = 1
                        else:
                            return False

    return True




def isValidSudoku(board) -> bool:
    return check_col(board) and check_row(board) and check_matrix(board)




board =[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]


for i in range(9):
    print(board[i])

print(isValidSudoku(board))
