# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))
def draw_board(board):
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

def put_sign(sign):
    check = False
    while not check:
        text = input("Where you'd like to put " + sign+": ")
        try:
            cell = int(text)
        except:
            print ("Error: check your input")
            continue
        if cell >= 1 and cell <= 9:
            if (str(board[cell-1]) not in "XO"):
                board[cell-1] = sign
                check = True
            else:
                print ("Error: this cell is not empty")
        else:
            print ("Error: print the figure from 1 to 9")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for cell in win_coord:
        if board[cell[0]] == board[cell[1]] == board[cell[2]]:
            return board[cell[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            put_sign("X")
        else:
            put_sign("O")
        counter += 1
        if counter > 4:
            if check_win(board):
                print(f"{check_win(board)}'s won")
                win = True
                break
        if counter == 9:
            print ("Nobody's won")
            break
    draw_board(board)

if __name__ == "__main__":
    main(board)