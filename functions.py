import math
from collections import defaultdict
class Cells():
    def __init__(self, aliveCells = set()):
        """
        (Cells, set()) -> None \n
        Initialize alive cells to {aliveCells}. Default aliveCells = set()
        """
        self.aliveCells = aliveCells
    
    def neighbours(self, cell):
        """
        (Cells, (int, int)) -> int \n
        Returns the amount of alive neighbours cell has
        """
        total = -1
        for other in self.aliveCells:
            if math.sqrt((cell[0]-other[0])**2+(cell[1]-other[1])**2) < 2:
                total += 1
        return total

    def evolve(self, grid):
        """
        (Cells, Grid) -> None \n
        Evolves the cells to next generation based on rules: \n
        1. Any live cell with fewer than two live neighbours dies \n
        2. Any live cell with two or three live neighbours lives on to the next generation. \n
        3. Any live cell with more than three live neighbours dies \n
        4. Any dead cell with exactly three live neighbours becomes a live cell
        """
        dead = set()
        deadNeighbours = defaultdict(int)
        for r in range(len(grid.grid)):
            for c in range(len(grid.grid[r])):
                adj = self.neighbours((r,c))
                if adj < 2 or adj > 3:
                    dead.add((r,c))
                if (r,c) not in self.aliveCells:
                    if (r-1,c-1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r-1,c) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r-1,c+1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r,c-1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r,c+1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r+1,c-1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r+1,c) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
                    if (r+1,c+1) in self.aliveCells:
                        deadNeighbours[(r,c)] += 1
        alive = self.aliveCells - dead
        for deadCell in deadNeighbours:
            if deadNeighbours[deadCell] == 3:
                alive.add(deadCell)
        self.aliveCells = alive

    def __repr__(self):
        """
        (Cells) -> str \n
        Returns a canonical string representation of Cells(aliveCells)
        """
        return f"Cells({self.aliveCells})"

    def __str__(self):
        """
        (Cells) -> str \n
        Returns the coordinates of alive cells in Cells
        """
        return f"The coordinates of alive cells are {self.aliveCells}"

class Grid():
    def __init__(self, dead, alive, bounds):
        """
        (Grid, str, str, tuple()) -> None \n
        Initialize dead and alive cell representations to dead and alive. \n
        Initialize (rows, columns) of grid to bounds.
        """
        self.dead = dead
        self.alive = alive
        self.bounds = bounds
        self.grid = [[self.dead for c in range(self.bounds[1])] for r in range(self.bounds[0])]

    def update(self, cells):
        """
        (Grid, Cells) -> None \n
        Update the grid with the alive and dead cells in cells
        """
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r,c) in cells.aliveCells:
                    self.grid[r][c] = self.alive
                else:
                    self.grid[r][c] = self.dead

    def __repr__(self):
        """
        (Grid) -> str
        Returns a canonical representation of Grid(dead, alive, bounds)
        """
        return f"Grid({self.dead}, {self.alive}, {self.bounds})"

    def __str__(self):
        """
        (Grid) -> str \n
        Returns a string representation of the grid
        """
        output = ""
        for r in self.grid:
            for c in r:
                output += c + " "
            output += "\n"
        return output
