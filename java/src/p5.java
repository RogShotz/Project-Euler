public class p5 {
    public static void main(String[] args) {
        int num = 0;
        int found = 0;
        while (found != 10) { // Only 10 are needed
            num++;
            found = 0;
            for (int div = 11; div <= 20; div++) { // Start at 11 since everything all lower numbers fit in these
                if(num % div == 0) {
                    found++;
                }
            }
        }
        System.out.println("Smallest: " + num);
    }
}
