from collections import deque

class Solution:
    def getColor(self, point):
        return self.image[point[0]][point[1]]
    
    def setColor(self, point, color):
        self.image[point[0]][point[1]] = color
    
    def getNeighbors(self, point):
        neighbors = []
        
        if point[0] > 0:
            neighbors.append((point[0]-1, point[1]))
        if point[0] < self.maxHeight - 1:
            neighbors.append((point[0]+1, point[1]))
        if point[1] > 0:
            neighbors.append((point[0], point[1]-1))
        if point[1] < self.maxWidth - 1:
            neighbors.append((point[0], point[1]+1))

        return neighbors
    
    def hasVisited(self, point):
        print("X: %i Y: %i" %(point[0], point[1]))
        return self.visited[point[0]][point[1]]
    
    def setVisited(self, point, status):
        self.visited[point[0]][point[1]] = status
    
    def isStartColor(self, point):
        return self.getColor(point) == self.startColor
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.maxWidth = len(image[0])
        self.maxHeight = len(image)
        self.image = image
        
        startPoint = (sr,sc)
        self.startColor = self.getColor(startPoint)
        self.setColor(startPoint, newColor)
        
        self.visited = [[False] * self.maxWidth for i in range(0,self.maxHeight)]
        
        toEvaluate = deque([])
        toEvaluate.append(startPoint)
        while len(toEvaluate) > 0:
            currPoint = toEvaluate.pop()
            for neighbor in self.getNeighbors(currPoint):
                if not self.hasVisited(neighbor) and self.isStartColor(neighbor):
                    self.setVisited(neighbor, True)
                    self.setColor(neighbor, newColor)
                    toEvaluate.append(neighbor)
                    
        return self.image
