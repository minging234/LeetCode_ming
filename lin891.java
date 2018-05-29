// Valid Palindrome II

public class Solution {
    /**
     * @param s: a string
     * @return: nothing
     */
    public boolean validPalindrome(String s) {
        if (s == "" || s == null) {
            return true;
        }
        int start = 0, end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                String s1 = s.substring(start,end);
                String s2 = s.substring(start+1, end);
                if (helper(s1) || helper(s2)) {
                    return true;
                } else {
                    return false;
                }
            }
            start ++;
            end ++;
        }
        return true;
    }
    private boolean helper(String s) {
        for(int i = 0, j = s.length()-1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}