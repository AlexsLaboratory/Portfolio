package com.company;

public class Main {

    public static void main(String[] args) {
        // width of int = 32 (4 bytes)
	    int myIntValue = 5 / 3;
	    // width of float = 32 (4 bytes)
	    float myFloatValue = 5f / 3f;
	    // width of double = 64 (8 bytes)
	    double myDoubleValue = 5d / 3f;

        System.out.println("myIntValue " + myIntValue);
        System.out.println("myFloatValue " + myFloatValue);
        System.out.println("myDoubleValue " + myDoubleValue);

        // Convert a given number of pounds to kilograms
        // 1. Create a variable to store the number of pounds
        // 2. Calculate the number of Kilograms for the number above and store in a variable
        // 3. Print out the result

        double numPounds = 200d;
        double numKilograms = numPounds * 0.453592d;
        System.out.println("Kilograms: " + numKilograms);
    }
}
