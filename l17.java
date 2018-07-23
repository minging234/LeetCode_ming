import java.util.ArrayList;

// Letter Combinations of a Phone Number

class Solution {
    public List<String> letterCombinations(String digits) {
        String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> ans = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return ans;
        }
        helper(map, ans, digits, 0, "");
        return ans;
    }

    private void helper(String[] map, List<String> ans, String digits, int ind, String cur) {
        if (ind == digits.length()) {
            ans.add(cur);
            return;
        }
        String possible = map[Integer.parseInt(digits.substring(ind,ind + 1))];
        for (int i=0; i < possible.length(); i++) {
            helper(map, ans, digits, ind+1, cur + possible.charAt(i));
        }
        return;
    }
}
