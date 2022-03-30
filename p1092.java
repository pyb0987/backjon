import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] NN = new int[N];
		for (int i =0 ; i <N ; i ++) {
			NN[i] = sc.nextInt();
		}
		int M = sc.nextInt();
		int[] MM = new int[M];
		for (int i =0 ; i <M ; i ++) {
			MM[i] = sc.nextInt();
		}
		sc.close();
		Arrays.sort(NN);
		int Mmax = Arrays.stream(MM).max().getAsInt();
		if (NN[N-1] < Mmax) {
			System.out.println(-1);
		}
		else {
			int maxx = (M%N==0) ? M/N : M/N+1 ;
			for (int i =0; i < N-1; i++) {
				int a = NN[i];
				int NNN=Arrays.stream(MM).filter(j->j>a).toArray().length;
				maxx = Math.max(maxx, (NNN%(N-1-i)==0) ? NNN/(N-1-i) : (NNN/(N-1-i)+1));
			}
			System.out.println(maxx);
		}
	}
}



