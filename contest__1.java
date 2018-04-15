class Solution {
    public int rotatedDigits(int N) {
        int count = 0;
        boolean flag = false; 

        for (int i = 1; i <= N; i++) {
            flag = false;
            while (i > 0) {
                int b = i%10;
                if (b == 2 || b == 5 || b == 6 || b == 9){
                    flag = true;
                }
                if (b == 3 || b == 4 || b == 7) {
                    flag = false;
                    break;
                }
                i = i/10;
            }
            if (flag) count++;
        }
        return count;

    }
}


class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        boolean[][] visted = new boolean[target[0]+1][target[1]+1];
        dfs(0,0,target,visted,0,ghosts);
        if (visted[target[0]][target[1]] == true) return true;
        else return false;

    }

    private void dfs(int x, int y, int[] target, boolean[][] visted,int step, int[][] ghosts){
        if (x < 0 || x > target[0]) return;
        if (y < 0 || y > target[1]) return;
        if (visted[x][y] == true || visted[target[0]][target[1]] == true) return;
        visted[x][y] = true;
        for (int i = 0; i < ghosts.length; i ++) {
            if (manhadist(x,y,ghosts[i]) <= step){
                if (x == target[0] && y == target[1]) visted[x][y] =false;
                return;
            }
        }
        dfs(x+1, y, target, visted, step + 1,ghosts);
        dfs(x, y+1, target, visted, step + 1,ghosts);
    }

    private int manhadist(int x, int y, int[] end) {
        return Math.abs(x - end[0]) + Math.abs(y - end[1]);
    }
}



class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        int[] start = new int[2]{0,0};
        int pdist = manhadist(start, target);

        for (int i =0; i < ghosts.length; i++) {
            if (manhadist(ghosts[i], target) < pdist) return false;
        }
        return true;
    }
    private int manhadist(int[] start, int[] end) {
        return Math.abs(start[0] - end[0]) + Math.abs(start[1] - end[1]);
    }
}


class Solution {
    public String customSortString(String S, String T) {
        linkedHashMap<Character,Integer> map = new linkedHashMap<Character, Integer>();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            map.put(c,0);
        }
        String ans = "";
        for (int i = 0; i < T.length(); i++) {
            char c = T.charAt(i);
            if (map.contains(c)) {
                map.put(c, map.get(c)+1);
            }
            else {
                ans = ans + c;
            }
        }
        for (Integer key : map.keySet()){
            int val = map.get(key);
            while(val-- > 0) {
                ans += key;
            }            
        }
        return ans;
    }
}