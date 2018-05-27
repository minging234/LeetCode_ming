// Implement pow(x, n).

public class Solution {
    /*
     * @param x: the base number
     * @param n: the power number
     * @return: the result
     */
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }

        if (n < 0) {
            x = 1/x;
            n = -n;
        } 

        int pow = 1;
        double ans = x;
        while (2 * pow < n) {
            ans *= ans;
            pow += pow;
            if (ans == 0) {
                return 0;
            }
        }

        ans *= myPow(x, n - pow);

        return ans;

    }
}