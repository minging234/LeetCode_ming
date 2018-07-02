import java.util.*;

public class KNearest {
	public List<Point> findKClosest(List<Point> points, Point center, int k) {
        Comparator<Point> cmp = (p1, p2) -> Integer.compare(calDistance(p2, center),calDistance(p1, center));
        PriorityQueue<Point> queue = new PriorityQueue<>(cmp);
        List<Point> ans = new ArrayList<>();

        for (Point point:points) {
            if (queue.size() < k) {
                queue.add(point);
            } else {
                queue.add(point);
                queue.poll();
            }
        }

        while (!queue.isEmpty()) {
            ans.add(0,queue.poll());
        }
        return ans;
	}

	private int calDistance(Point p1, Point p2) {
		return (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y);
	}

	static class Point {
		int x;
		int y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) {
		KNearest test = new KNearest();
		Point center = new Point(0, 0);
		List<Point> points = new ArrayList<>();
		for (int i = -3; i < 7; i++) {
			points.add(new Point(i - 3, i * i - 9));
			int a = i-3;
			int b = i*i - 9;
			System.out.println(a + "," + b + " " + test.calDistance(center, new Point(a, b)));
		}
		System.out.println("------------------");

		List<Point> res = test.findKClosest(points, center, 5);
		for (Point p: res) {
			System.out.println(p.x + "," + p.y + " " + test.calDistance(center, p));
		}
	}
	
}