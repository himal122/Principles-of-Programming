//  (Compute the weekly hours for each employee) Suppose the weekly hours for all
// employees are stored in a two-dimensional array. Each row records an employee’s sevenday work hours with seven columns. For example, the following array stores the work hours 
// for eight employees. Write a program that displays employees and their total hours in 
// decreasing order of the total hours.


#include <stdio.h>

int main() {
    int workHours[8][7] = {
        {2, 4, 3, 4, 5, 8, 8},
        {7, 3, 4, 3, 3, 4, 4},
        {3, 3, 4, 3, 3, 2, 2},
        {9, 3, 4, 7, 3, 4, 1},
        {3, 5, 4, 3, 6, 3, 8},
        {3, 4, 4, 6, 3, 4, 4},
        {3, 7, 4, 8, 3, 8, 4},
        {6, 3, 5, 9, 2, 7, 9}
    };

    int totalHours[8];
    int employeeIndexes[8];

    // Calculate total hours for each employee
    for (int i = 0; i < 8; i++) {
        totalHours[i] = 0;
        for (int j = 0; j < 7; j++) {
            totalHours[i] += workHours[i][j];
        }
        employeeIndexes[i] = i; // Store employee index
    }

    // Sort employees by total hours in descending order
    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 8; j++) {
            if (totalHours[employeeIndexes[i]] < totalHours[employeeIndexes[j]]) {
                // Swap indexes
                int temp = employeeIndexes[i];
                employeeIndexes[i] = employeeIndexes[j];
                employeeIndexes[j] = temp;
            }
        }
    }

    for (int i = 0; i < 8; i++) {
        printf("Employee %d\t%d\n", employeeIndexes[i], totalHours[employeeIndexes[i]]);
    }

    return 0;
}
