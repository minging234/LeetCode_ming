import java.util.HashMap;

class LRUCache {

    private class Node {
        int key;
        int val;
        Node pre;
        Node next;
        Node (int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
    private HashMap<Integer, Node> map = new HashMap<>();
    private Node dummyHead = new Node(-1, -1);
    private Node dummyTail = new Node(-1, -1);
    private int size = 0; 
    private int capacity;

    public LRUCache(int capacity) {
        dummyHead.next = dummyTail;
        dummyTail.pre = dummyHead;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        } else {
            Node curr = map.get(key);
            removeNode(curr);
            insertFirst(curr);
            return curr.val;
        }
    }
    private void insertFirst(Node curr) {
        curr.next = dummyHead.next;
        curr.pre = dummyHead;
        dummyHead.next.pre = curr;
        dummyHead.next = curr;
    }

    private void removeNode(Node curr) {
        curr.pre.next = curr.next;
        curr.next.pre = curr.pre;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node curr = map.get(key);
            curr.val = value;
            removeNode(curr);
            insertFirst(curr);
        } else {
            Node curr = new Node(key, value);
            insertFirst(curr);
            map.put(key, curr);
            this.size += 1;
            if (this.size > this.capacity) {
                Node discard = dummyTail.pre;
                removeNode(discard);
                map.remove(discard.key);
            }
        } 
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


// import java.util.LinkedHashMap;
// public class LRUCache {
//     private LinkedHashMap<Integer, Integer> map;
//     private final int CAPACITY;
//     public LRUCache(int capacity) {
//         CAPACITY = capacity;
//         map = new LinkedHashMap<Integer, Integer>(capacity, 0.75f, true){
//             protected boolean removeEldestEntry(Map.Entry eldest) {
//                 return size() > CAPACITY;
//             }
//         };
//     }
//     public int get(int key) {
//         return map.getOrDefault(key, -1);
//     }
//     public void set(int key, int value) {
//         map.put(key, value);
//     }
// }
