// Include libraries
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  
  // Check usage
  if (argc != 2) {
    printf("Usage: %s <number>\n", argv[0]);
    return 1; 
  }
  
  // Parse the input to an int 
  int n = atoi(argv[1]);
  
  // Check if the number is negative
  if (n < 0) {
    printf("%d is negative\n", n);
    return 1;
  }

  // Create an array of ints 
  int *primes = malloc(n * sizeof(int));
  int i = 0;
  
  // Loop until n and find all primes
  for (int j = 2; j <= n; j++) {
    int isPrime = 1;

    // Detect a prime number 
    for (int k = 0; k < i; k++) {
      if (j % primes[k] == 0) {
        isPrime = 0;
        break;
      }
    }
    // Append number if prime
    if (isPrime) {
      primes[i++] = j;
    }
  }
 
  // Print all results
  for (int k = 0; k < i; k++) {  
    printf("%i. %d\n", k + 1, primes[k]);
  }

  // Free the memory
  free(primes);
  return 0;
}
