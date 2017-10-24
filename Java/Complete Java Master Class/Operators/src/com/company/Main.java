package com.company;

public class Main {

  public static void main(String[] args) {
    int result = 1 + 2;
    System.out.println(result);

    int previousResult = result;

    result -= 1;
    System.out.println(result);

    previousResult = result;

    result *= 10;
    System.out.println(result);

    previousResult = result;

    result /= 5;
    System.out.println(result);

    previousResult =  result;

    result %= 3;
    System.out.println(result);

    previousResult = result;

    boolean isAlien = false;
    if (isAlien) {
      System.out.println("It is not an alien!");
    }

    int topScore = 100;
    if (topScore >= 100) {
      System.out.println("You got the top score!");
    }

    int secondTopScore = 80;
    if ((topScore > secondTopScore) && (topScore < 101)) {
      System.out.println("Greater than the top score and less then 101");
    }

    if ((topScore > 90) || (secondTopScore <= 90)) {
      System.out.println("One of these tests is true");
    }

    int newValue = 50;
    if (newValue == 50) {
      System.out.println("This is true");
    }

    boolean isCar = false;
    if (isCar) {
      System.out.println("This is not supposed to happen");
    }

    isCar = true;
    boolean wasCar = isCar ? true : false;
    if (wasCar) {
      System.out.println("wasCar is true");
    }

    /*
    * 1. Create a double variable with the value 20
    * 2. Create a second variable of type double with the value 80
    * 3. Add both numbers up and multiply by 25
    * 4. Use the remainder operator to figure out the remainder from the sum of #3 divided by 40
    * 5. Write an "if" statement that displays a message "Total was over the limit"
    * if the remainder total (#4) is equal to 20 or less
    */

    double varOne = 20;
    double varTwo = 80;
    double total = (varOne + varTwo) * 25;
    /* 2500 / 40 = 62.5
    * # Remove the remainder at the end of the number so 62.5 would then be 62
    * 62 * 40 = 2480
    * # This modulus operator will then produce a remainder of 20 because 40 could't go into 2500 evenly
    */
    double remainder = total % 40;
    if (remainder <= 20) {
      System.out.println("Total was over the limit");
    }
  }
}
