import java.util.ArrayList;
import java.util.Arrays;

// 3Sum

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return ans;
        }

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1;
            int end = nums.length - 1;
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            while (start < end) {
                int cur = nums[start] + nums[end] + nums[i];
                if (cur == 0) {
                    ans.add(Arrays.asList(nums[i], nums[start], nums[end]));
                    start ++;
                    while (start < end && nums[start] == nums[start - 1]) {
                        start ++;
                    }
                }
                if (cur < 0) {
                    start ++;
                } else {
                    end --;
                }
            }
        }

        return ans;
    }
}