//Low key proud of this one. I'm finally really starting to get the whole recurrsion thing intuitively. Which like. Hell yeah.

class Solution {
    char[][] grid;
    int rowMax;
    int colMax;
    
    public void floodFill(int row, int col){
        if(grid[row][col] == '0'){
            return;
        } else {
            grid[row][col] = '0';
            if(row > 0){
                floodFill(row - 1, col);
            }
            if(row < rowMax - 1){
                floodFill(row + 1, col);
            }
            if(col > 0){
                floodFill(row, col - 1);
            }
            if(col < colMax - 1){
                floodFill(row, col + 1);
            }
        }
    }
    
    public int isIsland(int row, int col){
        //If it's a 0, there's no island here. So return 0.
        if(grid[row][col] == '0'){
            return 0;
        }
        //Otherwise there is an island here and we need to recursively
        //flood fill 0s to prevent future double-counts.
        floodFill(row, col);
        return 1;
        
    }
    
    public int numIslands(char[][] _grid) {
        int count = 0;
        grid = _grid;
        rowMax = grid.length;
        
        if(rowMax > 0){
            colMax = grid[0].length;
        } else {
            colMax = 0;
        }
        
        
        for(int i = 0; i < rowMax; i++){
            for(int j = 0; j < colMax; j++){
                count += isIsland(i, j);
            }
        }
        
        return count;
    }
}
