import os

class Maze:
    #rows = 0
    #columns = 0
    #pacmanPos = (0, 0)
    #isPacmanOnLevel = False
    #isPacmanLookingUp = False
    #isPacmanLookingRight = False
    #isPacmanLookingDown = False
    #isPacmanLookingLeft = False

    def __init__(self, r, c):
        self.__rows = r
        self.__columns = c
        self.__pacmanPos = (0, 0)
        self.__isPacmanOnLevel = False
        self.__isPacmanLookingUp = False
        self.__isPacmanLookingRight = False
        self.__isPacmanLookingDown = False
        self.__isPacmanLookingLeft = False

        #for rows in range(self.rows):
        #    for columns in range(self.columns):
        #        print(" * ", end="")
        #    print("\n")

    def setPacmanAt(self, r, c):
        self.__pacmanPos = (r, c)
        self.__isPacmanOnLevel = True
        self.restartPacmanLook()
        self.__isPacmanLookingRight = True

    def restartPacmanLook(self):
        self.isPacmanLookingRight = False
        self.isPacmanLookingUp = False
        self.isPacmanLookingDown = False
        self.isPacmanLookingLeft = False

    def movePacmanUp(self):
        _np = self.__pacmanPos[0] - 1
        if _np < 0:
            print("Invalid position")
            return
        else:
            self.__pacmanPos = (_np, self.__pacmanPos[1])
            self.restartPacmanLook()
            self.__isPacmanLookingUp = True
            self.tick()

    def movePacmanRight(self):
        _np = self.__pacmanPos[1] + 1
        if _np >= self.__columns:
            print("Invalid position")
            return
        else:
            self.__pacmanPos = (self.__pacmanPos[0], _np)
            self.restartPacmanLook()
            self.__isPacmanLookingRight = True
            self.tick()

    def movePacmanDown(self):
        _np = self.__pacmanPos[0] + 1
        if _np >= self.__columns:
            print("Invalid position")
            return
        else:
            self.__pacmanPos = (_np ,self.__pacmanPos[1])
            self.restartPacmanLook()
            self.__isPacmanLookingDown = True
            self.tick()

    def movePacmanLeft(self):
        _np = self.__pacmanPos[1] - 1
        if _np < 0:
            print("Invalid position")
            return
        else:
            self.__pacmanPos = (self.__pacmanPos[0], _np)
            self.restartPacmanLook()
            self.__isPacmanLookingLeft = True
            self.tick()

    def restartPacmanPos(self):
        self.__pacmanPos = (0,0)
        self.restartPacmanLook()
        self.__isPacmanLookingRight = True
        self.tick()

    def whereIsPacman(self):
        print(f"Pacman is at row {self.__pacmanPos[0] + 1} and column {self.__pacmanPos[1] + 1}")

    #new frame on tick()
    def tick(self):
        #os.system("clear")

        if self.__isPacmanOnLevel:
            for rows in range(self.__rows):
                for columns in range(self.__columns):
                    if (rows, columns) == self.__pacmanPos:
                        if self.__isPacmanLookingUp:
                            print(" ^ ", end="")
                        elif self.__isPacmanLookingRight:
                            print(" > ", end="")
                        elif self.__isPacmanLookingDown:
                            print(" V ", end="")
                        elif self.__isPacmanLookingLeft:
                            print(" < ", end="")
                    else:
                        print(" * ", end="")
                print("\n")
        else:
            for rows in range(self.__rows):
                for columns in range(self.__columns):
                    print(" * ", end="")
                print("\n")


def game():
    _maze = Maze(5, 5)
    _maze.setPacmanAt(2, 2)
    _maze.tick()

game()
