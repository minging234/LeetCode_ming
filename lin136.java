import java.util.LinkedList;
import java.util.List;

// Palindrome Partitioning

public class Solution {
    /*
     * @param s: A string
     * @return: A list of lists of string
     */
    public List<List<String>> partition(String s) {
        LinkedList<String> item = new LinkedList<>();
        List<List<String>> ans = new LinkedList<>();

        helper(0, s, item, ans);

        return ans;
    }



    private void helper(int ind, String s, LinkedList<String> item, List<List<String>> ans) {
        if (ind == s.length()) {
            List<String> newitem = new LinkedList<>();
            newitem.addAll(item);
            ans.add(newitem);
            return;
        }

        for (int i=1; ind + i <= s.length(); i++) {
            String cur = s.substring(ind,ind+i);
            if (isPalindrome(cur)) {
                item.offerLast(cur);
                helper(ind + i, s, item, ans);
                item.pollLast();
            }
        }
        return;
    }

    private boolean isPalindrome(String str) {
        if (str.length() <= 1) {
            return true;
        }
        int left=0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left ++;
            right --;
        }
        return true;
    }
}