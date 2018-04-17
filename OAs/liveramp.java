
class Main
{
    static void printUnsorted(int arr[], int n) {
        int cadl = 0;
        int cadh = arr.length;
        for(int i = 1; i< arr.length; i++) {
            if (arr[i] < arr[i-1]) {
                cadl = i;
                break;
            }
        }
        for(int i = arr.length-1; i > 0; i--) {
            if (arr[i-1] > arr[i]) {
                cadh = i;
                break;
            }
        }
        int pmin = Integer.MAX_VALUE;
        int pmax = Integer.MIN_VALUE;
        for (int i = cadl;i <= cadh;i++) {
            if (pmin > arr[i]) pmin = arr[i];
            if (pmax < arr[i]) pmax = arr[i];
        }
        int s = cadl;
        for (int i = cadl; i >= 0; i--) {
            if (arr[i] > pmin) s = i;
            else break;
        }
        int e = cadh;
        for (int i = cadh; i < arr.length; i++) {
            if (arr[i] < pmin) e = i;
            else break;
        }
        System.out.print(s);
        System.out.print(e);
        return;
    }
}


int lengthOfLongestSubstring(string s) {

    int[] map = new int[128];
    int counter=0, begin=0, end=0, d=0; 
    while(end<s.size()){
        if(map[s[end++]]++>0) counter++; 
        while(counter>0) if(map[s[begin++]]-->1) counter--;
        d=max(d, end-begin); 
    }
    return d;
}

