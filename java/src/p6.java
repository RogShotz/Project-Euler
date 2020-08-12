public class p6 {
    public static void main(String[] args) {
        int sumof = 0; // Sum of squares
        int squareof = 0; // Square of sums

        for(int i = 1; i <= 100; i++) {
            sumof += i*i;
        }
        for(int i = 1; i <= 100; i++) {
            squareof += i;
        }
        squareof *= squareof;

        System.out.println(squareof-sumof);
    }
}
