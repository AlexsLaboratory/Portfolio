package com.company;

public class Account {
  private Number number;
  private double balance;
  private String customerName;
  private String customerEmailAddress;
  private String customerPhoneNumber;

  public Account() {
    this(1234, 2.50, "Default name", "Default address", "Default phone");
  }

  public Account(Number number, double balance, String customerName, String customerEmailAddress, String customerPhoneNumber) {
    this.number = number;
    this.balance = balance;
    this.customerName = customerName;
    this.customerEmailAddress = customerEmailAddress;
    this.customerPhoneNumber = customerPhoneNumber;
  }

  public Account(String customerName, String customerEmailAddress, String customerPhoneNumber) {
    this(12345, 100.45, customerName, customerEmailAddress, customerPhoneNumber);
  }

  public void deposit(double depositAmount) {
    this.balance += depositAmount;
    System.out.println("Deposit of " + depositAmount + " made. New balance is " + this.balance);
  }

  public void withdrawal(double withdrawalAmount) {
    if (this.balance - withdrawalAmount < 0) {
      System.out.println("Only " + balance + " available. Withdrawal not processed");
    } else {
      this.balance -= withdrawalAmount;
      System.out.println("Withdrawal of " + withdrawalAmount + " processed. Remaining balance = " + this.balance);
    }
  }

  public Number getNumber() {
    return number;
  }

  public double getBalance() {
    return balance;
  }

  public String getCustomerName() {
    return customerName;
  }

  public String getCustomerEmailAddress() {
    return customerEmailAddress;
  }

  public String getCustomerPhoneNumber() {
    return customerPhoneNumber;
  }
}
