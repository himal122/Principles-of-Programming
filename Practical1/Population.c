/* 1.1 (Population projection) The U.S. Census Bureau projects population based on the 
following assumptions: 
• One birth every 7 seconds 
• One death every 13 seconds 
• One new immigrant every 45 seconds 
Write a program to display the population for each of the next five years. Assume the 
current population is 312,032,486 and one year has 365 days. Hint: In Java, if two integers 
perform division, the result is an integer. The fractional part is truncated. For example, 5 / 4 
is 1 (not 1.25) and 10 / 4 is 2 (not 2.5). To get an accurate result with the fractional part, one 
of the values involved in the division must be a number with a decimal point. For example, 
5.0 / 4 is 1.25 and 10 / 4.0 is 2.5. */


#include <stdio.h>
#include <locale.h>

int main()
{
    // declairing variables
    double birthRate, deathRate, immigrantRate, secondsInYear;
    // use long long int to prevent overflow while dealing with large integers
    long long int currentPopulation = 312032486;

    // include locale to include commas in printf while printing numeric values
    setlocale(LC_NUMERIC, "");

    // convert year into seconds
    secondsInYear = 60 * 60 * 24 * 365;

    // calculate birth, death and immigrant rate in a year
    birthRate = secondsInYear / 7.0;
    deathRate = secondsInYear / 13.0;
    immigrantRate = secondsInYear / 45.0;

    // claculate each year's population for next five years
    printf("\nCurrent Population: %'d\n", currentPopulation);
    printf("\nPopulation in next 5 years\n");
    printf("-------------------------------\n");
    for (int i = 1; i <= 5; i++)
    {
        currentPopulation += (long long int)(birthRate - deathRate) + immigrantRate;
        //return population for next 5 years
        printf("Population in Year %d: %'lld\n", i, currentPopulation);
    }
    
    return 0;
}