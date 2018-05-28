import java.util.List;

// Given an array of integers and a number k, the majority number is the number that occurs more than 1/k of the size of the array.

public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer
     * @return: The majority number
     */
    public int majorityNumber(List<Integer> nums, int k) {
        int[] can = new int[k-1];
        int[] count = new int[k-1];

        int pos = 0;
        can[pos] = nums.get(0);

        for (int n: nums) {
            int i = 0;
            while (i <= pos) {
                if (can[i] == n) {
                    count[i] += 1;
                    break;
                } 
                i += 1;
            }

            if (i > pos) {
                if (i <= k-1) {
                    pos = i;
                    can[pos] = n;
                    count[pos] = 1;
                } else {
                    i = 0;
                    while (i <= pos) {
                        if (count[i] == 0) {
                            can[i] = n;
                            count[i] = 1;
                            break;
                        } 
                        i += 1;
                    }
                    if (i > pos) {
                        for(int j=0; j <= pos; j++) {
                            count[j] -= 1;
                        }
                    }
                }

            }
        }

        int[] dcount = new int[pos+1]; 
        int ans = can[0];
        int max = 0;

        for (int n: nums) {
            for (int i=0; i <= pos; i++) {
                if (n == can[i]) {
                    dcount[i] += 1;
                    if (dcount[i] > max) {
                        max =  dcount[i];
                        ans = can[i];
                    }
                }
            }
        }
        
        return ans;

    }
}