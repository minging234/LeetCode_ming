import java.util.ArrayList;
import java.util.Set;

// Word Break II


public class Solution {
    /*
     * @param s: A string
     * @param wordDict: A set of words.
     * @return: All possible sentences.
     */
    // public List<String> wordBreak(String s, Set<String> wordDict) {
    //     List<String> ans = new ArrayList<>();
    //     dfsHelper(ans, 0, 0, s, "", wordDict);
    //     return ans;
    // }

    // private void dfsHelper(List<String> ans, int start, int ind, String s, String possible, Set<String> wordDict) {
    //     if (ind == s.length()) {
    //         if (start == s.length() - 1) {
    //             ans.add(possible);
    //         }
    //         return;
    //     }

    //     if (wordDict.contains(s.substring(start, ind + 1))) {
    //         String next = possible + " " + s.substring(start, ind + 1);
    //         int nextStart = ind;
    //         dfsHelper(ans, nextStart, ind+1, s, next, wordDict);
    //     }

    //     dfsHelper(ans, start, ind + 1, s, possible, wordDict);
    // }

    public ArrayList<String> wordBreak(String s, Set<String> dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        Map<String, ArrayList<String>> memo = new HashMap<String, ArrayList<String>>();
        return wordBreakHelper(s, dict, memo);
    }

    public ArrayList<String> wordBreakHelper(String s,
                                                Set<String> dict,
                                                Map<String, ArrayList<String>> memo){
        if (memo.containsKey(s)) {
            return memo.get(s);
        }
        
        ArrayList<String> results = new ArrayList<String>();
        
        if (s.length() == 0) {
            return results;
        }
        
        if (dict.contains(s)) {
            results.add(s);
        }
        
        for (int len = 1; len < s.length(); ++len){
            String word = s.substring(0, len);
            if (!dict.contains(word)) {
                continue;
            }
            
            String suffix = s.substring(len);
            ArrayList<String> segmentations = wordBreakHelper(suffix, dict, memo);
            
            for (String segmentation: segmentations){
                results.add(word + " " + segmentation);
            }
        }
        
        memo.put(s, results);
        return results;
    }
}