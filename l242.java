class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] a = new int[26];
        for (int i=0; i< s.length();i++) {
            a[s.charAt(i)-'a'] += 1;
        }
        for (int i=0; i< t.length();i++) {
            a[t.charAt(i)-'a'] -= 1;
        }
        for (int num: a){
            if (num != 0) return false;
        }
        return true;
    }
}