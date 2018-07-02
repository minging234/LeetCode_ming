import java.util.ArrayList;
import java.util.LinkedList;

// Combination Sum II

public class Solution {
    /**
     * @param num: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        LinkedList<Integer> iterm = new LinkedList<>();
        Arrays.sort(num);
        helper(num, 0, 0, target, ans, iterm);
        List<List<Integer>> newans = new ArrayList<>();
        for (int i=ans.size()-1; i>=0;i--) {
            newans.add(ans.get(i));
        }
        return newans;
    }

    private void helper(int[] num, int ind, int currsum, int target, List<List<Integer>> ans, LinkedList<Integer> iterm) {
        if (ind == num.length || currsum > target) {
            return;
        }
        if (currsum == target) {
            List<Integer> newiterm = new ArrayList<>(iterm);
            ans.add(newiterm);
            return;
        }
        int p = 1;
        while (ind+p < num.length && num[ind] == num[ind+p]) {
            p++;
        }
        for (int i=0; i <= p; i++) {
            for (int j=0; j < i; j++) {
                iterm.offerLast(num[ind]);
                currsum += num[ind];
            }
            helper(num, ind + p, currsum, target, ans, iterm);
            for (int j=0; j < i; j++) {
                iterm.pollLast();
                currsum -= num[ind];
            }
        }
        return;
    }

    // public List<List<Integer>> combinationSum2(int[] candidates, int target) {
    //     List<List<Integer>> results = new ArrayList<>();
    //     if (candidates == null || candidates.length == 0) {
    //         return results;
    //     }

    //     Arrays.sort(candidates);
    //     List<Integer> combination = new ArrayList<Integer>();
    //     helper(candidates, 0, combination, target, results);

    //     return results;
    // }

    // private void helper(int[] candidates,
    //                 int startIndex,
    //                 List<Integer> combination,
    //                 int target,
    //                 List<List<Integer>> results) {
    //     if (target == 0) {
    //         results.add(new ArrayList<Integer>(combination));
    //         return;
    //     }

    //     for (int i = startIndex; i < candidates.length; i++) {
    //         if (i != startIndex && candidates[i] == candidates[i - 1]) {
    //             continue;
    //         }
    //         if (target < candidates[i]) {
    //             break;
    //         }
    //         combination.add(candidates[i]);
    //         helper(candidates, i + 1, combination, target - candidates[i], results);
    //         combination.remove(combination.size() - 1);
    //     }
    // }
}