package com.company;

public class Main {

  public static void main(String[] args) {
    int count = 0;
    while (count != 5) {
      System.out.println("Count value is " + count);
      count++;
    }

    count = 0;
    while (true) {
      if (count == 5) {
        break;
      }
      System.out.println("Count value is " + count);
      count++;
    }

    System.out.println("\n");

    // Does the same thing as the while loop above

    for (count = 0; count < 5; count++) {
      System.out.println("Count value is " + count);
    }

    System.out.println("\n");

    count = 0;
    do {
      System.out.println("Count value was " + count);
      count++;
    } while (count != 5);

    System.out.println("\n");

    int number = 4;
    int finishNumber = 20;
    int totalEven = 0;
    while (number <= finishNumber) {
      if (isEvenNumber(number)) {
        totalEven++;
        System.out.println("Even number " + number);
      }
      if (totalEven >= 5) {
        System.out.println(totalEven + " even numbers found");
        break;
      }
      number++;
    }

    // Modify the while code above
    // Make it also record the total number of even numbers it has found
    // and break once 5 a4re found
    // and at the end, display the total number of even numbers found
  }

  // Create a method called IsEvenNumber that takes a parameter of type int
  // It's purpose is to determine if the argument passed to the method is
  // an even number or not.
  // Return true it an even number, otherwise return false.

  public static boolean isEvenNumber(int number) {
    if (number % 2 == 0) {
      return true;
    } else {
      return false;
    }
  }
}
