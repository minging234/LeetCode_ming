class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        int[] map = new int[128];
        for(int i = 0, j = 0; i < s.length(); i++) {
            j = Math.max(j,map[s.charAt(i)]);
            ans = Math.max(ans, i-j+1);
            map[s.charAt(i)] = i + 1;
        }
        return ans;
    }
}