class Solution {
public:
    
    int cols;
    int rows;
    
    struct point{
        int row;
        int col;
    };
    
    vector<point> getNeighbors(point p){
        vector<point> neighbors;
        if(p.row > 0){
            point leftNeighbor;
            leftNeighbor.row = p.row - 1;
            leftNeighbor.col = p.col;
            neighbors.push_back(leftNeighbor);
        }
        if(p.row < rows){
            point rightNeighbor;
            rightNeighbor.row = p.row + 1;
            rightNeighbor.col = p.col;
            neighbors.push_back(rightNeighbor);            
        }
        if(p.col > 0){
            point bottomNeighbor;
            bottomNeighbor.row = p.row;
            bottomNeighbor.col = p.col + 1;
            neighbors.push_back(bottomNeighbor);            
        }
        if(p.col < cols){
            point topNeighbor;
            topNeighbor.row = p.row;
            topNeighbor.col = p.col - 1;
            neighbors.push_back(topNeighbor);            
        }
        return neighbors;
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        cols = image[0].size();
        rows = image.size();
        int startingColor = image[sr][sc];
        
        vector<vector<bool>> visitedPixel(cols, vector<bool>(rows,false));
        
        
        std::queue<point> pointsToEvaluate;
        point startingPoint;
        startingPoint.row = sr;
        startingPoint.col = sc;
        pointsToEvaluate.push(startingPoint);
        
        while(pointsToEvaluate.size() != 0){
            point currPoint = pointsToEvaluate.front();
            pointsToEvaluate.pop();
            for(point neighbor: getNeighbors(currPoint)){
                int nRow = neighbor.row;
                int nCol = neighbor.col;
                if(image[nRow][nCol] == startingColor && !visitedPixel[nRow][nCol]){
                    pointsToEvaluate.push(neighbor);
                    visitedPixel[nRow][nCol] = true;
                    image[nRow][nCol] = newColor;
                }
            }
        }
        
        cols = 0;
        rows = 0;
        
        return vector<vector<int>>(image);
    }
};
