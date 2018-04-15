import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null){
                sb.append(node.val);
                sb.append(",");
                queue.add(node.left);
                queue.add(node.right);
            }
            else {
                sb.append("#");
                sb.append(",");
            }
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.length() == 0) return null;
        String[] datas = data.split(",");
        ArrayList<TreeNode> nodes = new ArrayList<>();
        for (int i=0; i < datas.length;i++) {
            if (!datas[i].equals("#")) {
                TreeNode node = new TreeNode(Integer.parseInt(datas[i]));
                nodes.add(node);
            } else {
                nodes.add(null);
            }
        }
        int fat = 0, son = 1;

        while (fat < datas.length) {
            if (datas[fat].equals("#")) {
                fat ++;
                continue;
            }
            TreeNode father = nodes.get(fat);
            if (son == datas.length) continue;
            father.left = nodes.get(son);   
            son ++;            
            if (son == datas.length) continue;    
            father.right = nodes.get(son);         
            son ++; 
            fat ++;
        }
        return nodes.get(0);
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));