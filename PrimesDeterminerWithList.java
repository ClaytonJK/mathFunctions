import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import javax.swing.JComponent;
import javax.swing.KeyStroke;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class PrimesDeterminerWithList {
    private static double testNumber;
    private static double divisor;
    private static double result;
    private static JComponent abort;
    private static boolean stop;
    

    public static void main(String[] args) {
        System.out.println("To cancel long-running primes, press Ctrl + C");
        System.out.println("Please input your number:");
        Scanner sc = new Scanner(System.in);
        testNumber = sc.nextDouble();
        divisor = 2;
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
