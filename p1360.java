import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(bf.readLine());
		String[] text = new String[N];
		for(int i =0; i<N; i++) {
			text[i]=bf.readLine();
		}
		StringBuilder sb = new StringBuilder();
		String[] sptext = new String[3];
		long deltime = 1000000001;
		for(int i = N-1; i > -1; i-- ) {
			sptext = text[i].split(" ");
			if (Long.parseLong(sptext[2])>=deltime) {
				continue;
			}
			else if(sptext[0].equals("undo")) {
				deltime = Long.parseLong(sptext[2])-Long.parseLong(sptext[1]);
				continue;
			}
			else if(sptext[0].equals("type")){
				sb.insert(0, sptext[1]);
			}
		}

		System.out.println(sb.toString());
	}
}
