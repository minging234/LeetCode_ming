// Combination Sum

public class Solution {
    /**
     * @param candidates: A list of integers
     * @param target: An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> iterm = new ArrayList<>();
        Arrays.sort(candidates);
        helper(0, candidates, target, ans, iterm);
        return ans;
    }

    private void helper(int ind, int[] candidates, int target, List<List<Integer>> ans, List<Integer> iterm) {
        if (target == 0) {
            ans.add(new ArrayList<>(iterm));
            return;
        }
        for (int i=ind; i < candidates.length; i++) {
            if (target < candidates[ind]) {
                break;
            }
            if (i != 0 && candidates[i] == candidates[i - 1]) {
                continue;
            }
            iterm.add(candidates[i]);
            helper(i, candidates, target - candidates[i], ans, iterm);
            iterm.remove(iterm.size() -1);
            
        }
        return;
    }
}