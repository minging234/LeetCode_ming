import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */

class DirectedGraphNode {
    int label;
        ArrayList<DirectedGraphNode> neighbors;
        DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
}

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        HashMap<DirectedGraphNode, Integer> map = new HashMap<>();
        for (DirectedGraphNode g: graph) {
            for (DirectedGraphNode n: g.neighbors) {
                if (map.containsKey(n)) map.put(n, map.get(n)+1);
                else map.put(n, 1);
            }
        }
        ArrayList<DirectedGraphNode> ans = new ArrayList<>();
        Queue<DirectedGraphNode> que = new LinkedList<>();
        for (DirectedGraphNode g: graph) {
            if (!map.containsKey(g)) {
                ans.add(g);
                que.offer(g);
            }
        }
        while (!que.isEmpty()) {
            DirectedGraphNode node = que.poll();
            for (DirectedGraphNode n: node.neighbors) {
                map.put(n, map.get(n)-1);
                if (map.get(n)==0) {
                    ans.add(n);
                    que.offer(n);
                }
            }
        }
        return ans;
    }
}