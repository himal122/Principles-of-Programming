// *4.3 (Sum elements column by column) Write a program that returns the sum of all the 
// elements in a specified column in a matrix. 

#include <stdio.h>

void columns_addition(double num[][4], int rows, int cols) {
    int i, j;

    for (j = 0; j < cols; j++) {
        double col_sum = 0.0;  // Sum variable for each column
        for (i = 0; i < rows; i++) {
            col_sum += num[i][j];
        }
        printf("Sum of the elements at column %d is %.1f\n", j + 1, col_sum);
    }
}

int main() {
    int rows = 3, cols = 4;
    double num[3][4];

    printf("Enter elements of the matrix (%dx%d):\n", rows, cols);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%lf", &num[i][j]);
        }
    }

    printf("\n");
    columns_addition(num, rows, cols);

    return 0;
}