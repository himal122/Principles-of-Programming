// *4.1 (Print distinct numbers) Write a program that reads in ten numbers and displays the 
// number of distinct numbers and the distinct numbers separated by exactly one space (i.e., if 
// a number appears multiple times, it is displayed only once). (Hint: Read a number and store 
// it to an array if it is new. If the number is already in the array, ignore it.) After the input, the 
// array contains the distinct numbers.


#include <stdio.h>

// Function to print distinct numbers
void distinct(int num[], int size) {
    int i, j;

    printf("Distinct Numbers: ");
    for (i = 0; i < size; i++) {
        int isDistinct = 1; // let the current element be distinct

        // Check if the current element has appeared before
        for (j = 0; j < i; j++) {
            if (num[i] == num[j]) {
                isDistinct = 0;
                break;
            }
        }

        // If it's distinct, print it
        if (isDistinct) {
            printf("%d ", num[i]);
        }
    }
    printf("\n");
}

int main() {
    int size;

    // Input the size of the array
    printf("Enter the size of Array: ");
    scanf("%d", &size);

    int num[size];

    // Input the array elements
    printf("Enter %d Elements: ", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &num[i]);
    }

    // Call the function to print distinct elements
    distinct(num, size);

    return 0;
}