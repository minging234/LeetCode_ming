import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

// Topological Sorting

/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        if (graph == null || graph.size() == 0) {
            return graph;
        }

        HashMap<DirectedGraphNode, Integer> indegree = new HashMap<>();
        
        for (DirectedGraphNode node: graph) {
            for (DirectedGraphNode neigbor: node.neighbors) {
                if (indegree.containsKey(neigbor)) {
                    indegree.put(neigbor, indegree.get(neigbor) + 1);
                } else {
                    indegree.put(neigbor, 1);
                }
            }
        }

        LinkedList<DirectedGraphNode>zeroIn = new LinkedList<>();

        for (DirectedGraphNode node: graph) {
            if (!indegree.containsKey(node)) {
                zeroIn.add(node);
            }
        }

        ArrayList<DirectedGraphNode> ans = new ArrayList<>();

        while (zeroIn.size() > 0) {
            DirectedGraphNode curr = zeroIn.poll();
            ans.add(curr);
            for (DirectedGraphNode node: curr.neighbors) {
                int de = indegree.get(node);
                de --;
                if (de == 0) {
                    zeroIn.add(node);
                }
                indegree.put(node, de);
            }
        }

        return ans;

    }
} 