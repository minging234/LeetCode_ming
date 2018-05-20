//Implement strStr function in O(n + m) time.

public class Solution {
    /*
     * @param source: A source string
     * @param target: A target string
     * @return: An integer as index
     */
    public int BASE=1000000;

    public int strStr2(String source, String target) {
        if (source == null || target == null) return -1;

        int tlen = target.length();
        if (tlen == 0) return 0;

        //calculate power
        int power = 1;
        for (int i=0; i<tlen; i++) {
            power = (power * 31) % BASE;
        }

        //calculate the target hashcode
        int hashcode = 0;
        int patternCode = 0;
        for (int i=0; i<tlen; i++) {
            hashcode = (hashcode * 31 + target.charAt(i)) % BASE;
        }
        
        for (int i=0; i < source.length(); i++) {
            // append the last char
            patternCode = (patternCode * 31 + source.charAt(i)) % BASE;

            if (i < tlen -1){
                continue;
            }
            // strip the fist char
            if (i >= tlen) {
                patternCode = patternCode - (source.charAt(i - tlen) * power) % BASE;
                if (patternCode < 0) patternCode += BASE;
            }

            // double check if match
            if (hashcode == patternCode) {
                if (source.substring(i-tlen+1, i+1).equals(target)) {
                    return i-tlen+1;
                }
            }
        }

        return -1;

    } 
}