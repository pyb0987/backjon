import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[][][] arr = new int[num][][]; 
		for(int i =0; i < num; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			arr[i] = new int[c][2];
			for(int j=0; j<c; j++) {
				arr[i][j][0] = sc.nextInt();
				arr[i][j][1] = sc.nextInt();
			}

			int change = 1;
			int[] ans = new int[c];  
			for (int j=0; j< c;j++) {
				ans[j]=j;
			}
			while (change==1) {
				change=0;
				for(int j=0; j<c; j++) {
					for(int k=0; k<c; k++) {
						if ((Math.abs(arr[i][j][0]-arr[i][k][0])==1 && arr[i][j][1]==arr[i][k][1] && ans[k]!=ans[j]) || (Math.abs(arr[i][j][1]-arr[i][k][1])==1 && arr[i][j][0]==arr[i][k][0] && ans[k]!=ans[j])){
							ans[k]= Math.min(ans[k], ans[j]);
							change=1;	
						}
					}
				}
			}
			Set<Integer> set = new HashSet<>();
			for(int j : ans) {
				set.add(j);
			}
			System.out.println(set.size());
		}
		sc.close();
	}




}