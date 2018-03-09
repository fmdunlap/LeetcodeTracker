import unicodedata
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        goodMatrix = []
        #First normalize this bastardized unicode
        for row in matrix:
            newRow = []
            for col in row:
                newRow.append(int(col.encode('ascii', 'ignore')))
            goodMatrix.append(newRow)
        
        maxSide = 0
        
        for row in range(0,len(goodMatrix)):
            for col in range(0, len(goodMatrix[row])):
                if goodMatrix[row][col] == 1:
                    side = 0
                    while col + side < len(goodMatrix[row]):
                        nextVal = goodMatrix[row][col+side]
                        if nextVal == 1:
                            side += 1
                        else:
                            break
                    # print("Side: %i" %side)
                    if side > maxSide:
                        correctBounds = 0
                        for i in range(0,side):
                            if(row + i < len(goodMatrix)):
                                if(goodMatrix[row+i][col] != 1):
                                    break
                                correctBounds += 1
                        # print("Correct Bounds %i" %correctBounds)
                        currSizeToCheck = 0
                        broken = False
                        while not broken and currSizeToCheck < correctBounds:
                            for i in range(0,currSizeToCheck):
                                rowVal = goodMatrix[row+i][col+currSizeToCheck]
                                colVal = goodMatrix[row+currSizeToCheck][col+i]
                                diagVal = goodMatrix[row+currSizeToCheck][col+currSizeToCheck]
                                if rowVal != 1 or colVal != 1 or diagVal != 1:
                                    broken = True
                                    break
                            if not broken:
                                currSizeToCheck += 1
                        maxSide = max(maxSide, currSizeToCheck)
            # print("MaxSide: %i" %maxSide)
        
        return maxSide**2
                        
