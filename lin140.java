// Calculate the an % b where a, b and n are all 32bit integers.

public class Solution {
    /**
     * @param a: A 32bit integer
     * @param b: A 32bit integer
     * @param n: A 32bit integer
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        if (n == 0) {
            return 1%b;
        }
        if (n == 1) {
            return a%b;
        }

        long mid = fastPower(a, b, n/2)%b;
        mid = (mid * mid)%b;

        if (n%2 == 1) {
            mid = (mid * a)%b;
        }
        return (int)mid%b;
    }
}