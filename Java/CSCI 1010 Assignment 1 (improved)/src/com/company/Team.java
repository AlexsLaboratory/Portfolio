package com.company;

import jdk.jfr.Percentage;
import org.jetbrains.annotations.NotNull;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Team {
  private String teamName;

  private List<Integer> dataPoints;
  private int total;
  private double average;

  public Team(String teamName, int[] dataPoints) {
    this.teamName = teamName;
    List<Integer> list = new ArrayList<>();
    for (int i : dataPoints) {
      list.add(i);
    }
    this.dataPoints = list;
    setTotal(getDataPoints());
    this.average = (double) getTotal()/list.size();
  }

  public String getTeamName() {
    return this.teamName;
  }

  public List<Integer> getDataPoints() {
    return this.dataPoints;
  }

  public String dataPointsToString() {
    String output = "";
    int tracker = 0;
    int dataLength = getDataPoints().size();
    Iterator <Integer> i = getDataPoints().iterator();
    while (i.hasNext()) {
      if (dataLength - 1 != tracker) {
        output = output.concat(i.next() + ", ");
      } else {
        output = output.concat(i.next() + "");
      }
      ++tracker;
    }
    return output;
  }

  private void setTotal(List<Integer> list) {
    int sum = 0;
    for (int i : list) {
      sum += i;
    }
    this.total = (int) sum;
  }

  public int getTotal() {
    return this.total;
  }

  public double getAverage() {
    return this.average;
  }

  public String toOutput() {
    return "Team name = " + this.teamName + ", Stats = " + dataPointsToString() + ", Total = " + this.total + ", Average = " + this.average;
  }
}
