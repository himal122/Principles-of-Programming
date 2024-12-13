// 3.2 (Find the number of days in a month) Write a program that prompts the user to enter the 
// month and year and displays the number of days in the month. For example, if the user 
// entered month 2 and year 2012, the program should display that February 2012 had 29 days. 
// If the user entered month 3 and year 2015, the program should display that March 2015 had 
// 31 days.

#include <stdio.h>

int main() {
    int month, year, days;

    printf("Enter month (1-12): ");
    scanf("%d", &month);
    printf("Enter year: ");
    scanf("%d", &year);

    // get the number of days in month
    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            days = 31;
            break;
        case 4: case 6: case 9: case 11:
            days = 30;
            break;
        case 2:
            // Check if the year is leap year
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                days = 29;
            } else {
                days = 28;
            }
            break;
        default:
            printf("Invalid month!\n");
            break;
    }

    printf("Month %d of year %d has %d days.\n", month, year, days);

    return 0;
}
