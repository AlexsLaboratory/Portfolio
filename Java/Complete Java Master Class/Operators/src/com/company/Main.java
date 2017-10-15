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
    if (topScore > secondTopScore && topScore < 101) {
      System.out.println("Greater than the top score and less then 101");
    }
  }
}
