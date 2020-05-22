class QueensProblem():
    def __init__(self, num_of_queens):
        self.num_of_queens = num_of_queens 
        self.chessTable = [[None for i in range(num_of_queens)] for j in range(num_of_queens)]

    def solveQueensProblem(self):
        if self.solve(0):
            self.printQueens()
        else:
            print("No solution possible")

    def solve(self, colIndex):
        if colIndex == self.num_of_queens:
            return True 

        for rowIndex in range(self.num_of_queens):
            if self.isPlaceValid(rowIndex, colIndex):
                self.chessTable[rowIndex][colIndex] = 1

                if self.solve(colIndex + 1):
                    return True
                
                # Backtracking ...
                self.chessTable[rowIndex][colIndex] = 0 

        return False 

    def isPlaceValid(self, rowIndex, colIndex):
        # same row check
        for i in range(colIndex):
            if self.chessTable[rowIndex][i] == 1:
					return False 

        # top left to bottom right check ...
        j = colIndex 
        for i in range(rowIndex, -1 , -1):
            if j < 0 :
                break 
            if self.chessTable[i][j] == 1:
                return False 

            j -= 1

        # top right to bottom left ...
        j = colIndex
        for i in range(rowIndex, len(self.chessTable)):
            if j < 0 :
                break
            if self.chessTable[i][j] == 1: 
                return False 

            j -= 1

        return True 

    def printQueens(self):
        for i in range(self.num_of_queens):
            for j in range(self.num_of_queens):
                if self.chessTable[i][j] == 1:
                    print(" *  ", end ="  ")
                else: 
                    print(" -  ", end = "  ")

            print(" \n ")


queensProblem = QueensProblem(4)
queensProblem.solveQueensProblem()
