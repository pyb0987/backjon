import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();
		sc.close();
		int ans = 0;
		for (int i=N; i>0; i--) {
			ans += tf((r&(1<<(i-1)))==(1<<(i-1)))*2*Math.pow(4,i-1)+tf((c&(1<<(i-1)))==(1<<(i-1)))*Math.pow(4,i-1);	
		}
		System.out.println(ans);
	}
	
	public static int tf(boolean a) {
		if (a){
			return 1;
		}
		else {
			return 0;
		}
	}
}

