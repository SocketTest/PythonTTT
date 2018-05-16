import os
import random
class GameBoard:
    def __init__(self):
        self.board=list(range(1,10))
    def printBoard(self):
        os.system("clear")
        print("|-----" * 3 + "|")
        for i in range(3):
            print("|     " * 4)
            print("|  " +  str(self.board[0 + i * 3])+ "  |  "+ str(self.board[1 + i * 3])+ "  |  "+ str(self.board[2 + i * 3])+ "  |")
            print("|     " * 4)
            print("|-----" * 3 + "|")

class CPU_player:
    # def __init__(self,board):
    #     self.board = board
    def stupid_player (self):
        move = random.randint(1, 9)
        # self.board[move - 1] = player_side
        return move


class Game:


    def __init__(self,board):
        self.board = board

    move_counter = 0
    def greeting(self):
        ok = False

        while ok is False:
            os.system("clear")
            print("     1. Game for 2 players")
            print("     2. Game for 1 player vs CPU")
            # print("     3. CPU vs CPU")
            print(" ")
            side = int(input("     Make a choice!"))
            if side <= 2 and side >= 1:

                ok = True
            else:
                ok = False
            if side == 2 and ok == True:

                os.system("clear")
                side = raw_input("     Choose your side X or O ?")
                if  side == "O" or side == "0" or side == "o":
                    side = "X"
                    ok = True
                elif side == "X" or side == "x":
                    side = "O"
                    ok = True

                else:
                    ok = False
        if side == "1":
            return False
        else:
            return side

    def check_win(self):

        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]

        return False

    def inputPlayer(self,player,cpu):
        valid = False
        while not valid:
            if cpu:
                player_answer = CPU_player().stupid_player()
            else:
                try:
                    player_answer = input("  Select the cell where to put " + player + "? ")

                    player_answer = int(player_answer)
                except:
                    print ("Not a number")
                    continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(self.board[player_answer - 1]) not in "XO"):
                    self.board[player_answer - 1] = player
                    valid = True
                else:
                    if not cpu:
                        print("     The cell is busy!")
            else:
                print("     Invalid number")



if __name__ == '__main__':

    game_board = GameBoard()
    game = Game(game_board.board)
    cpu_player = CPU_player()
    os.system("clear")
    cpu_side = game.greeting()
    game_board.printBoard()

    while True:

        if cpu_side == "X":
            game.inputPlayer("X",True)
            game_board.printBoard()

        else:
            game.inputPlayer("X", False)
            game_board.printBoard()
        # move_counter += 1
        temp = game.check_win()
        if temp:
            break


        if cpu_side == "O":
            game.inputPlayer("O", True)
            game_board.printBoard()
        else:
            game.inputPlayer("O", False)
            game_board.printBoard()
        # move_counter += 1
        temp = game.check_win()
        if temp:
            break

    if (temp == "nhw"):
        print ("     Nobody has won :-P")
    else:
        print("     " +str(temp) + "is Winner !")
    while True:
        a=0










