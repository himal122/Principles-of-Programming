#include <stdio.h>

int main() {
    int number, largest = 0, count = 0;

    printf("Enter Elements (end with 0): ");

    while (1) {
        scanf("%d", &number);

        if (number == 0) {
            break;
        }

        // get the largest and increase the counter
        if (number > largest) {
            largest = number;
            count = 1;
        } else if (number == largest) {
            count++;
        }
    }

    printf("The largest number is %d\n", largest);
    printf("The occurrence count of the largest number is %d\n", count);

    return 0;
}