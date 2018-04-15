""" Word Search """

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i,j,word,board):
            if len(word) == 0:
                return True
            if i <0 or i >= len(board) or j<0 or j>= len(board[0]) or board[i][j] != word[0]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(i+1,j,word[1:],board) or dfs(i,j+1,word[1:],board) or dfs(i-1,j,word[1:],board) or dfs(i,j-1,word[1:],board)
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,word,board):
                    return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))


"""
            def dfs(x, y, word):
            if len(word)==0: return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if(dfs(i,j,word[1:])):
                        return True
        return False
"""