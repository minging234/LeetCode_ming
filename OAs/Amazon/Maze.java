import java.util.LinkedList;
import java.util.Queue;

public class Maze {
    public int Solution(int[][] matrix) {
        int[] offsetx = {1, -1, 0, 0};
        int[] offsety = {0, 0, -1, 1};

        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return 0;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        Queue<int[]> queue = new LinkedList<>();
        if (matrix[0][0] == 9) {
            return 1;
        } else if (matrix[0][0] == 0) {
            return 0;
        }
        queue.offer(new int[]{0,0});

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int i=0; i < 4; i++) {
                int[] next = {curr[0] + offsetx[i], curr[1] + offsety[i]};
                if (next[0] >= 0 && next[0] < m && next[1] >= 0 && next[1] < n) {
                    if (matrix[next[0]][next[1]] == 9) {
                        return 1;
                    } else if (matrix[next[0]][next[1]] == 1) {
                        queue.offer(next);
                        matrix[next[0]][next[1]] = 0;
                    }
                }
            }
        }
        return 0;
    }
}