import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		long n = Long.parseLong(str[0]);
		int k = Integer.parseInt(str[1]);
		
		int a = (int)n%k;
		long hop = (long)Math.pow(10, str[0].length());
		if (a==0) {
			System.out.println(1);		
		} else {
			int[] checker = new int[k];
			int i = 2;
			int b = a;
			while (true){
				checker[b] = 1;
				b = (int)((b*hop+a)%k);
				if (b==0) {
					System.out.println(i);
					break;
				} else if(checker[b]==1) {
					System.out.println(-1);
					break;
				}
				i++;
			}
		}
	}
}
