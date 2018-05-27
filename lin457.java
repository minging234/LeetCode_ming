// Find any position of a target number in a sorted array. Return -1 if target does not exist.

public class Solution {
    /*
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    // public int findPosition(int[] nums, int target) {
    //     int start = 0;
    //     int end = nums.length - 1;
    //     return helper(nums, target, start, end);
    // }

    // private int helper(int[] nums, int target, int start, int end) {
    //     if (start > end) {
    //         return -1;
    //     } 
        
    //     int mid = (start + end)/2;
    //     if (nums[mid] == target) {
    //         return mid;
    //     }

    //     if (nums[mid] < target) {
    //         start = mid + 1;
    //         return helper(nums, target, start, end);
    //     }

    //     end = mid - 1;
    //     return helper(nums, target, start, end);
    // }

    public int findPosition(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int mid;
        
        while (start <= end) {
            mid = (start + end)/2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return -1;
    }   

}