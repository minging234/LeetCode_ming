import java.util.ArrayList;

// Find the Celebrity


/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

      public class Solution extends Relation {
        /**
         * @param n a party with n people
         * @return the celebrity's label or -1
         */
        public int findCelebrity(int n) {
            if (n == 0 || n == 1) {
                return 0;
            }
            ArrayList<Integer> cand = new ArrayList<>();

            for (int i = 1; i < n; i++) {
                if (knows(0,i) && !knows(i,0)) {
                    cand.add(i);
                }
            }

            for (int i = 1; i < n; i++) {
                ArrayList<Integer> newCand = new ArrayList<>();
                for (int person: cand) {
                    if (knows(i,person) || !knows(person,i)) {
                        newCand.add(person);
                    }
                }
                cand = newCand;
            }

            if (cand.size() != 1) {
                return -1;
            } else {
                return cand.get(0);
            }
        }
    }