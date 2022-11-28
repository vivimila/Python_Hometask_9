# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))

winning_cases = [(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8,),(3,6,9)]

def game_board():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
    print("-------------")

def input_an_action (entering):
    while True:
        value = input ("Сделайте ход. Выберите ячейку для: " + entering)  
        if not (value in "123456789"):
            print("Неверный ввод. Повторите попытку")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("УПС! Место занято. Повторите попытку")
            continue
        board[value -1] = entering
        break

def who_is_winner():
    for each in winning_cases:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
          return board[each[1]-1]  
    else:
        return False

def game():
    count = 0
    while True: 
        game_board()
        if count % 2 == 0:
            input_an_action("X")
        else:
            input_an_action("O")
        if count > 3:
           winner = who_is_winner()
           if winner:
                game_board()
                print(winner, "Победитель!")
                break
        count += 1
        if count > 8:
            game_board()
            print("Ничья")
            break

game()