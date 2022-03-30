import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] a = new int[num];
		for(int j =0; j < num; j++){
			a[j] = sc.nextInt();	
		}
		sc.close();
		for(int j =0; j < num; j++){
			if ( a[j] == 0) {
				System.out.println("1 0");
			}
			else if (a[j] == 1) {
				System.out.println("0 1");
			}
			else {
				int[] dp = new int[a[j]+1];
				dp[a[j]]=1;
				for (int i=a[j]; i>1; i--) {
					dp[i-1]+=dp[i];
					dp[i-2]+=dp[i];
				}
				System.out.println(dp[0]+" "+dp[1]);
			}
		}



	}
}