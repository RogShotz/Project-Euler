public class p4 {
    public static void main(String[] args) {
        int largest = 0;
        for (int i = 100; i <= 999; i++) { // made from two 3 digit numbers
            for (int j = 100; j <= 999; j++) {
                int number = i * j;
                int convNum = number; // convNum is used and edited to convert the number.
                int reversed = 0;

                while (convNum != 0) {
                    int digit = convNum % 10; // gets the remainder
                    reversed = reversed * 10 + digit; // times by ten moving it up one place then appends digit
                    convNum /= 10; // moves number down one place to progress
                }

                // System.out.println(number + ":" + reversed);
                if (number == reversed) {
                    if (number > largest) {
                        largest = number;
                        System.out.println(largest);
                    }
                }
            }
        }
    }
}
