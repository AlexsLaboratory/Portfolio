package com.company;

import java.util.ArrayList;
import java.util.Iterator;

public class Main {
  public static void main(String[] args) {

    ArrayList<Team> team = new ArrayList<>();

    team.add(new Team("Team 1", new int[]{0, 1, 2, 3, 4, 5}));
    team.add(new Team("Team 2", new int[]{10, 80, 10, 10, 10, 1}));
    team.add(new Team("Team 3", new int[]{0, 10, 0, 8, 20, 1}));

    Iterator <Team> i = team.iterator();
    while (i.hasNext()) {
      Team data = i.next();
      System.out.println(data.toOutput());
    }

    QuickSort qs = new QuickSort();
    qs.sort(team, 0, team.size() - 1, "desc");

    System.out.print("\n");
    System.out.println(team.get(0).getTeamName() + " has the highest average of " + team.get(0).getAverage());

  }
}
