public class Manacher {
    public int longest(String s) {
        String pre = "#";
        for (int i=0; i<s.length(); i++) {
            pre = pre + s.charAt(i) + "#";
        }

        int[] RL = new int[pre.length()];
        int MaxRight = 0;
        int pos = 0;
        int MaxLen = 0;

        for (int i=0; i < pre.length(); i++) {
            if (i < MaxRight) RL[i] = Math.min(RL[2*pos - i], MaxRight -i);
            else RL[i] = 1;

            while (i - RL[i] >=0 && i + RL[i] < pre.length() && pre.charAt(i-RL[i]) == pre.charAt(i + RL[i])) {
                RL[i] += 1;
            }

            if (RL[i] + i -1 > MaxRight) {
                MaxRight = RL[i] + i - 1;
                pos = i;
            }
            MaxLen = Math.max(MaxLen, RL[i]);
        }

        return MaxLen - 1;
        
    }

    public String longestSubP(String s) {
        if (s == null || s.length() == 0) return "";
        String pre = "#";
        for (int i=0; i <s.length(); i++) {
            pre = pre + s.charAt(i) + "#";
        }

        int[] RL = new int[pre.length()];
        int MaxRight = 0;
        int pos = 0;
        int MaxLen = 0;
        String ans = "";

        for (int i=0; i < pre.length(); i ++) {
            if (i < MaxRight) RL[i] = Math.min(RL[2*pos - i], MaxRight - i);
            else RL[i] = 1;

            while(i - RL[i] >=0 && i + RL[i] < pre.length() && pre.charAt(i - RL[i]) == pre.charAt(i + RL[i])) {
                RL[i] += 1;
            }

            if (RL[i] + i -1 > MaxRight) {
                MaxRight = RL[i] + i -1;
                pos = i;
            }

            if (MaxLen < RL[i]) {
                MaxLen = Rl[i];
                ans = pre.substring(i - RL[i], i + RL[i]).replace("#", "");
            }

            return ans;
        }

    }
}