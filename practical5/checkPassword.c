#include <stdio.h>
#include <string.h>

void checkPassword(char password[])
{
	int length = strlen(password);	// Get the length of the password

	if (length >= 8)
	{
		int digit_count = 0;
		int upper_case = 0;
		int lower_case = 0;

		for (int i=0;i<length;i++)
		{
			if (password[i] >= 'a' && password[i] <= 'z') ++lower_case;
			if (password[i] >= 'A' && password[i] <= 'Z') ++upper_case;
			if (password[i] >= '0' && password[i] <= '9') ++digit_count;
		}
		
		if ((lower_case > 0 || upper_case > 0) && digit_count >= 2)
		{
			printf("Valid Password!");
		} else {
			printf("Invalid Password! Password must contain at least two digits.\n");
		}

	}

	else {
		printf("Invalid Password! Password must be at least 8 characters long.\n");
	}
}

int main()
{
	char password[16];

	printf("Enter Password (upto 15 characters): ");
	scanf("%15s", &password);

	checkPassword(password);

	return 0;
}