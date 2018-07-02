

// Combinations

public class Solution {
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> iterm = new ArrayList<>();
        helper(n, k, 1, ans, iterm);
        return ans;
    }

    private void helper(int n, int k, int start, List<List<Integer>> ans, List<Integer> iterm) {
        if (iterm.size() == k) {
            ans.add(new ArrayList<>(iterm));
            return;
        }

        for (int i=start; i <= n; i++) {
            iterm.add(i);
            helper(n, k, i+1, ans, iterm);
            iterm.remove(iterm.size() - 1);
        }
        return;
    }
}