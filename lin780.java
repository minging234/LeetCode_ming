import java.util.ArrayList;

// Remove Invalid Parentheses

public class Solution {
    /**
     * @param s: The input string
     * @return: Return all possible results
     */
    public List<String> removeInvalidParentheses(String s) {
        List<String> ans = new ArrayList<>();

        int left = 0, right = 0;
        for (char c:s.toCharArray()) {
            if (c == '(') {
                left ++;
            } else if (c == ')') {
                if (left > 0) {
                    left --;
                } else {
                    right ++;
                }
            }
        }

        dfs(ans, left, right, 0, s);
        return ans;
    }

    private void dfs(List<String> ans, int left, int right, int start, String s) {
        if (left == 0 && right == 0&& isValid(s)) {
            ans.add(s);
        }
        for (int i=start; i < s.length(); i++) {
            if (i != start && s.charAt(i) == s.charAt(i-1)) {
                continue;
            }
            if (left > 0 && s.charAt(i) == '(') {
                dfs(ans, left - 1, right, i, s.substring(0, i) + s.substring(i+1));
            }
            if (right > 0 && s.charAt(i) == ')') {
                dfs(ans, left, right - 1, i, s.substring(0, i) + s.substring(i+1));
            }
        }
        return;
    }

    private boolean isValid(String s) {
        int left = 0;
        for (char c:s.toCharArray()) {
            if (c == '(') {
                left ++;
            } else if (c == ')') {
                if (left > 0) {
                    left --;
                } else {
                    return false;
                }
            }
        }
        return left == 0;
    }
}