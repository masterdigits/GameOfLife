from game_of_life_library import MapAbstract, CellAbstract
from random import random
from copy import deepcopy

class Map(MapAbstract):
    
    def __init__(self, X, Y, alive_probability):
        super().__init__(X, Y, alive_probability)

    def __generateMap(self, prob):
        return [
            [Cell(random() < prob) for _ in range(self.sizeY)]
            for _ in range(self.sizeX)]

    def __nextGeneration(self):
        new_map = deepcopy(self.Map)
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                x_addons = {-1,0,1}
                y_addons = {-1,0,1}

                if x == 0:
                    x_addons.remove(-1)
                if x == self.sizeX - 1:
                    x.addons.remove(1)
                if y == 0:
                    y_addons.remove(-1)
                if y == self.sizeY - 1:
                    y.addons.remove(1)

                cell_map = [self.Map[x + x_addon][y + y_addon] 
                            for x_addon in x_addons 
                            for y_addon in y_addons]
                
                new_status = self.Map[x][y].checkMe(cell_map)
                new_map[x][y].setStatus(new_status)

        return new_map

class Cell(CellAbstract):

    def __init__(self, alive):
        super().__init__(alive)

    def checkMe(self, my_map):
        neighbours = sum([1 for cell in my_map if cell.getStatus()])
        if self.getStatus() and neighbours - 1 in {2,3}:
            return True
        if neighbours in {2,3}:
            return True
        return False          