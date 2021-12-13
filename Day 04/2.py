input_file = open("./bingo.txt","r")

bingo_temp = input_file.readlines()
nothing_important = [x for x in bingo_temp]
bingo = [elem.split() for elem in nothing_important]

input_file.close()

def replace_with_minus_one(lista, n):
    for board in lista:
        for row in board:
            for i in range(5):
                if(row[i] == n):
                    row[i] = -1
                    
def is_bingo_on_board(board):
    size = len(board)
    for i in range(size):
        sum_column = 0
        if sum(board[i]) == -size:
            return True
        for row in board:
            sum_column += row[i]
        if sum_column == -size:
            return True
    else:
        return False

numbers = [int(x) for x in bingo[0][0].split(",")]

bingo = [x for x in bingo[1:] if len(x) != 0]

boards = []

for i in range(0, len(bingo), 5):
    temp_list = []
    temp_list.append([int(x) for x in bingo[i]])
    temp_list.append([int(x) for x in bingo[i+1]])
    temp_list.append([int(x) for x in bingo[i+2]])
    temp_list.append([int(x) for x in bingo[i+3]])
    temp_list.append([int(x) for x in bingo[i+4]])
    boards.append(temp_list)

losing_board = []
last_number = 0

for n in numbers:
    replace_with_minus_one(boards, n)
    for board in boards:
        if is_bingo_on_board(board) == True:
            boards.remove(board)
    if len(boards) == 1:
        losing_board = boards[0]
    if len(boards) == 0:
        last_number = n        
        break 

losing_board = [x for x in losing_board for x in x]
losing_board = [x for x in losing_board if x != -1]

print(sum(losing_board*last_number))

