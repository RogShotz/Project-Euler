import java.util.ArrayList;
import java.util.List;

public class p7 {
    public static void main(String[] args) {
        ArrayList<Integer> primes = new ArrayList<>();
        int num = 1; // Start at one due to immediate increase

        while (primes.size() != 10001) {
            num++;
            boolean prime = true;
            for (int i = 0; i < primes.size(); i++) {
                if (num % primes.get(i) == 0) {
                    prime = false;
                }
            }
            if (prime) {
                primes.add(num);
                System.out.println(num);
            }
        }
        System.out.println("10001th Prime:" + num);
    }
}
