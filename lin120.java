import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

// Word Ladder

public class lin120 {
    /*
     * @param start: a string
     * @param end: a string
     * @param dict: a set of string
     * @return: An integer
     */
    // public int ladderLength(String start, String end, Set<String> dict) {
    //     if (dict.size() == 0 || dict == null) {
    //         return 0;
    //     }

    //     if (start == end) {
    //         return 1;
    //     }

    //     char[] transform = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

    //     List<String> startFringe = new LinkedList<>();
    //     List<String> endFringe = new LinkedList<>();
    //     startFringe.add(start);
    //     endFringe.add(end);


    //     Set<String> startExplored = new HashSet<>();
    //     Set<String> endExplored = new HashSet<>();
    //     startExplored.add(start);
    //     endExplored.add(end);


    //     int step = 1;

    //     while (!startFringe.isEmpty() && !endFringe.isEmpty()) {
    //         step ++;
    //         int startsize = startFringe.size();

    //         for (int count = 0; count < startsize; count++) {
    //             char[] cs = startFringe.get(count).toCharArray();
    //             for (int i=0; i < cs.length; i++) {
    //                 char origin = cs[i];  
    //                 for (int j=0; j < transform.length; j++) {
    //                     cs[i] = transform[j];
    //                     String possible = cs.toString();
    //                     if (endExplored.contains(possible)) {
    //                         return step;
    //                     }
    //                     if (dict.contains(possible) && !startExplored.contains(possible)) {
    //                         startFringe.add(possible);
    //                         startExplored.add(possible);
    //                     }
    //                 }
    //                 cs[i] = origin;
    //             }
    //         }

    //         step ++;
    //         int endsize = endFringe.size();

    //         for (int count = 0; count < endsize; count++) {
    //             char[] cs = startFringe.get(count).toCharArray();
    //             for (int i=0; i < cs.length; i++) {
    //                 char origin = cs[i];  
    //                 for (int j=0; j < transform.length; j++) {
    //                     cs[i] = transform[j];
    //                     String possible = cs.toString();
    //                     if (startExplored.contains(possible)) {
    //                         return step;
    //                     }
    //                     if (dict.contains(possible) && !endExplored.contains(possible)) {
    //                         endFringe.add(possible);
    //                         endExplored.add(possible);
    //                     }
    //                 }
    //                 cs[i] = origin;
    //             }
    //         }
    //     }

    //     return 0;

    // }


    public int ladderLength(String start, String end, Set<String> dict) {
        if (dict.size() == 0 || dict == null) {
            return 0;
        }

        if (start.equals(end)) {
            return 1;
        }

        char[] transform = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

        dict.add(start);
        dict.add(end);

        LinkedList<String> startFringe = new LinkedList<>();
        Set<String> startExplored = new HashSet<>();

        startFringe.add(start);
        startExplored.add(start);

        int step = 1;

        while (!startFringe.isEmpty()) {
            step ++;
            int size = startFringe.size();

            for (int k=0; k < size; k++){
                StringBuilder strBuilder = new StringBuilder(startFringe.poll());
                for (int i=0; i < strBuilder.length(); i++) {
                    char origin = strBuilder.charAt(i);  
                    for (int j=0; j < transform.length; j++) {
                        strBuilder.setCharAt(i, transform[j]);
                        String possible = strBuilder.toString();

                        if (possible.equals(end)) {
                            return step;
                        }
                        if (dict.contains(possible) && !startExplored.contains(possible)) {
                            startFringe.add(possible);
                            startExplored.add(possible);
                        }
                    }
                    strBuilder.setCharAt(i, origin);
                }
            }
        }

        return 0;

    }

    public static void main(String[] args) {

        lin120 s = new lin120();
        String start = "a";
        String end = "c";
        Set<String> dict = new HashSet<>();
        dict.add("a");
        dict.add("b");
        dict.add("c");
        int ans = s.ladderLength(start, end, dict);
        System.out.println(ans);
    }
} 