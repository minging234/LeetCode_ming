import oracle.jrockit.jfr.events.EventHandlerImpl;

class Solution {
    public String removeKdigits(String num, int k) {
        char[] dig = num.toCharArray();
        int change = 0;
        Stack<Character> stack = new Stack<>();
        for(int i=0; i< dig.length;i++){
            while(!stack.empty() && stack.peek() > dig[i] && change < k){
                stack.pop();
                change ++;
            }
            stack.push(dig[i]);
        }
        while(!stack.empty() && change < k){
            stack.pop();
            change ++;
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.empty()) {
            sb.append(stack.pop());
        }
        while(sb.length() > 0 && sb.charAt(sb.length()-1) == '0') {
            sb.deleteCharAt(sb.length()-1);
        }
        sb.reverse();
        if (sb.length() == 0) return "0";
        return sb.toString();
        
    }
}