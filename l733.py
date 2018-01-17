""" Flood Fill """

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if newColor == color:
            return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:  dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1:  dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
        dfs(sr, sc)
        return image

"""
    看别人写的有一种使用 collection.deque() 的方法，也是dfs的思想

        if not image:
            return
        cache = collections.deque()
        val = image[sr][sc]
        if val == newColor:
            return image
        cache.append((sr, sc))
        while cache:
            row, col = cache.popleft()
            image[row][col] = newColor
            if row > 0 and image[row-1][col] == val:
                cache.append((row-1, col))
            if row + 1 < len(image) and image[row+1][col] == val:
                cache.append((row+1, col))
            if col > 0 and image[row][col-1] == val:
                cache.append((row, col-1))
            if col + 1 < len(image[0]) and image[row][col+1] == val:
                cache.append((row, col+1))
        return image
"""