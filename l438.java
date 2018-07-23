import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

// Find All Anagrams in a String

class Solution {

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        int[] dict = new int[256];
        for (char c:p.toCharArray()) {
            dict[c] += 1;
        }

        int start = 0;
        int i = 0;

        while (i < s.length()) {
            dict[s.charAt(i)] -= 1;

            while (dict[s.charAt(i)] < 0) {
                dict[s.charAt(start)] += 1;
                start ++;
            }

            if (i - start + 1 == p.length()) {
                ans.add(start);
                dict[s.charAt(start)] -= 1;
                start += 1;
            }
            i += 1;
        }

        return ans;
        
    }








    // 一开始想的 O（n *p）的智障方法

    // public List<Integer> findAnagrams(String s, String p) {
    //     Set<Character> set = new HashSet<>();
    //     List<Integer> ans = new ArrayList<>();
    //     int[] pChars = new int[26];
    //     for (int i=0; i < p.length(); i++) {
    //         set.add(p.charAt(i));
    //         pChars[p.charAt(i) - 'a'] += 1;
    //     }
    //     int i = 0;
    //     while (i < s.length() - p.length() + 1) {
    //         if (set.contains(s.charAt(i))) {
    //             if (isAnagrams(s, i, i+p.length(), pChars)) {
    //                 ans.add(i);
    //                 while (i + p.length() < s.length() && s.charAt(i) == s.charAt(i + p.length())) {
    //                     i ++;
    //                     ans.add(i);
    //                 }
    //             } 
    //         }
    //         i ++;
    //     }
    //     return ans;
    // }

    // private boolean isAnagrams(String s, int ind, int end, int[] pChars) {
    //     int[] dict = new int[26];
    //     for (int i=ind; i < end; i++) {
    //         dict[s.charAt(i) - 'a'] += 1; 
    //     }
    //     for (int i=0; i < 26; i++) {
    //         if (dict[i] != pChars[i]) return false;
    //     }
    //     return true;
    // }
}
