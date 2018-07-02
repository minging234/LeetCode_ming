// Find the Missing Number II

public class Solution {
    /**
     * @param n: An integer
     * @param str: a string with number from 1-n in random order and miss one number
     * @return: An integer
     */
    public int findMissing2(int n, String str) {
        boolean[] tag = new boolean[n+1];
        helper(tag, 0, str, n+1);
        return this.ans;
    }

    private int ans = 0;

    private void helper(boolean[] tag, int ind, String str, int n) {
        if (this.ans != 0) return;
        if (ind == str.length()) {
            int count = 0;
            int cand = 0;
            for (int i=1; i < n; i++) {
                if (tag[i] == false) {
                    cand = i;
                    count ++;
                }
            }
            if (count == 1) {
                this.ans = cand;
            }
            return;
        }

        if (str.charAt(ind) == '0') {
            return;
        }
        int cur;
        
        if (ind < str.length() - 1) {
            cur = Integer.parseInt(str.substring(ind,ind+2));
            if (cur < n && tag[cur] == false) {
                tag[cur] = true;
                helper(tag, ind + 2, str, n);
                tag[cur] = false;
            }
        }
        
        cur = Integer.parseInt(str.substring(ind,ind+1));
        
        if (cur < n && tag[cur] == false) {
            tag[cur] = true;
            helper(tag, ind + 1, str, n);
            tag[cur] = false;
        }

        return;
    }
}