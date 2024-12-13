// 3.1 (Find future dates) Write a program that prompts the user to enter an integer for today’s 
// day of the week (Sunday is 0, Monday is 1, …, and Saturday is 6). Also prompt the user to 
// enter the number of days after today for a future day and display the future day of the week.

#include <stdio.h>

int main()
{
    int today, nextDay, futureDay;

    printf("Enter today's day: ");
    scanf("%d", &today);

    printf("Enter the number of days elasped since today: ");
    scanf("%d", &nextDay);

    // calculate the future day
    futureDay = (today + nextDay) % 7;

    // week days for 'today'
    printf("Today is ");
    switch (today) {
        case 0: printf("Sunday"); break;
        case 1: printf("Monday"); break;
        case 2: printf("Tuesday"); break;
        case 3: printf("Wednesday"); break;
        case 4: printf("Thursday"); break;
        case 5: printf("Friday"); break;
        case 6: printf("Saturday"); break;
        default: printf("Invalid day"); break;
    }

    // week days for 'futureday'
    printf(" and the future day is ");
    switch (futureDay) {
        case 0: printf("Sunday"); break;
        case 1: printf("Monday"); break;
        case 2: printf("Tuesday"); break;
        case 3: printf("Wednesday"); break;
        case 4: printf("Thursday"); break;
        case 5: printf("Friday"); break;
        case 6: printf("Saturday"); break;
        default: printf("Invalid day"); break;
    }

    printf("\n");

    return 0;
}