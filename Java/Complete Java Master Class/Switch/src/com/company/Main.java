package com.company;

public class Main {

  public static void main(String[] args) {
    int value = 3;
    if (value == 1) {
      System.out.println("Value was 1");
    } else if (value == 2) {
      System.out.println("Value was 2");
    } else {
      System.out.println("Value was neither 1 or 2");
    }

    int switcValue = 8;
    switch (switcValue) {
      case 1:
        System.out.println("Value was 1");
        break;
      case 2:
        System.out.println("Value was 2");
        break;
      case 3:
      case 4:
      case 5:
        System.out.println("Value was a 3, 4, or 5");
        System.out.println("Actually it was a " + switcValue);
        break;
      default:
        System.out.println("Value was not 1, 2, 3, 4, or 5");
        break;
    }

    // Create a new switch statement using char instead of int
    // create a new char variable
    // create a switch statement testing for
    // A, B, C, D, or E
    // display a message if any of these are found and then break
    // Add a default which displays a message saying not found

    char charValue = 'A';

    switch (charValue) {
      case 'A':
      case 'B':
      case 'C':
      case 'D':
      case 'E':
        System.out.println("I found " + charValue);
        break;
      default:
        System.out.println(charValue + " wasn't found");
        break;
    }

    String month = "JaNuAry";
    switch (month.toLowerCase()) {
      case "january":
        System.out.println("Jan");
        break;
      case "february":
        System.out.println("Feb");
        break;
      default:
        System.out.println("Not found");
        break;
    }
  }
}