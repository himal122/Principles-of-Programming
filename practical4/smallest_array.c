// 4.2 (Find the smallest element) Write a program that finds the smallest element in an array 
// of double values. Test program that prompts the user to enter ten numbers, finds the 
// minimum value, and displays the minimum value.


#include <stdio.h>

int main(){

	int size;
	
	printf("Enter the size of the array: ");
	scanf("%d", &size);

	double num[size];

	printf("Enter Elements: ");
	for(int i=0;i<size;i++){
		scanf("%lf", &num[i]);
	}

	double smallest = num[0];

	for(int i=0;i<size;i++){

		if(num[i] < smallest){
			smallest = num[i];
		}
	}

	printf("Smallest: %.1f", smallest);

	return 0;
}