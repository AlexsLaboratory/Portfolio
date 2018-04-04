package com.company;

public class Main {

  public static void main(String[] args) {
    // Create a new class for a bank account
    // Create fields for the account number, balance, customer name, email, and phone number.
    //
    // Create getters and setters for each field
    // Create two additional methods
    // 1. To allow the customer to deposit funds (this should increment the balance field).
    // 2. To allow the customer to withdraw funds. This should deduct from the balance field,
    // but not allow the withdrawal to complete if there are insufficient funds.
    // You want to create various code in the Main class (the one created by IntelliJ) to
    // confirm you code is working.
    // Add some System.out.println's in the two methods above as well.

    Account bobsAccount = new Account(12345, 0, "Bob Brown", "myemail@bob.com", "(704) 123-1234");
    System.out.println(bobsAccount.getNumber());
    System.out.println(bobsAccount.getBalance());
    bobsAccount.withdrawal(100);

    bobsAccount.deposit(50);
    bobsAccount.withdrawal(100);

    bobsAccount.deposit(51);
    bobsAccount.withdrawal(100);

    Account alexsAccount = new Account("Alex", "alex@email.com", "(704) 123-1234");
    System.out.println(alexsAccount.getNumber() + " name " + alexsAccount.getCustomerName());

    // Create a new class VipCustomer
    // it should have 3 fields name, credit limit, and email address.
    // create 3 constructors
    // 1st constructor empty should call the constructor with 3 parameters with default values
    // 2nd constructor should pass on the 2 values it receives and and a default value for 3rd
    // 3rd constructor should save all fields.
    // create getters only for this using the code generation of IntelliJ as setters won't be needed
    // test and confirm that it works.

    System.out.println("\n");


    VipCustomer person1 = new VipCustomer();
    System.out.println(person1.getName());

    VipCustomer person2 = new VipCustomer("Bob", (double) 25000);
    System.out.println(person2.getName());

    VipCustomer person3 = new VipCustomer("Alex", (double) 100, "alex@email.com");
    System.out.println(person3.getName());
  }
}
