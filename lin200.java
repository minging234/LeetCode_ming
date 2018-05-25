//Given a string S, find the longest palindromic substring in S

public class Solution {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */

    // private int getPalindromeNum(String s, int front, int back) {
    //     int cur = 0;
    //     while(front >= 0 && back < s.length()) {
    //         if (s.charAt(front) != s.charAt(back)) break;
    //         front --;
    //         back ++;
    //         cur ++;
    //     }
    //     return cur;
    // }

    // public String longestPalindrome(String s) {
    //     if (s == null || s.length() == 0) {
    //         return "";
    //     }

    //     String ans = s.substring(0,1);
    //     for (int i = 1; i < s.length(); i++) {
    //         int cur = getPalindromeNum(s, i-1, i+1);
    //         if (2*cur + 1 > ans.length()) ans = s.substring(i - cur, i + cur +1);

    //         if (s.charAt(i) == s.charAt(i-1)) {
    //             cur = getPalindromeNum(s, i-2, i+1);
    //             if (2*cur + 2 > ans.length()) ans = s.substring(i-1-cur, i+cur+1);
    //         }
            
    //     }

    //     return ans;
    // } 


    // the dp method to solve this problem
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }
        
        int n = s.length(); 
        int start = 0, len = 1; 
        boolean[][] isp = new boolean[n][n];

        isp[0][0] = true;
        for (int i = 1; i < n; i++) {
            isp[i][i] = true;
            if (s.charAt(i) == s.charAt(i-1)) {
                isp[i-1][i] = true;
                start = i-1;
                len = 2;
            }
        }

        for (int i = n-1; i >= 0; i--) {
            for (int j = i + 2; j < n; j++) {
                isp[i][j] = s.charAt(i) == s.charAt(j) && isp[i+1][j-1];
                if (isp[i][j] && j-i+1 > len) {
                    start = i;
                    len = j-i+1;
                }
            }
        }
        return s.substring(start, start + len);
    } 
    
}


