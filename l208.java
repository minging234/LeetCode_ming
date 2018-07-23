import java.util.ArrayList;
import java.util.List;

// Implement Trie (Prefix Tree)

class l208 {

    private class TrieNode {
        char val;
        List<TrieNode> next;
        TrieNode(char c) {
            this.val = c;
            next = new ArrayList<>();
        }
    }

    /** Initialize your data structure here. */

    private TrieNode root;

    public l208() {
        root = new TrieNode('@');
    }

    private TrieNode nextNodeHelper(TrieNode cur, char c) {
        for (TrieNode node:cur.next) {
            if (node.val == c) {
                return node;
            }
        }
        return cur;
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode cur = root;

        for (int i=0; i < word.length(); i++) {     
            char c = word.charAt(i);
            TrieNode next = nextNodeHelper(cur, c);
            if (cur == next) {
                TrieNode newNode = new TrieNode(c);
                cur.next.add(newNode);
                cur = newNode;
            } else {
                cur = next;
            }
        }

        TrieNode end = new TrieNode('#');
        cur.next.add(end);
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode cur = root;
        for (int i=0; i < word.length(); i++) {
            char c = word.charAt(i);
            TrieNode next = nextNodeHelper(cur, c);
            if (next == cur) {
                return false;
            } else {
                cur = next;
            }
        }
        for (TrieNode node:cur.next) {
            if (node.val == '#') {
                return true;
            }
        }
        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode cur = root;

        for (int i=0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            TrieNode next = nextNodeHelper(cur, c);
            if (next == cur) {
                return false;
            } else {
                cur = next;
            }
        }
        return true;        
    }

    public static void main(String[] args) {
        l208 obj = new l208();
        obj.insert("apple");
        System.out.println(obj.search("apple"));
        System.out.println(obj.startsWith("apple"));
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */