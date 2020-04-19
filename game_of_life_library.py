from abc import ABC, abstractmethod

class MapAbstract(ABC):

    self.Map = None
    self.sizeX = 0
    self.sizeY = 0

    def __init__(self, X, Y, alive_probability):

        self.sizeX = X
        self.sizeY = Y

        self.__generateMap(alive_probability)

    def mapGenerating(self, prob):
        if prob < 0:
            raise ValueError('Alive probability cannot be smaller than 0.')
        if prob == 0:
            print('Warning! Alive probability is 0. None of cells cannot be alive.')
        self.Map = self.__generateMap(prob)

    def next(self):
        if self.Map == None:
            raise TypeError('Map is not assigned yet.')

        self.Map = self.__nextGeneration()

    def __str__(self):
        return self.__printMap()

    @abstractmethod
    def __generateMap(self, prob):
        '''
        Generuje nową mapę powołując do życia komórki podanym prawdopodobieństwem.
        '''
        pass

    @abstractmethod
    def __nextGeneration(self):
        '''
        Oblicza nową generację komórek.
        '''
        pass

    @abstractmethod
    def __printMap(self):
        '''
        Tworzy ciąg pozwalający wypisać mapę na ekran.
        '''
        pass

class CellAbstract(ABC):

    self.Status = None
    self.__symbol = chr('@')

    def __init__(self, alive):
        
        self.Status = alive

    @abstractmethod
    def checkMe(self, my_map):
        '''
        Oblicz liczbę sąsiadów i na tej podstawie określa czy zmienić status.
        '''
        pass

    def getStatus(self):
        return self.Status

    def setStatus(self,alive):
        self.Status = alive

    def __str__(self):
        return self.__symbol