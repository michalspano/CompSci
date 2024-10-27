/*
FIBONACCI SEQUENCE in C

Compilation:
~ $ gcc fib.c -o fib
~ $ clang fib.c -o fib

Run:
./fib $LIMIT_VAL
*/

#include <stdio.h>
#include <stdlib.h>

#define ERROR printf("Usage: ./fib $LIMIT_VAL\n");

// Define main function
int main(int argc, char* argv[]) {

	// Pass command-line arguments
	if (argc != 2) {
		ERROR;
		return 1;
	}

	int RANGE = atoi(argv[1]);

	// Initialise x,y,z type int
	int x, y, z;

	while (1) 
	{
		x = 0;
		y = 1;

		do 
		{
			// Out
			printf("%d\n", x);

			// Arithmetics
			z = x + y;
			x = y;
			y = z;

		} while (x < RANGE);
	}
}

