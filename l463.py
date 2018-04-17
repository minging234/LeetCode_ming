""" Island Perimeter """

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vert = len(grid)
        long = len(grid[0])
        prim = 0
        for i in range(vert):
            for j in range(long):
                contr = 0
                if grid[i][j] == 1:
                    contr = 4
                    if i == 0:
                        pass
                    elif grid[i-1][j] == 1:
                        contr -= 1
                    if i == vert-1:
                        pass
                    elif grid[i+1][j] == 1:
                        contr -= 1
                    if j == 0:
                        pass
                    elif grid[i][j-1] == 1:
                        contr -= 1
                    if j == long - 1:
                        pass
                    elif grid[i][j+1] == 1:
                        contr -= 1
                prim += contr
        return prim

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

vert = len(grid)
long = len(grid[0])
prim = 0
for i in range(vert):
    for j in range(long):
        contr = 0
        if grid[i][j] == 1:
            contr = 4
            if i == 0:
                pass
            elif grid[i-1][j] == 1:
                contr -= 1
            if i == vert-1:
                pass
            elif grid[i+1][j] == 1:
                contr -= 1
            if j == 0:
                pass
            elif grid[i][j-1] == 1:
                contr -= 1
            if j == long - 1:
                pass
            elif grid[i][j+1] == 1:
                contr -= 1
        prim += contr
        print(prim,i, j, contr)





