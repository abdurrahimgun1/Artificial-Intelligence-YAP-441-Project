from tkinter import *
import search
from sokoPuzzle import *
from node import *
import time

board1 = [['O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'S', ' ', 'B', ' ', 'O'],
          ['O', ' ', 'O', 'R', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O']]

board2 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
          ['O', ' ', ' ', 'O', 'O', 'O', ' ', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'O', '.', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
          ['O', ' ', ' ', 'B', ' ', ' ', 'O', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board3 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', ' ', ' ', ' ', 'O', ' ', ' ', 'O'],
          ['O', ' ', ' ', 'B', 'R', ' ', ' ', 'O'],
          ['O', ' ', ' ', ' ', 'O', 'B', ' ', 'O'],
          ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
          ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board4 = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
          ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
          ['O', 'O', ' ', '*', ' ', ' ', 'O'],
          ['O', 'O', 'B', 'O', 'B', ' ', 'O'],
          ['O', ' ', 'S', 'R', 'S', ' ', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'O', 'O'],
          ['O', 'O', 'O', ' ', ' ', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O']]

board5 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'S', 'O', ' ', ' ', 'O', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'B', ' ', 'O', 'O'],
          ['O', ' ', 'B', ' ', 'R', ' ', ' ', 'S', 'O'],
          ['O', 'O', 'O', ' ', 'O', ' ', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'B', 'O', ' ', 'O', 'O', 'O'],
          ['O', 'O', 'O', ' ', ' ', 'S', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board8 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', ' ', 'R', ' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O'],
          ['O', ' ', 'B', ' ', 'B', ' ', 'B', ' ', ' ', ' ', 'O'],
          ['O', ' ', 'B', 'O', 'O', 'O', 'O', ' ', 'B', ' ', 'O'],
          ['O', 'O', ' ', ' ', 'S', 'S', 'S', 'O', ' ', 'O', 'O'],
          ['O', 'O', 'S', 'S', 'S', '*', ' ', 'B', ' ', ' ', 'O'],
          ['O', 'O', ' ', 'O', '*', ' ', 'O', ' ', ' ', ' ', 'O'],
          ['O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard1 = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'S', ' ', 'O', ' ', 'R', 'O'],
            ['O', ' ', ' ', 'O', 'B', ' ', 'O'],
            ['O', 'S', ' ', ' ', 'B', ' ', 'O'],
            ['O', ' ', ' ', 'O', 'B', ' ', 'O'],
            ['O', 'S', ' ', 'O', ' ', ' ', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard2 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'S', 'S', 'S', ' ', 'O', 'O', 'O'],
            ['O', ' ', 'S', ' ', 'B', ' ', ' ', 'O'],
            ['O', ' ', ' ', 'B', 'B', 'B', ' ', 'O'],
            ['O', 'O', 'O', 'O', ' ', ' ', 'R', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard3 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', ' ', ' ', ' ', ' ', 'O', 'O', 'O'],
            ['O', ' ', ' ', ' ', 'B', ' ', ' ', 'O'],
            ['O', 'S', 'S', 'S', '*', 'B', 'R', 'O'],
            ['O', ' ', ' ', ' ', 'B', ' ', ' ', 'O'],
            ['O', ' ', ' ', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard4 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'S', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', ' ', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'S', ' ', 'S', ' ', 'O', 'O', 'O', 'O'],
            ['O', ' ', 'B', ' ', 'B', 'B', ' ', ' ', 'O'],
            ['O', 'O', 'O', 'S', ' ', ' ', 'B', 'R', 'O'],
            ['O', 'O', 'O', ' ', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]


class Gui:
    def __init__(self, board, search_algo, deadlock_detection, type="watch", num_step_level=0):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=63 * self.width, height=63 * self.height)
        self.canvas.pack()
        self.search_algo = search_algo
        self.final_steps = False
        self.legnth_solution = 0
        self.num_steps = 0
        self.deadlock_detection = deadlock_detection
        self.type = type
        self.num_step_level = num_step_level

        self.button = Button(self.window, text="Exit", padx=10, bg='#263D42', pady=4, command=self.close)
        self.button.pack(side=RIGHT)

        self.button = Button(self.window, text="Back", padx=10, bg='#263D42', pady=4, command=self.Back)
        self.button.pack(side=LEFT)

        if self.type == "watch":
            self.button = Button(self.window, text="Start", padx=10, bg='#263D42', pady=4, command=self.start)
            self.button.pack()

        if self.type == "play":
            self.step_parcouru = 0
            self.initial_node, self.sokoPuzzle = create_initial_node(self.board, type='play')
            self.window.bind('<KeyPress>', self.move)  #

        Node.deadlock_map = []
        self.draw_board()

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def start(self):
        show_solution(self, self.board, self.search_algo, self.deadlock_detection, self.window)

    def close(self):
        self.window.destroy()

    def Back(self):
        self.window.destroy()
        Level(self.search_algo, self.deadlock_detection, type=self.type)

    def draw_board(self, final_steps=False):
        self.obstacle = PhotoImage(file="images/obstacle.png")
        self.vide = PhotoImage(file="images/vide.png")
        self.cible = PhotoImage(file="images/cible.png")
        self.cibla = PhotoImage(file="images/cibla.png")
        self.robot = PhotoImage(file="images/robot.png")
        self.bloc = PhotoImage(file="images/bloc.png")
        self.blocible = PhotoImage(file="images/blocible.png")
        self.DeadCoin = PhotoImage(file="images/DeadCoin.png")
        self.DeadLigne = PhotoImage(file="images/DeadLigne.png")

        for i, j in itertools.product(range(self.height), range(self.width)):
            if self.board[i][j] == 'O':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.obstacle)
            elif self.board[i][j] == 'S':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.vide)
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.cible)
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.cibla)
            elif self.board[i][j] == 'B':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.bloc)
            elif self.board[i][j] == 'R':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.vide)
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.robot)
            elif self.board[i][j] == '*':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.blocible)
            elif self.board[i][j] == '.':
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.vide)
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.cible)
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.robot)
            else:
                self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.vide)

            try:
                if self.deadlock_detection:
                    if Node.deadlock_map[i][j] == 'D':
                        self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.DeadCoin)
                    elif Node.deadlock_map[i][j] == 'L':
                        self.canvas.create_image(63 * j, 63 * i, anchor=NW, image=self.DeadLigne)
            except:
                pass

        if self.final_steps:
            if self.deadlock_detection:
                self.label = Label(self.window, text="The " + self.search_algo + " with deadlock detection : ",
                                   bg='green', fg='white')
            else:
                self.label = Label(self.window,
                                   text="L'algorithme de " + self.search_algo + " without deadlock detection : ",
                                   bg='green', fg='white')
            self.label.pack()
            self.label = Label(self.window, text="Number of steps used by this algorithm : " + str(self.num_steps),
                               bg='#c45242', fg='white')
            self.label.pack()

            self.label = Label(self.window, text="Minimum number of steps to win is : " + str(self.legnth_solution),
                               bg='#c45242', fg='white')
            self.label.pack()

    def update_board(self, board, final_steps=False, legnth_solution=0, num_steps=0):
        self.final_steps = final_steps
        self.legnth_solution = legnth_solution
        self.num_steps = num_steps
        self.board = board
        self.canvas.delete("all")
        self.draw_board()
        self.window.update()


class start_game_class:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=300, height=300)
        self.canvas.pack()

        self.bg = PhotoImage(file="images/bg.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)

        self.button0 = Button(self.window, text="Start game", padx=5, bg='#33EE88', pady=2, command=self.start_game)
        button0_canvas = self.canvas.create_window(115, 260,
                                                   anchor="nw",
                                                   window=self.button0)

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def start_game(self):
        self.window.destroy()
        choice()


class choice:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)

        self.button1 = Button(self.window, text="Watch the algorithms in action", padx=5, bg='#33EE88', pady=3,
                              font=("Arial", 13), command=self.start_game2)
        button1_canvas = self.canvas.create_window(60, 220,
                                                   anchor="nw",
                                                   window=self.button1)

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def start_game(self):
        self.window.destroy()
        Level(type='play')

    def start_game2(self):
        self.window.destroy()
        search_method()


class search_method:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)

        self.button0 = Button(self.window, text="Back", padx=5, bg='#537365', pady=2, command=self.Back)
        button0_canvas = self.canvas.create_window(20, 20,
                                                   anchor="nw",
                                                   window=self.button0)
        self.button0 = Button(self.window, text="Exit", padx=5, bg='#537365', pady=2, command=self.Exit)
        button0_canvas = self.canvas.create_window(350, 20,
                                                   anchor="nw",
                                                   window=self.button0)

        self.label = Label(self.window, text="Choose a search method :", bg='#c45242', font=("Arial", 18))
        self.label.config(padx=3, pady=2, borderwidth=2)
        label_canvas = self.canvas.create_window(20, 60,
                                                 anchor="nw",
                                                 window=self.label)

        self.button0 = Button(self.window, text="Breadth First", padx=5, bg='#559776', font=("Arial", 13), pady=1,
                              command=self.BFS)
        button0_canvas = self.canvas.create_window(70, 100,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="Astar with heuristic 1", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.Astar1)
        button0_canvas = self.canvas.create_window(70, 140,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="Astar with heuristic 2", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.Astar2)
        button0_canvas = self.canvas.create_window(70, 180,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="Astar with heuristic 3", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.Astar3)
        button0_canvas = self.canvas.create_window(70, 220,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="IDAstar with heuristic 1", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.IDAstar1)
        button0_canvas = self.canvas.create_window(70, 260,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="IDAstar with heuristic 2", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.IDAstar2)
        button0_canvas = self.canvas.create_window(70, 300,
                                                   anchor="nw",
                                                   window=self.button0)

        self.button0 = Button(self.window, text="IDAstar with heuristic 3", padx=5, bg='#559776', font=("Arial", 13),
                              pady=1, command=self.IDAstar3)
        button0_canvas = self.canvas.create_window(70, 340,
                                                   anchor="nw",
                                                   window=self.button0)

        self.var = IntVar()

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        choice()

    def Exit(self):
        self.window.destroy()

    def BFS(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False

        Level("BFS", deadlock_detection, "watch")

    def Astar1(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic1", deadlock_detection, "watch")

    def Astar2(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic2", deadlock_detection, "watch")

    def Astar3(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic3", deadlock_detection, "watch")

    def IDAstar1(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("IDAstar,heuristic1", deadlock_detection, "watch")

    def IDAstar2(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("IDAstar,heuristic2", deadlock_detection, "watch")

    def IDAstar3(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("IDAstar,heuristic3", deadlock_detection, "watch")


class Level:
    def __init__(self, search_algo="BFS", deadlock_detection=False, type="watch"):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.search_algo = search_algo
        self.deadlock_detection = deadlock_detection
        self.type = type

        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)

        self.button0 = Button(self.window, text="Back", padx=5, bg='#537365', pady=2, command=self.Back)
        button0_canvas = self.canvas.create_window(20, 20,
                                                   anchor="nw",
                                                   window=self.button0)
        self.button0 = Button(self.window, text="Exit", padx=5, bg='#537365', pady=2, command=self.Exit)
        button0_canvas = self.canvas.create_window(350, 20,
                                                   anchor="nw",
                                                   window=self.button0)
        self.button1 = Button(self.window, text="Level 1", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level1)
        button1_canvas = self.canvas.create_window(70, 70,
                                                   anchor="nw",
                                                   window=self.button1)

        self.button2 = Button(self.window, text="Level 2", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level2)
        button2_canvas = self.canvas.create_window(70, 120,
                                                   anchor="nw",
                                                   window=self.button2)
        self.button3 = Button(self.window, text="Level 3", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level3)
        button3_canvas = self.canvas.create_window(70, 170,
                                                   anchor="nw",
                                                   window=self.button3)
        self.button4 = Button(self.window, text="Level 4", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level4)
        button4_canvas = self.canvas.create_window(70, 220,
                                                   anchor="nw",
                                                   window=self.button4)
        self.button5 = Button(self.window, text="Level 5", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level5)
        button5_canvas = self.canvas.create_window(70, 270,
                                                   anchor="nw",
                                                   window=self.button5)

        self.buttonEXTRA1 = Button(self.window, text="EXTRA Level 1", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                                   command=self.levelEXTRA1)
        buttonEXTRA1_canvas = self.canvas.create_window(200, 70,
                                                        anchor="nw",
                                                        window=self.buttonEXTRA1)

        self.buttonEXTRA2 = Button(self.window, text="EXTRA Level 2", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                                   command=self.levelEXTRA2)
        buttonEXTRA2_canvas = self.canvas.create_window(200, 120,
                                                        anchor="nw",
                                                        window=self.buttonEXTRA2)

        self.buttonEXTRA3 = Button(self.window, text="EXTRA Level 3", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                                   command=self.levelEXTRA3)
        buttonEXTRA3_canvas = self.canvas.create_window(200, 170,
                                                        anchor="nw",
                                                        window=self.buttonEXTRA3)

        self.buttonEXTRA4 = Button(self.window, text="EXTRA Level 4", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                                   command=self.levelEXTRA4)
        buttonEXTRA4_canvas = self.canvas.create_window(200, 220,
                                                        anchor="nw",
                                                        window=self.buttonEXTRA4)

        self.button8 = Button(self.window, text="EXTRA Level X", padx=5, bg='#c45242', pady=2, font=("Arial", 13),
                              command=self.level8)
        button8_canvas = self.canvas.create_window(200, 270,
                                                   anchor="nw",
                                                   window=self.button8)

        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        if self.type == "watch":
            search_method()
        elif self.type == "play":
            choice()

    def Exit(self):
        self.window.destroy()

    def level1(self):
        self.window.destroy()
        Gui(board1, self.search_algo, self.deadlock_detection, self.type, 4)

    def level2(self):
        self.window.destroy()
        Gui(board2, self.search_algo, self.deadlock_detection, self.type, 29)

    def level3(self):
        self.window.destroy()
        Gui(board3, self.search_algo, self.deadlock_detection, self.type, 33)

    def level4(self):
        self.window.destroy()
        Gui(board4, self.search_algo, self.deadlock_detection, self.type, 30)

    def level5(self):
        self.window.destroy()
        Gui(board5, self.search_algo, self.deadlock_detection, self.type, 25)

    def level8(self):
        self.window.destroy()
        Gui(board8, self.search_algo, self.deadlock_detection, self.type, 0)

    def levelEXTRA1(self):
        self.window.destroy()
        Gui(EXboard1, self.search_algo, self.deadlock_detection, self.type, 41)

    def levelEXTRA2(self):
        self.window.destroy()
        Gui(EXboard2, self.search_algo, self.deadlock_detection, self.type, 55)

    def levelEXTRA3(self):
        self.window.destroy()
        Gui(EXboard3, self.search_algo, self.deadlock_detection, self.type, 30)

    def levelEXTRA4(self):
        self.window.destroy()
        Gui(EXboard4, self.search_algo, self.deadlock_detection, self.type, 83)


def create_initial_node(board=None, type='watch'):
    height = len(board)
    width = len(board[0])

    tab_dyn = [[''] * width for _ in range(height)]
    tab_stat = [[''] * width for _ in range(height)]
    deadlock_map = [[''] * width for _ in range(height)]

    for i, j in itertools.product(range(height), range(width)):
        if board[i][j] == 'R':
            robot_position = (i, j)
            tab_dyn[i][j] = 'R'
            tab_stat[i][j] = ' '
        elif board[i][j] == 'B':
            tab_dyn[i][j] = 'B'
            tab_stat[i][j] = ' '
        elif board[i][j] == 'S' or board[i][j] == 'O' or board[i][j] == ' ':
            tab_dyn[i][j] = ' '
            tab_stat[i][j] = board[i][j]
        elif board[i][j] == '*':
            tab_dyn[i][j] = 'B'
            tab_stat[i][j] = 'S'
        else:
            robot_position = (i, j)
            tab_dyn[i][j] = 'R'
            tab_stat[i][j] = 'S'

    Node.tab_stat = tab_stat

    for i, j in itertools.product(range(height), range(width)):
        if (tab_stat[i][j] == ' ' and tab_stat[i][j - 1] == 'O' and tab_stat[i - 1][j] == 'O') or (
                tab_stat[i][j] == ' ' and tab_stat[i][j + 1] == 'O' and tab_stat[i - 1][j] == 'O') or (
                tab_stat[i][j] == ' ' and tab_stat[i][j - 1] == 'O' and tab_stat[i + 1][j] == 'O') or (
                tab_stat[i][j] == ' ' and tab_stat[i][j + 1] == 'O' and tab_stat[i + 1][j] == 'O'):
            deadlock_map[i][j] = 'D'
        else:
            deadlock_map[i][j] = ' '

    for i, j in itertools.product(range(height), range(width)):

        if deadlock_map[i][j] == 'D':
            if tab_stat[i][j - 1] == 'O' and tab_stat[i - 1][j] == 'O':

                deadlock_line = False
                for k in range(j + 1, width):
                    if deadlock_map[i][k] == 'D':
                        deadlock_line = True
                        break
                    elif Node.tab_stat[i][k] != ' ' or Node.tab_stat[i - 1][k] != 'O':
                        deadlock_line = False
                        break
                if deadlock_line:
                    for k in range(j + 1, k):
                        deadlock_map[i][k] = 'L'

                deadlock_line = False
                for k in range(i + 1, height):
                    if deadlock_map[k][j] == 'D':
                        deadlock_line = True
                        break
                    elif Node.tab_stat[k][j] != ' ' or Node.tab_stat[k][j - 1] != 'O':
                        deadlock_line = False
                        break
                if deadlock_line:
                    for k in range(i + 1, k):
                        deadlock_map[k][j] = 'L'

            elif tab_stat[i][j + 1] == 'O' and tab_stat[i + 1][j] == 'O':
                deadlock_line = False
                for k in range(j - 1, 0, -1):
                    if deadlock_map[i][k] == 'D':
                        deadlock_line = True
                        break
                    elif Node.tab_stat[i][k] != ' ' or Node.tab_stat[i + 1][k] != 'O':
                        deadlock_line = False
                        break
                if deadlock_line:
                    for k in range(j - 1, k, -1):
                        deadlock_map[i][k] = 'L'

                deadlock_line = False
                for k in range(i - 1, 0, -1):
                    if deadlock_map[k][j] == 'D':
                        deadlock_line = True
                        break
                    elif Node.tab_stat[k][j] != ' ' or Node.tab_stat[k][j + 1] != 'O':
                        deadlock_line = False
                        break
                if deadlock_line:
                    for k in range(i - 1, k, -1):
                        deadlock_map[k][j] = 'L'

    Node.deadlock_map = deadlock_map
    sokoPuzzle = SokoPuzzle(tab_dyn, robot_position)
    initial_node = Node(sokoPuzzle)
    if type == 'watch':
        return initial_node
    else:
        return initial_node, sokoPuzzle


def show_solution(gui, board, search_algo, deadlock_detection, window):
    initial_node = create_initial_node(board=board)
    if search_algo == 'BFS':
        goalNode, num_steps = search.breadthFirst(initial_node, window, deadlock_detection)
    elif search_algo == 'Astar,heuristic1':
        goalNode, num_steps = search.Astar(initial_node, window, 1, deadlock_detection)
    elif search_algo == 'Astar,heuristic2':
        goalNode, num_steps = search.Astar(initial_node, window, 2, deadlock_detection)
    elif search_algo == 'Astar,heuristic3':
        goalNode, num_steps = search.Astar(initial_node, window, 3, deadlock_detection)
    elif search_algo == 'IDAstar,heuristic1':
        goalNode, num_steps = search.IDAstar(initial_node, window, 1, deadlock_detection)
    elif search_algo == 'IDAstar,heuristic2':
        goalNode, num_steps = search.IDAstar(initial_node, window, 2, deadlock_detection)
    elif search_algo == 'IDAstar,heuristic3':
        goalNode, num_steps = search.IDAstar(initial_node, window, 3, deadlock_detection)
    if goalNode:
        solution = goalNode.getSolution()
        for action in solution:
            gui.update_board(action)
            time.sleep(0.05)
        gui.update_board(action, True, len(solution) - 1, num_steps)
    else:
        labelerreur = Label(window, text=f'Optimal solution not found', bg='#c45242', fg='white')
        labelerreur.pack()
        window.update()