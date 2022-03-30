import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();	
		sc.close();
		if (N%M==0) {
			System.out.println(0);
		}
		else {
			System.out.println(cut((N%M),M));
			
		}
	}
	
	static int cut(int n, int m){
		int a = gcd(n,m);
		if (n!=1 && a !=1) {
			return a*cut(n/a,m/a);
		}
		return m-1;
	}


	static int gcd(int n, int m) {
		int minN = Math.min(n, m);
		int maxN = Math.max(n, m);
		int tmp;
		while (minN != maxN) {
			maxN -= minN;
			if (maxN<minN) {
				tmp = minN;
				minN = maxN;
				maxN = tmp;
			}
		}
		return maxN;
				
	}
}