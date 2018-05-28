class Solution {
    public void nextPermutation(int[] nums) {
        int l = nums.length - 1;
        while(l > 0 && nums[l] <= nums[l-1]) {
            l--;
            if (l == 0) break;
        }

        if(l==0) {
            rev(nums,0,nums.length-1);
            return;
        }

        int target = l-1;
        l = nums.length - 1;
        while(nums[l] <= nums[target]) {
            l --;
        }

        int temp = nums[target];
        nums[target] = nums[l];
        nums[l] = temp;
        rev(nums,target+1,nums.length-1);
        return;
    }
    private int[] rev(int[] nums, int start, int end) {
        int temp;
        while(start < end) {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start ++;
            end --;
        }
        return nums;
    }
}