import unittest
from main import CPU_player
from  main import Game
from  main import GameBoard





class test_CPU_player_module(unittest.TestCase):

    def test_rundom_number_cpu_player(self):
        for i in range(10000):
            cpu = CPU_player().stupid_player()
            self.assertIn(cpu,range(1,10))

class test_input_player_module(unittest.TestCase):

    def test_check_win_with_clear_board(self):
        gb = GameBoard().board
        chw = Game(gb).check_win()
        self.assertFalse(chw)

    def test_check_win_with_correct_positions_X(self):
        test_mas = (("X","X","X", 4, 5, 6, 7, 8, 9),
                  (1, 2, 3, "X", "X", "X", 7, 8, 9,),
                  (1, 2, 3, 4, 5, 6, "X", "X", "X",),
                  ("X", 2, 3, "X", 5, 6, "X", 8, 9,),
                  (1, "X", 3, 4, "X", 6, 7, "X", 9,),
                  (1, 2, "X", 4, 5, "X", 7, 8, "X",),
                  ("X", 2, 3, 4, "X", 6, 7, 8, "X",),
                  (1, 2, "X", 4, "X", 6, "X", 8, 9,)
                  )
        for gb in test_mas:
            chw = Game(gb).check_win()
            self.assertTrue(chw)

    def test_check_win_with_correct_positions_0(self):
        test_mas = (("O","O","O", 4, 5, 6, 7, 8, 9),
                  (1, 2, 3, "O", "O", "O", 7, 8, 9,),
                  (1, 2, 3, 4, 5, 6, "O", "O", "O",),
                  ("O", 2, 3, "O", 5, 6, "O", 8, 9,),
                  (1, "O", 3, 4, "O", 6, 7, "O", 9,),
                  (1, 2, "O", 4, 5, "O", 7, 8, "O",),
                  ("O", 2, 3, 4, "O", 6, 7, 8, "O",),
                  (1, 2, "O", 4, "O", 6, "O", 8, 9,)
                  )
        for gb in test_mas:
            chw = Game(gb).check_win()
            self.assertTrue(chw)

    def test_check_win_with_uncorrect_positions_X(self):
        test_mas = ((1,"X", 3, 4,5,"X",7,"X",9),
                    ("X", 2, 3, "X", "X", 6, 7, 8, 9),
                    (1, "X", 3, "X", 5, "X", 7, 8, 9),
                    ("X", "X", 3, 4, 5, 6, 7, 8, "X"),
                    (1, 2, "X", 4, "X", 6, 7, "X", "X"),
                    (1, 2, "X", "X", "X", 8, 7, 8, 9),
                    (1, 2, "X", "X", 5, "X", "X", 8, 9),
                    (1, "X", 3, 4, 5, 6, 7, "X", 9),

                  )
        for gb in test_mas:
            chw = Game(gb).check_win()
            self.assertFalse(chw)

    def test_check_win_with_uncorrect_positions_0(self):
        test_mas = (("O", "O", 3, 4, 5, 6, 7, 8, "O"),
                    (1, "O", 3, "O", 5, "O", 7, 8, 9),
                    ("O", "O", 3, "O", 5, 6, 7, 8, 9),
                    (1, 2, 3, 4, 5, "O", 7, 8, "O"),
                    (1, 2, 3, "O", 5, 6, 7, 8, 9),
                    (1, 2, "O", 4, 5, 6, "O", 8, "O"),
                    (1, "O", 3, "O", 5, 6, "O", 8, 9),
                    ("O", 2, "O", 4, "O", 6, 7, "O", 9),
                  )
        for it in test_mas:
            chw = Game(it).check_win()
            self.assertFalse(chw)


    def test_check_win_with_wit_garbage(self):
        test_mas = (("a", 2, "ty", "X", 5, 6, 7, "O", 9),
                    (1, 2, "X", "X", "X", 6, 7, 8, 9),
                    (1, "O", 3, "r", "67", "O", 7, 8, 9),
                    ("O", "@", "X", "l", 5, "D", 7, "X", 9),
                    ("*", 2, "4", "]", "|", 6, 7, 8, "X"),
                    (1, "X", 3, 4, "O", 6, 7, "O", 9),
                    (1, 2, 3, "X", "X", "O", 7, 0x45, 9),
                    (1, "O", 3, "F", 5, "f", 7, 8, ),
                    )
        for it in test_mas:
            chw = Game(it).check_win()
            self.assertFalse(chw)



if __name__ == '__main__':
    unittest.main()
