// Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

public class Solution {
    /*
     * @param nums: a list of integers
     * @return: find a  majority number
     */
    public int majorityNumber(List<Integer> nums) {
        int count = 0;
        int ans = 1;
        for (int n :nums) {
            if (n == ans) {
                count ++;
            } else {
                count --;
            }

            if (count < 0) {
                ans = n;
                count = 1;
            }
        }
        return ans;
    }
}