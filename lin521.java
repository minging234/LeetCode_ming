import java.util.Arrays;

// Remove Duplicate Numbers in Array

public class Solution {
    /*
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int fast = 0, slow = 0;
        Arrays.sort(nums);
        while (fast < nums.length) {
            if (fast == nums.length -1 || nums[fast + 1] != nums[fast]) {
                nums[slow] = nums[fast];
                slow ++;
            }
            fast ++;
        }
        return slow;
    }
}