/* Suppose you save $100 each month into a savings account with the annual interest rate 5%. 
Thus, the monthly interest rate is 0.05/12 = 0.00417. After the first month, the value in the 
account becomes 
100 * (1 + 0.00417) = 100.417 
After the second month, the value in the account becomes 
(100 + 100.417) * (1 + 0.00417) = 201.252 
After the third month, the value in the account becomes 
(100 + 201.252) * (1 + 0.00417) = 302.507 
and so on. 
Write a program that prompts the user to enter a monthly saving amount and displays the 
account value after the sixth month. (You will use a loop to simplify the code and display 
the account value for any month in your practical session in Week 4.)  */


#include <stdio.h>

int main()
{
    // Declaring variables
    double monthlySavingAmount = 0.0, accountValue = 0.0;
    const double monthlyInterestRate = 0.05 / 12;

    // read monthly saving amount
    printf("Enter monthly saving amount: ");
    scanf("%lf", &monthlySavingAmount);

    // Calculate account value after six months
    for (int i = 1; i <= 6; i++)
    {
        accountValue = (accountValue + monthlySavingAmount) * (1 + monthlyInterestRate);
    }

    // Display account value after sixth month
    printf("After the sixth month, the account value is $%.2lf\n", accountValue);

    return 0;
}
