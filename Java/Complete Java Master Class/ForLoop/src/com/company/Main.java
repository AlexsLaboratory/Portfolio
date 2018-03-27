package com.company;

public class Main {

  public static void main(String[] args) {
    System.out.println("10,000 at 2% interest = " + calculateInterest(10000, 2));
    System.out.println("10,000 at 3% interest = " + calculateInterest(10000, 3));
    System.out.println("10,000 at 4% interest = " + calculateInterest(10000, 4));
    System.out.println("10,000 at 5% interest = " + calculateInterest(10000, 5));

    for (int i = 0; i < 5; i++) {
      System.out.println("Loop " + i + " hello!");
    }

    // using the for statement, call the calculateInterest method with
    // the amount of 10000 with an interestRate of 2, 3, 4, 5, 6, 7, and 8
    // and print the results to the console window

    for (int i = 2; i <= 8; i++) {
      System.out.println("10,000 at " + i + "% interest = " + String.format("%.2f", calculateInterest(10000, i)));
    }

    System.out.println("\n");

    // How would you modify the for loop above to do the same thing as
    // show but to start from 8% adn work back to 2%

    for (int i = 8; i >= 2; i--) {
      System.out.println("10,000 at " + i + "% interest = " + String.format("%.2f", calculateInterest(10000, i)));
    }

    System.out.println("\n");

    // Create a for statement using any range of numbers
    // Determine if the number is a prime number using the isPrime method
    // if it is a prime, print it out AND increment a count of the
    // number of prime numbers found
    // if that count is 3 exit the for loop
    // hint: Use the break statement to exit

    int count = 0;
    for (int i = 1; i <= 512; i++) {
      if (isPrime(i)) {
        System.out.println(i + " is a prime number");
        count++;
        if (count == 3) {
          break;
        }
      }
    }
  }

  public static double calculateInterest(double amount, double interestRate) {
    return (amount * (interestRate / 100));
  }

  public static boolean isPrime(int n) {
    if (n == 1) {
      return false;
    }
    for (int i = 2; i <= n/2; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}