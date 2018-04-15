class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        int curr = 1;
        String ans = s.substring(0,1);
        for (int i = 1; i < s.length(); i++)
        {
            if (i-curr-1>0 && s.charAt(i-curr-1) == s.charAt(i)) curr += 2;
            else if (curr == 1 && s.charAt(i) == s.charAt(i-1)) curr ++;
            else 
            {
                if (curr > ans.length())
                {
                    ans = s.substring(i - curr, i);
                }
                curr = 1;
            }
            
        }
        if (curr > ans.length())
        {
            ans = s.substring(s.length() - curr);
        }
        return ans;
    }
}