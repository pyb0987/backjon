import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] a = sc.next().toCharArray();
		char[] b = sc.next().toCharArray();
		sc.close();
		if (a.length!=b.length) {
			System.out.println(0);
		}
		else {
			int ans = 0;
			for (int i=0;i<a.length; i++) {
				if (a[i]!=b[i]) {
					break;
				}
				if (a[i]=='8') {
					ans++;
				}
			}
			System.out.println(ans);
		}
	}
}
