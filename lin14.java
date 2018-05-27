// For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length;

        while (start + 1 < end) {
            int mid = start + ((end - start) >> 1);
            if (nums[mid] == target && mid - 1 >=0 && nums[mid] < target) {
                return mid;
            }
            if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (nums[start] == target) {
            if (start == 0) {
                return start;
            } else if (nums[start - 1] < target) {
                return start;
            }
        }
        if (nums[end] == target && end - 1 >=0 && nums[end - 1] < target) {
            return end;
        }
        return -1;
    }
}