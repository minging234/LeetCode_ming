// Intersection of Two Arrays

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) {
            return new int[]{};
        }

        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> intersect = new HashSet<>();
        
        for (int i=0; i < nums1.length; i++) {
            set.add(nums1[i]);
        }
        
        for (int i=0; i < nums2.length; i++) {
            if (set.contains(nums2[i])) {
                intersect.add(nums2[i]);
            }
        }
        int[] ans = new int[intersect.size()];
        int i = 0;
        for (int num:intersect) {
            ans[i] = num;
            i ++;
        }
        return ans;
    }
}