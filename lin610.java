import java.util.Arrays;
import java.util.Comparator;

// Two Sum - Difference equals to target

class pair {
    public int val;
    public int ind;
    pair(int val, int ind) {
        this.val = val;
        this.ind = ind;
    }
}

public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: an integer
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum7(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return nums;
        }
        if (target < 0) {
            target = -target;
        }

        pair[] ps = new pair[nums.length];

        for (int i = 0; i < nums.length; i++) {
            ps[i] = new pair(nums[i], i);
        }

        Comparator<pair> cmp = (first, second) -> Integer.compare(first.val, second.val);

        Arrays.sort(ps, cmp);

        int fast = 1;

        for (int i=0; i < ps.length; i ++) {
            while (ps[fast].val - ps[i].val < target || fast == i) {
                fast ++;
            }

            if (ps[fast].val - ps[i].val == target) {
                if (ps[i].ind < ps[fast].ind ) {
                    return new int[]{ps[i].ind + 1, ps[fast].ind + 1};
                } else {
                    return new int[]{ps[fast].ind + 1, ps[i].ind + 1};
                }
                
            }
        }

        return new int[]{0,0};
    }
}