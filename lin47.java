import java.util.List;

// Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.

public class Solution {
    /*
     * @param nums: a list of integers
     * @return: The majority number that occurs more than 1/3
     */
    public int majorityNumber(List<Integer> nums) {
        int count_1 = 0, count_2 = 0;
        int cand_1 = nums.get(0), cand_2 = nums.get(0);

        for (int n: nums) {
            if (n == cand_1) {
                count_1 += 1;
            } else if (n == cand_2) {
                count_2 += 1;
            } else {
                if (cand_1 == cand_2) {
                    cand_2 = n;
                    count_2 = 1;
                } else if (count_1 == 0) {
                    cand_1 = n;
                    count_1 = 1;
                } else if (count_2 == 0) {
                    cand_2 = n;
                    count_2 = 1;
                } else {
                    count_1 -= 1;
                    count_2 -= 1;
                }
            }
        }
        count_1 = 0;
        count_2 = 0;
        for (int n: nums) {
            if (n == cand_1) count_1 += 1;
            if (n == cand_2) count_2 += 1;
        }

        return count_1 > count_2 ? cand_1 : cand_2;
    }
}