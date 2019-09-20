public class p1 {
    public static void main (String[] args) {
        int sum = 0;
        int number = 1000;

        for (int i = 1; i < number; i++) {
            if (i % 3 == 0 || i % 5 == 0) { // all we need to know is if i is divisible by 5 or 3
                sum += i;
            }
        }

        System.out.println("The sum all divisible numbers below " + sum + " is: ");
    }


    // If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    //
    //Find the sum of all the multiples of 3 or 5 below 1000.
}
