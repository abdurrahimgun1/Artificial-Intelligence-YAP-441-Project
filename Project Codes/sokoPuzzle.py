import numpy as np

""" Representations:
O => Obstacle
S => Storage
B => Block
R => Robot
* => Block on a storage
. => Robot on a storage """


class SokoPuzzle:

    def __init__(self, tab_dyn, robot_position):
        self.tab_dyn = tab_dyn
        self.robot_position = robot_position

        self.moves = ["U", "D", "L", "R"]

    def isDeadLock(self, deadlock_map):
        S_indices_x, S_indices_y = np.where(np.logical_or(np.array(deadlock_map) == 'D', np.array(deadlock_map) == 'L'))

        for ind_x, ind_y in zip(S_indices_x, S_indices_y):
            if self.tab_dyn[ind_x][ind_y] == 'B':
                return True
        return False

        S_indices_x, S_indices_y = np.where(np.array(tab_stat) == 'S')

        for ind_x, ind_y in zip(S_indices_x, S_indices_y):
            if self.tab_dyn[ind_x][ind_y] != 'B':
                return False
        return True

    def isGoal(self, tab_stat):
        S_indices_x, S_indices_y = np.where(np.array(tab_stat) == 'S')
        for ind_x, ind_y in zip(S_indices_x, S_indices_y):
            if self.tab_dyn[ind_x][ind_y] != 'B':
                return False
        return True

    def executeMove(self, action, tab_stat):
        if action == "U":
            return (self.up(tab_stat))
        if action == "D":
            return (self.down(tab_stat))
        if action == "L":
            return (self.left(tab_stat))
        if action == "R":
            return (self.right(tab_stat))

    def up(self, tab_stat):
        robot_x, robot_y = self.robot_position

        robot_x = robot_x - 1

        if self.tab_dyn[robot_x][robot_y] == 'B':
            box_x, box_y = robot_x - 1, robot_y
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x + 1][robot_y] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True

        else:
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x + 1][robot_y] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                return True

        return False

    def down(self, tab_stat):
        robot_x, robot_y = self.robot_position

        robot_x = robot_x + 1

        if self.tab_dyn[robot_x][robot_y] == 'B':
            box_x, box_y = robot_x + 1, robot_y
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x - 1][robot_y] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True

        else:
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x - 1][robot_y] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                return True

        return False

    def left(self, tab_stat):
        robot_x, robot_y = self.robot_position
        robot_y = robot_y - 1

        if self.tab_dyn[robot_x][robot_y] == 'B':
            box_x, box_y = robot_x, robot_y - 1
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y + 1] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True

        else:
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y + 1] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                return True

        return False

    def right(self, tab_stat):
        robot_x, robot_y = self.robot_position

        robot_y = robot_y + 1

        if self.tab_dyn[robot_x][robot_y] == 'B':
            box_x, box_y = robot_x, robot_y + 1
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y - 1] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True

        else:
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y - 1] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'
                return True

        return False