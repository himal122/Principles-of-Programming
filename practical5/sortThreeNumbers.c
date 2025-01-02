#include <stdio.h>

int DisplaySortedNumbers(double num1, double num2, double num3)
{

	double temp;

	if (num1 > num2)
	{
		temp = num1;
		num1 = num2;
		num2 = temp;
	}

	if (num2 > num3)
	{
		temp = num2;
		num2 = num3;
		num3 = temp;
	}

	if (num1 > num2)
	{
		temp = num1;
		num1 = num2;
		num2 = temp;
	}

	printf("\nSorted Numbers: %.2f %.2f %.2f", num1, num2, num3);

}

int main()
{
	double num1;
	double num2;
	double num3;
	
	printf("Enter 3 numbers: ");
	scanf("%lf%lf%lf", &num1, &num2, &num3);

	printf("\nOriginal Numbers: %.2f %.2f %.2f", num1, num2, num3);

	DisplaySortedNumbers(num1, num2, num3);


	return 0;
}
