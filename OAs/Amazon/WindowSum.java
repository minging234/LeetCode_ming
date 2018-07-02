import java.util.*;

public class WindowSum {
	public List<Integer> calculate(List<Integer> list, int window) {
        List<Integer> ans = new ArrayList<>();
        if (list == null || list.size() == 0 || window <= 0) {
            return ans;
        }
        int sum = 0;
        
        for (int i=0; i < window && i < list.size(); i++) {
            sum += list.get(i);
        }
        ans.add(sum);

        for (int i=window; i < list.size(); i++) {
            sum -= list.get(i-window);
            sum += list.get(i);
            ans.add(sum);
        }
        return ans;
	}

	public static void main(String[] args) {
		WindowSum test = new WindowSum();
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < 10; i++) {
			list.add(i);
		}
		List<Integer> res = test.calculate(list, 3);
		for (Integer i: res) {
			System.out.print(i + ",");
		}
		System.out.println();
	}
}