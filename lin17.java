import java.util.ArrayList;

// Subsets

public class Solution {
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> iterm = new ArrayList<>();
        if (nums == null) {
            return ans;
        }
        Arrays.sort(nums);
        helper(0, nums, ans, iterm);
        return ans;
    }

    private void helper(int ind, int[] nums, List<List<Integer>> ans, List<Integer> iterm) {
        ans.add(new ArrayList<>(iterm));
        
        for (int i=ind; i < nums.length; i++) {
            if (i != ind && nums[i] == nums[i -1]) {
                continue;
            }
            iterm.add(nums[i]);
            helper(i+1, nums, ans, iterm);
            iterm.remove(iterm.size() - 1);
        }
        return;
    }
}