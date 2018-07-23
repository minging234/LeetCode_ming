import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[][] transpose(int[][] A) {
        if (A == null || A.length == 0 || A[0] == null || A[0].length == 0) {
            return A;
        }
        int[][] B = new int[A[0].length][A.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                B[j][i] = A[i][j];
            }
        }
        return B;
    }

    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        if (root == null) {
            return root;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        HashMap<TreeNode, TreeNode> map =  new HashMap<>();

        queue.add(root);
        map.put(root, null);
        LinkedList<TreeNode> level = new LinkedList<>();
        

        while(!queue.isEmpty()) {
            int size = queue.size();
            level = new LinkedList<>();
            for (int i=0; i < size; i++) {
                TreeNode cur = queue.poll();
                level.offer(cur);
                if (cur.left != null) {
                    queue.add(cur.left);
                    map.put(cur.left, cur);
                }
                if (cur.right != null) {
                    queue.add(cur.right);
                    map.put(cur.right, cur);
                }
            }
        }

        while (level.size() != 1) {
            LinkedList<TreeNode> temp = new LinkedList<>();
            for (TreeNode node: level) {
                if (temp.isEmpty()) {
                    temp.offer(map.get(node));
                    continue;
                }
                if (map.get(node) != temp.peek()) {
                    temp.add(map.get(node));
                }
            }
            level = temp;
        }

        return level.get(0);
    }

    // public int primePalindrome(int N) {
    //     int scal = 0;
    //     int num = N;
    //     while (num > 0) {
    //         num = num/10;
    //         scal ++;
    //     } 
    //     int seed = N;
    //     for (int i=0; i < scal/2; i++) {
    //         seed = seed/10;
    //     }
    //     int[] nums = new int[scal/2];
    //     int cand = seed;


    //     do {
    //         cand = seed;  
    //         int cseed = seed;
    //         if (scal % 2 != 0) {
    //             cseed /= 10;
    //         }
    //         for (int i=0; i < nums.length; i++) {
    //             nums[i] = cseed % 10;
    //             cseed /= 10;
    //         }

    //         for (int i=0; i < scal /2 ; i++) {
    //             cand *= 10;
    //             cand += nums[i];
    //         } 
    //         if (cand >= N && isPalindrome(cand)) {
    //             return cand;
    //         }
    //         seed ++;

    //     } while (cand < Math.pow(10, scal));

    //     int m = 1;
    //     for (int i=0; i < scal; i++) {
    //         m *= 10;
    //     }
    //     return primePalindrome(m);
        
    // }

    public int primePalindrome(int N) { 
        String s = String.valueOf(N);

        String front = s.substring(0, (s.length() + 1)/2);
        int f = Integer.parseInt(front);

        while (front.length() <= (s.length() + 1)/2) {
            StringBuilder end = new StringBuilder(front);
            if (s.length()%2 != 0) {
                end.deleteCharAt(end.length() - 1);
            }        
            end.reverse();
            String all = front + end.toString();

            int m = Integer.parseInt(all);
            if (m > N && isPalindrome(m)) {
                return m;
            }
            f ++;
            front = String.valueOf(f);
        }
        int m = 1;
        for (int i=0; i < s.length(); i++) {
            m *= 10;
        }
        return primePalindrome(m);
    }

    private boolean isPalindrome(int m) {
        if (m == 1) return false;
        for (int i = 2; i < m; i++) {
            if (m%i == 0) {
                return false;
            }
        }
        return true;
    }
}