// Subsets II

public class Solution {
    /**
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums == null) {
            return ans;
        }
        Arrays.sort(nums);
        List<Integer> iterm = new ArrayList<>();
        helper(0, nums, iterm, ans);
        return ans;
    }

    private void helper(int ind, int[] nums, List<Integer> iterm, List<List<Integer>> ans) {
        ans.add(new ArrayList<>(iterm));

        for (int i=ind; i < nums.length; i++) {
            if (i != ind && nums[i] == nums[i-1]) {
                continue;
            }
            iterm.add(nums[i]);
            helper(i+1, nums, iterm, ans);
            iterm.remove(iterm.size() -1);
        }
        return;
    }
}