#include <stdio.h>

int main() {

	char str[100];
	int vowels = 0, consonents = 0; // counters


	printf("Enter a Sentence: ");
	fgets(str, sizeof(str), stdin); // read input string sentance

    // loop through all characters in strings
	for(int i=0; str[i] != '\0'; i++){

		char ch = str[i]; // get current character

		if((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')){

			if((ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
			|| (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')){

				vowels++;
			}

			else {
				consonents++;
			}
		}
	}

	printf("Original Sentence: %s", str);
	printf("The number of vowels is %d", vowels);
	printf("\nThe number of consonents is %d", consonents);
	

	return 0;

}