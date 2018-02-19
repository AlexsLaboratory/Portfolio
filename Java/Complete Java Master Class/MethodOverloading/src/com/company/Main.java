package com.company;

public class Main {

  public static void main(String[] args) {
    int newScore = calculateScore("Alex", 500);
    System.out.println("New Score is " + newScore);
    calculateScore(75);
    calculateScore();
    caldFeetAndInchesToCentimeters(6,6);
    caldFeetAndInchesToCentimeters(158);
  }

  public static int calculateScore(String playersName, int score) {
    System.out.println("Player " + playersName + " scored " + score + " points");
    return score * 1000;
  }

  public static int calculateScore(int score) {
    System.out.println("Unnamed Player scored " + score + " points");
    return score * 1000;
  }

  public static void calculateScore() {
    System.out.println("No player name, no player score");
  }

  // Create a method called caldFeetAndInchesToCentimeters
  // It needs to have two parameters
  // feet is the first parameter, inches is the 2nd parameter
  //
  // You should validate that the first parameter, feet, is >= 0
  // You should validate that the 2nd parameter, inches, is >= 0 and <=12
  // return -1 from the method if either of the above is not true
  //
  // If the parameters are valid, the calculate how many centimeters
  // comprise the feed and inches passes to this method and return
  // that value
  //
  // Create a 2nd method of the same name but with only one parameter
  // inches is the parameter
  // validate that its >= 0
  // return -1 if it is not true
  // But if its valid, then calculate how many feet are in the inches
  // and then here is the tricky part
  // call the other overloaded method passing the correct feet and inches
  // calculated so that if can calculate correctly
  // hints: Use double for your number data types is probably a good idea
  // 1 inch = 2.54cm and one foot = 12 inches
  // use the link I give you to confirm your code is calculating correctly
  // Calling another overloaded method just requires you to use the
  // right number of parameters

  public static double caldFeetAndInchesToCentimeters(double feet, double inches) {
    if (feet >= 0 || inches >= 0 || inches <= 12) {
      double centimeters = ((feet * 12) * 2.54) + (inches * 2.54);
      System.out.println(feet + " feet, " + inches + " inches = " + centimeters + " cm");
      return centimeters;
    } else {
      return -1;
    }
  }

  public static double caldFeetAndInchesToCentimeters(double inches) {
    if (inches >= 0) {
      double feet = (int) inches / 12;
      double remainingInches = (int) inches % 12;
      System.out.println(inches + " inches is equal to " + feet + " feet and " + remainingInches + " inches");
      return caldFeetAndInchesToCentimeters(feet, remainingInches);
    } else {
      return -1;
    }
  }
}