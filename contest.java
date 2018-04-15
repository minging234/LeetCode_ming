class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        if (sx > tx || sy > ty) return false;
        if (sx == tx && sy == ty) return true;
        if (tx >= ty){
            tx = tx - ty;
        }
        else{
            ty = ty - tx;
        }
        return reachingPoints(sx,sy,tx,ty);
    }
}