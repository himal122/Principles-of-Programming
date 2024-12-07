/* Customer statistics
Practical 3, Part x
@author Himal Acharya */
                                                                 
#include<stdio.h>
FILE *fp; // define a file pointer for the file

int main()
{
    /* code */
    // open the file and assign its address to file pointer
    fp = fopen("testInput.txt", "r");

    //define variables for number of customers, customer number, previous metre, current metre
    int noCustomers, customerNo, previous, current;
    
    //define and initiate variables for numbers of heavy users, regular users, light users
    int heavyUsers = 0, regularUsers = 0, lightUsers = 0;

    //read number of customers
    printf("Reading number of customers:\n ");
    fscanf(fp, "%d", &noCustomers);

    //loop begins
    for (int i = 1; i <= noCustomers; i++) {

        //read a set of values from input file
        printf("Reading customer number, previous metre and current metre:\n ");

        //read customer number, previous metre and current metre 
        fscanf(fp, "%d %d %d", &customerNo, &previous, &current);

        //display customer number, previous metre and current metre
        printf("The customer number, previous metre and current metre from file: ");
        printf("%d %d %d\n", customerNo, previous, current);
      
        //Classify a user and update statistics
        if (current - previous >= 1000)
           heavyUsers++; // if  >= 1000, heavy users increase by 1
        else if (current - previous >= 500) 
          regularUsers++; // else if >= 500 (already < 1000), regular users increase by 1
        else if (current - previous < 500) 
           lightUsers++; // else if < 500, light users increase by 1
        else
          printf("Metre reading error"); //  else error
    }
    //loop ends

    fclose (fp); // always close files you've opened 

    // Display customer statistics
        printf("Heavy users: %d\n", heavyUsers);
        printf("Regular users: %d\n", regularUsers);
        printf("Light users: %d\n", lightUsers);

    return 0;
} 