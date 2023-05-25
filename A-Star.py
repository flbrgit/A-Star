'''
Implementation of the A*- Algorithm.
'''
from math import sqrt
from typing import Callable, Tuple

class NODE:
    def __init__(self, position, g, h, old):
        self.position = position
        self.g = g
        self.h = h
        self.f = self.g+self.h
        self.old = old

    def set_h(self, h):
        self.h = h

    def set_g(self, g):
        self.g = g

    def set_f(self):
        self.f = self.g + self.h

class ASTAR:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int], dim: Tuple[int, int], around: Callable = None):
        """
        @param start: Start coordinates
        @param end: End coordinates
        @param dim: Dimensions of the grid
        @param around: Optional callable used for surrounding tiles. When called, 
        this ASTAR object is passed as first argument. If no function is provided, 
        use the built-in around method 
        computing also diagonal fields in the grid
        """
        self.openlist = list()
        self.closedlist = list()
        self.start = start
        self.end = end
        self.dim = dim
        self.g = 0
        self.call = around
        self.create_node(start, None)
        # Set forbidden coordinates here
        self.forbidden = []

    def get_around(self, pos: tuple, dim: tuple, forbidden: list, closedlist: list):
        positions = [(x, y) for x in range(1, dim[0]+2) for y in range(1, dim[1]+2) \
            if x-pos[0] in [0,1,-1] and y-pos[1] in [0,1,-1] and (x,y) not in forbidden \
                and (x,y) not in closedlist and (x,y) != pos]        
        return positions

    def get_best_node(self):
        '''
        Gets the best node to walk.
        '''
        if len(self.openlist) == 1:
            return self.openlist[0]
        flist = [i.f for i in self.openlist]
        pos = flist.index(min(flist))
        return self.openlist[pos]

    @staticmethod
    def h(start, end):
        '''
        Gets the distance between two positions.
        '''
        dis = sqrt((abs(start[0]-end[0])**2)+(abs(start[1]-end[1])**2))
        return dis


    def create_node(self, position, old, cost=1):
        '''
        Creates a node.
        '''
        dis = ASTAR.h(position, self.end)
        node = NODE(position, cost, dis, old)
        self.openlist.append(node)

    def move(self, node):
        '''
        Moves a node from openlist to closedlist.
        '''
        self.closedlist.append(node.position)
        del self.openlist[self.openlist.index(node)]

    def update(self):
        '''
        Updates the openlist to new values.
        '''
        self.openlist = list(set(self.openlist))
        self.openlist = [element for element in self.openlist if element.position not in self.closedlist]

    def run(self, *args, **kwargs):
        '''
        Runs the algorithm.
        '''
        self.history = list()
        while self.end not in self.closedlist:
            #Get the best following node
            node = self.get_best_node()
            print("Moving to node {}".format(node.position))
            self.move(node)
            self.update()
            neighbors = self.get_around(node.position, self.dim, self.forbidden, self.closedlist) if self.call == None else self.call(self, *args, **kwargs)
            for position in neighbors:
                self.create_node(position, node)
            self.g += node.g
            if len(self.openlist) == 0:
                print("No way found.")
                break
            self.history.append(node.position)
        print("Reversing path...")
        self.history.reverse()
        way = list()
        while node.old != None:
            way.append(node.position)
            node = node.old
        print(way)

                       
if __name__ == "__main__":
    star = ASTAR((7,10), (2,2), (10,10))
    star.run()