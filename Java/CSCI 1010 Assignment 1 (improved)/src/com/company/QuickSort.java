package com.company;
import java.util.ArrayList;

public class QuickSort {
  private int partition(ArrayList<Team> teams, int low, int high, String order) {
    double pivot = teams.get(high).getAverage();
    int i = low - 1;
    for (int j = 0; j <= high - 1; j++) {
      if (order.equalsIgnoreCase("asc")) {
        if (teams.get(j).getAverage() < pivot) {
          i++;

          Team temp = teams.get(i);
          teams.set(i, teams.get(j));
          teams.set(j, temp);
        }
      } else if (order.equalsIgnoreCase("desc")) {
        if (teams.get(j).getAverage() > pivot) {
          i++;

          Team temp = teams.get(i);
          teams.set(i, teams.get(j));
          teams.set(j, temp);
        }
      }
    }

    Team temp = teams.get(i + 1);
    teams.set(i + 1, teams.get(high));
    teams.set(high, temp);
    return i + 1;
  }

  void sort(ArrayList<Team> teams, int low, int high, String order) {
    if (low < high) {
      int pi = partition(teams, low, high, order);

      sort(teams, low, pi-1, order);
      sort(teams, pi+1, high, order);
    }
  }
}
