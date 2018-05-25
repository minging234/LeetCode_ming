public class Solution {
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    // public int longestPalindrome(String s) {
    //     if (s == null || s.length() == 0) return 0;
    //     Map<Character, Integer> dict = new HashMap<>();
    //     for (int i=0; i < s.length(); i++) {
    //         if (dict.containsKey(s.charAt(i))) dict.put(s.charAt(i), dict.get(s.charAt(i)) + 1);
    //         else dict.put(s.charAt(i), 1);
    //     }

    //     int ans = 0;
    //     boolean flag = false;

    //     for (int num: dict.values()) {
    //         if(num % 2 != 0) flag = true;
    //         ans += (num/2) * 2;
    //     }
    //     if (flag) ans += 1;
    //     return ans;
        
    // }

    // using arrary to implement
    public int longestPalindrome(String s) {
        if (s == null || s.length() == 0)  return 0;
        int[] dict =  new int[255];
        int ans = 0;
        boolean flag = false;
        for (int i = 0; i < s.length(); i++) {
            dict[s.charAt(i)] += 1;
        }
        for (int i: dict) {
            if (i % 2 != 0) flag = true;
            ans += (i/2) * 2;
        }
        if (flag) return ans + 1;
        return ans;
    }

}