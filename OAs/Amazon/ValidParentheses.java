import java.util.Scanner;
import java.util.Stack;

// l678. Valid Parenthesis String

class Solution {
    public int checkValidString(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        Stack<Character> stack = new Stack<>();

        for (int i=0; i < s.length(); i++) {
            if (stack.isEmpty()) {
                if (s.charAt(i) == '[') {
                    stack.push('[');
                } else {
                    return -1;
                }
            } else if (s.charAt(i) == ']') {
                stack.pop();
            } else if (s.charAt(i) == '[') {
                stack.push('[');
            }
        }

        if (stack.isEmpty()) {
            return s.length()/2;
        } else {
            return -1;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		while (s.length() > 0) {
			System.out.println(solution.checkValidString(s));
			s = sc.nextLine();
        }
        
        sc.close();
	}
}