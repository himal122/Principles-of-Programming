/* 1.2 (Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree in a double 
value from the console, then converts it to Fahrenheit and displays the result. The formula 
for the conversion is as follows: fahrenheit = (9 / 5) * celsius + 32. 
Hint: In Java, 9 / 5 is 1, but 9.0 / 5 is 1.8. */

#include <stdio.h>

int main()
{
    // variables declarations
    double celciusDegree = 0, fahrenheitDegree = 0;

    // read celsius degree
    printf("Enter a degree in Celsius: ");
    if (scanf("%lf", &celciusDegree) != 1) 
    {
        printf("Invalid input. Enter numeric value.\n");
        return 1;
    }

    // calculate fahrenheit
    fahrenheitDegree = (9.0/5) * celciusDegree + 32;

    // display converted degree
    printf("%.1lf degree Celcius is %.1lf Fahrenheit", celciusDegree, fahrenheitDegree);


    return 0;
}