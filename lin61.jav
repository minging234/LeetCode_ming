// Search for a Range

public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        if (A == null || A.length ==0) {
            return new int[]{-1, -1};
        }

        int start = 0, end = A.length -1;
        int front = -1, back = -1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] == target) {
            front = start;
        } else if (A[end] == target) {
            front = end;
        }

        start = 0;
        end = A.length -1;

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (A[mid] > target) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (A[end] == target) {
            back = end;
        } else if (A[start] == target) {
            back = start;
        }

        return new int[]{front, back};

    } 
}