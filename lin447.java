// Search in a Big Sorted Array
// Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

public class Solution {
    /*
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return: An integer which is the first index of target.
     */
    public int searchBigSortedArray(ArrayReader reader, int target) {
        if (reader.get(0) == target) {
            return 0;
        }
        if (reader.get(0) < target) {
            return -1;
        }

        int start = 1;
        int end  = start *2;
        while (reader.get(end) < target) {
            start = end;
            end = end * 2;
        }      

        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (reader.get(mid) < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (reader.get(start) == target) {
            return start;
        } 
        if (reader.get(end) == target) {
            return end;
        }
        return -1;
    }
}