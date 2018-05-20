//Given a string S, find the longest palindromic substring in S

public class Solution {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */

    private int getPalindromeNum(String s, int front, int back) {
        int cur = 0;
        while(front >= 0 && back < s.length()) {
            if (s.charAt(front) != s.charAt(back)) break;
            front --;
            back ++;
            cur ++;
        }
        return cur;
    }

    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }

        String ans = s.substring(0,1);
        for (int i = 1; i < s.length(); i++) {
            int cur = getPalindromeNum(s, i-1, i+1);
            if (2*cur + 1 > ans.length()) ans = s.substring(i - cur, i + cur +1);

            if (s.charAt(i) == s.charAt(i-1)) {
                cur = getPalindromeNum(s, i-2, i+1);
                if (2*cur + 2 > ans.length()) ans = s.substring(i-1-cur, i+cur+1);
            }
            
        }

        return ans;
    } 
}