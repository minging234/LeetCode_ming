// Rectangle Area

class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int width = overLapLength(A, C, E, G);
        int height = overLapLength(B, D, F, H);
        return (C - A) * (D - B) + (G - E) * (H - F) - width * height;
    }
    private int overLapLength(int startA, int endA, int startB, int endB) {
        int begin = startB > startA ? startB:startA;
        int stop = endB < endA ? endB:endA;

        if (begin < stop) {
            return stop - begin;
        }
        return 0;
    }
}