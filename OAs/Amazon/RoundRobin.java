import java.util.LinkedList;
import java.util.Queue;

class process {
    int arrTime;
    int exeTime;
    process(int arr, int exe) {
        arrTime = arr;
        exeTime = exe;
    }
}

public class RoundRobinScheduling {
    public float Solution(int[] Atime, int[] Etime, int q) {
        if (Atime == null || Etime == null || Atime.length != Etime.length) {
            return 0;
        }

        int currTime = 0;
        int waitTime = 0;
        int index = 0;
        Queue<process> queue = new LinkedList<>();

        while (!queue.isEmpty() && index < Atime.length) {
            if (!queue.isEmpty()) {
                process exeProcess = queue.poll();
                waitTime += currTime - exeProcess.arrTime;
                currTime += Math.min(exeProcess.exeTime, q);
                while (index < Atime.length && Atime[index] <= currTime) {
                    queue.offer(new process(Atime[index], Etime[index]));
                    index ++;
                }
                if (exeProcess.exeTime > q) {
                    queue.add(new process(currTime, exeProcess.exeTime - q));
                }

            } else {
                currTime = Atime[index];
                queue.offer(new process(Atime[index], Etime[index]));
                index ++;
            }
        }

        return (float)waitTime/A.length;
    }
}