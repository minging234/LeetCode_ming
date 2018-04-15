class Solution {
    public int expressiveWords(String S, String[] words) {
        int ans=0;
        for(String word: words){
            if(word.length() > S.length()) continue;
            int i=0,j=0;
            boolean flag = true;
            while(i < word.length() && j < S.length()){
                int count1=0,count2=0;
                if(word.charAt(i) != S.charAt(j)) {
                    flag = false;
                    break;
                }
                while(i+1 < word.length() && word.charAt(i)==word.charAt(i+1)){
                    count1++;
                    i++;
                } 
                while(j+1 < S.length() && S.charAt(j)==S.charAt(j+1)){
                    count2++;
                    j++;
                } 

                if(count2 - count1 == 1 ||count2 - count1 < 0) {
                    flag =false;
                    break;
                }
                i++;
                j++;

            }
            if(flag && j==S.length()) ans ++;
        }
        return ans;
    }
    
}