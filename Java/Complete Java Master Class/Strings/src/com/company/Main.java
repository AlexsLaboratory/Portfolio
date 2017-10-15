package com.company;

public class Main {
  public static void main(String[] args) {
    // byte
    // short
    // int
    // long
    // float
    // double
    // char
    // boolean

    String myString = "This is my string";
    System.out.println(myString);
    myString += ", and this is more.";
    System.out.println(myString);
    myString += " \u00A9 2017";
    System.out.println(myString);

    String numberString = "250.55";
    numberString += "50.55";
    System.out.println(numberString);

    String lastString = "10";
    int myInt = 50;
    lastString += myInt;
    System.out.println(lastString);
    double doubleNumber = 120.47;
    lastString += doubleNumber;
    System.out.println(lastString);
  }
}
