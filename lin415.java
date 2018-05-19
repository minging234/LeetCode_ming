public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        s = s.toLowerCase();
        int start = 0, end = s.length()-1;

        while(start < end) {
            if (!Character.isLetterOrDigit(s.charAt(start))) {
                start ++;
                continue;
            }

            if (!Character.isLetterOrDigit(s.charAt(end))) {
                end --;
                continue;
            }

            if (s.charAt(start) != s.charAt(end)) return false;
            start ++;
            end --;
        }
        return true;
        
    }
}