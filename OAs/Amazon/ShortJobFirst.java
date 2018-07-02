import java.util.Comparator;
import java.util.PriorityQueue;

public class ShortestJobFirst {
    private class process {
        int arr;
        int dur;
        process (int arr, int dur) {
            this.arr = arr;
            this.dur = dur;
        }
    }

    public float Solution(int[] req, int[] dur) {
        if (req == null || dur == null || req.length != dur.length) {
            return 0;
        }
        int index = 0;
        int currTime = 0;
        int waitTime = 0;
        Comparator<process> cmp = (p1, p2) -> p1.dur - p2.dur != 0 ? p1.dur - p2.dur : p1.arr - p1.arr;
        PriorityQueue<process> que = new PriorityQueue<>(cmp);

        while (!que.isEmpty() || index < req.length) {
            if (!que.isEmpty()) {
                process exeProcess = que.poll();
                currTime += exeProcess.dur;
                waitTime += currTime - exeProcess.arr;
                
                while (req[index] <= currTime && index < req.length) {
                    que.offer(new process(req[index], dur[index]));
                    index ++;
                }

            } else {
                currTime = req[index];
                while (req[index] == currTime) {
                    que.offer(new process(req[index], dur[index]));
                    index ++;
                }
            }
        }

        return (float)waitTime/index;
    }
}