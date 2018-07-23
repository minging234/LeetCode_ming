// Java code for Josephus Problem
import java.io.*;

class GFG {

static int josephus(int n, int k)
{
if (n == 1)
	return 1;
else
	/* The position returned by josephus(n - 1, k) 
	is adjusted because the recursive call 
	josephus(n - 1, k) considers the original 
	position k%n + 1 as position 1 */
	System.out.println("----" + n);
	int a = (josephus(n - 1, k) + k-1) % n + 1;
	System.out.println(a);
	return a;
}

// Driver Program to test above function
public static void main(String[] args)
{
int n = 5;
int k = 2;
System.out.println("The chosen place is " + josephus(n, k));
}
}

// This code is contributed by Prerna Saini
