import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class p8 {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Integer> num = loader();
        long largest = 0; // Largest is so big it needs to be long

        for(int i = 0; i < num.size()-12; i++) { // -12 because it starts at 0 and it needs 13 digits to calc
            long temp = 1; // Temp also has to be a long for the same reason
            for(int j = 0; j < 13; j++) {
                temp *= num.get(i + j);
                System.out.println("I: " + i + " |J: " + j + " |Temp:" + temp);
            }
            if(temp > largest) {
                largest = temp;
                System.out.println(largest);
            }
        }
        System.out.println("Largest adjacent multiple: " + largest);
    }

    public static ArrayList<Integer> loader() throws FileNotFoundException {
        ArrayList<Integer> result = new ArrayList<>();
        Scanner file = new Scanner(new File("p8number.txt"));
        while (file.hasNext()) {
            char[] numbers = file.nextLine().toCharArray();
            for (int i = 0; i < numbers.length; i++) {
                result.add(Character.getNumericValue(numbers[i]));
            }
        }
        return result;
    }
}
