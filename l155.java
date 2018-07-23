// Min Stack

class MinStack {

    /** initialize your data structure here. */
    private int[] data;
    int size;
    int top;
    int minVal;

    public MinStack() {
        this.size = 10;
        this.data = new int[this.size];
        this.top = -1;
        this.minVal = Integer.MAX_VALUE;
    }
    
    public void push(int x) {
        top += 1;
        if (this.size == top) {
            this.size *= 2;
            int[] newData = new int[this.size];
            System.arraycopy(data, 0, newData, 0, top);
            this.data = newData;
        } 
        data[top] = x;
        
        if (x < this.minVal) {
            this.minVal = x;
        }
    }
    
    public void pop() {
        if (top >= 0) {
            if (data[top] == minVal) {
                minVal = Integer.MAX_VALUE;
                for (int i=0; i<top; i++) {
                    minVal = data[i] < minVal?data[i]:minVal;
                }
            }
            data[top] = 0;
            top -= 1;
        }
    }
    
    public int top() {
        return data[top];
    }
    
    public int getMin() {
        return minVal;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */