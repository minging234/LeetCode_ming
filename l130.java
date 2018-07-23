import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    private int[] offsetx = {0, 0, 1, -1};
    private int[] offsety = {1, -1, 0, 0};


    public void solve(char[][] board) {
        if (board == null || board.length == 0 || board[0] == null || board[0].length == 0) {
            return;
        }
        int n = board.length;
        int m = board[0].length;
        boolean[][] map = new boolean[n][m];

        for (int i=0; i < n; i++) {
            if (board[i][0] == 'o') {
                dfs(board, map, i, 0, n, m);
            }
            if (board[i][m-1] == 'o') {
                dfs(board, map, i, m-1, n, m);
            }
        }

        for (int i=0; i < m; i++) {
            if (board[0][i] == 'o') {
                dfs(board, map, 0, i, n, m);
            }
            if (board[n-1][i] == 'o') {
                dfs(board, map, n-1, i, n, m);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'o' && map[i][j] == false) {
                    board[i][j] = 'x';
                }
            }
        }

        return;
    }
    
    private void dfs(char[][] board, boolean[][] map, int x, int y, int n, int m) {
        if (x < 0 || x == n || y < 0 || y == m || map[x][y] == true || board[x][y] == 'x') {
            return;
        }
        map[x][y] = true;
        for (int i=0; i < 4; i++) {
            dfs(board, map, x + offsetx[i], y + offsety[i], n, m);
        }
    }
}