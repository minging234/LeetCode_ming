import java.util.Arrays;

// Two Sum - Difference equals to target

public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: an integer
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum7(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return nums;
        }
        Arrays.sort(nums);
    }
}