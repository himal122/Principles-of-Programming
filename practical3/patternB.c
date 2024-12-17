#include <stdio.h>

int main()
{
    int i, j;

    for (i = 6; i >= 1; i--)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%2d", j); // %2d for space
        }

        printf("\n");
    }

    return 0;
}