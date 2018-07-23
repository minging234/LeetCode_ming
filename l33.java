// Search in Rotated Sorted Array

class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int start = 0;
        int end = nums.length - 1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (nums[mid] > target) {
                if ((nums[mid] >= nums[0] && target >= nums[0]) || (nums[mid] < nums[0] && target < nums[0])) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else if (nums[mid] < target) {
                if ((nums[mid] >= nums[0] && target >= nums[0]) || (nums[mid] < nums[0] && target < nums[0])) {
                    start = mid;
                } else {
                    end = mid;
                }
            } else {
                return mid;
            }
        }
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }

        return -1;
    }
}