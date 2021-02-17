import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PrimesDeterminerWithList {
    private static double testNumber;
    private static double divisor;
    private static double result;
    private static boolean factorable;

    public static void main(String[] args){
        System.out.println("Please input your number:");
        Scanner sc = new Scanner(System.in);
        testNumber = sc.nextDouble();
        divisor = 2;
        factorable = false;
        List<Double> factorsList = new ArrayList();
        while(testNumber>divisor){
            result = testNumber/divisor;
            if (result == Math.round(result)){
                factorsList.add(divisor);
                System.out.println("Thinking...");
            }
            divisor = divisor+1;
        }
        if (factorsList.isEmpty() == true){
            System.out.println(testNumber + " is a prime number");
        }
        else{
            System.out.println(testNumber + " is not a prime number with factors of " + factorsList.toString() );
        }
    }
}
