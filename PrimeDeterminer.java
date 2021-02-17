import java.util.Scanner;

public class PrimeDeterminer {
    private static double testNumber;
    private static int divisor;
    private static double result;
    private static boolean factorable;

    public static void main(String[] args){
        System.out.println("Please input your number:");
        Scanner sc = new Scanner(System.in);
        testNumber = sc.nextDouble();
        divisor = 2;
        factorable = false;
        while(testNumber>divisor){
            result = testNumber/divisor;
            if (result == Math.round(result)){
                System.out.println(testNumber + " has a factor of  " + divisor);
                factorable = true;
            }
            divisor = divisor+1;
        }
        if (factorable == false){
            System.out.println(testNumber + " is a prime number");
        }
        else{
            System.out.println(testNumber + " is not a prime number");
        }
    }
}
