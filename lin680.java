import java.util.ArrayList;

// Split String

public class Solution {
    /*
     * @param : a string to be split
     * @return: all possible split string array
     */
    public List<List<String>> splitString(String s) {
        List<List<String>> ans = new ArrayList<>();
        List<String> li = new ArrayList<>();
        helper(s, 0, li);
        return ans;
    }

    private void helper(String s, int ind, List<String> li, List<List<String>> ans) {

        if (ind >= s.length() - 1) {
            ans.add(li);
            return;
        }

        if (ind < s.length() - 2) {
            List<String> another = new ArrayList<>();
            another.addAll(li);
            another.add(s.substring(ind, ind + 2));
            helper(s, ind+2, another, ans);
        }
        li.add(s.substring(ind, ind+1));
        helper(s, ind+1, li, ans);

    }
}