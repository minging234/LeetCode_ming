// Implement strStr()

public class Solution {
    /*
     * @param source: source string to be scanned.
     * @param target: target string containing the sequence of characters to match
     * @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
     */
    public int strStr(String source, String target) {
        // write your code here
        if (target == null || source == null) return -1;
        if (source.equals(target)) return 0;
        for(int i = 0; i < source.length() - target.length() + 1; i++) {
            int j = 0;
            while(j < target.length()){
                if(source.charAt(i+j) != target.charAt(j)) break;
                j++;
            }
            if(j == target.length()) return i;
        }
        return -1;
    }
}