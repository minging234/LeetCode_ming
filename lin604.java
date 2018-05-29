// Window Sum

public class Solution {
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    public int[] winSum(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return nums;
        }
        int[] outc = new int[nums.length - k + 1];
        int ans = 0;
        int start = 0, end = k;

        for (int i=0; i < k; i ++){
            ans += nums[i];
        }

        outc[start] = ans; 

        while (end < nums.length) {
            ans = ans - nums[start] + nums[end];
            start ++;
            end ++;
            outc[start] = ans;
        }

        return outc;
    }
}