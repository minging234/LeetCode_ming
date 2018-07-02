import java.util.LinkedList;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        // int a = 8;
        // double b = 7.0;

        // System.out.println(b-a);

        // List<Integer> a = new LinkedList<>();
        // a.add(1);
        // a.add(2);
        // a.add(3);

        // List<Integer> b = new LinkedList<>();     
        // b.addAll(a);
        
        // for (int ea:a) {
        //     System.out.println(ea);
        // }

        // b.set(1,0);

        // for (int ea:b) {
        //     System.out.println(ea);
        // }


        int[] a = new int[8];

        for (int i=0; i < a.length; i++) {
            if (i == 0 && a[i+1] == 0) {
                System.out.println("get first");
            } else if (i == a.length - 1 && a[i-1] == 0) {
                System.out.println("get last");
            } else {
                System.out.println("get middle");
            }
        }

    }
}