// Given a target number, a non-negative integer target and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

public class Solution {
    /**
     * @param A: an integer array
     * @param target: An integer
     * @param k: An integer
     * @return: an integer array
     */
    private int findlowerclosest(int[] A, int target) {
        int start = 0, end = A.length - 1;
        int[] ans = new int[k];

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[end] < target) {
            return end;
        }
        if (A[start] < target) {
            return start;
        }
        
        return -1;
    }

    private boolean isLeftCloser(int[] A, int target, int left, int right) {
        if (left < 0) {
            return false;
        }

        if (right >= A.length) {
            return true;
        }
        
        if (target - A[left] != A[right] - target) {
            return target - A[left] < A[right] - target;
        }
        
        return true;
    }

    public int[] kClosestNumbers(int[] A, int target, int k) {
        int left = findlowerclosest(A, target);
        int right = left + 1;
        int[] ans = new ans[k];

        for (int i=0; i < k; i++) {
            if (isLeftCloser(A, target, left, right)) {
                ans[i] = A[left];
                left -= 1;
            } else {
                ans[i] = A[right];
                right += 1;
            }
        }

        return ans;
    }
}