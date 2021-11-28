#include <stdio.h>
#include <stdlib.h>

#define LENGTH 26

// Create a structure to hold num. and char pair
typedef struct {
  int num_val;
  char char_val;
} letter;

// Crate a structure to hold all letters
typedef struct {
    letter letters_array[LENGTH];
} letters;

// Main function
int main(void) {
    // Crate new instance of letters
    letters alphabet;
    // Populate structure
    for (int i = 0; i < LENGTH; i++) {
        alphabet.letters_array[i].num_val = i + (int) 'a';
        alphabet.letters_array[i].char_val = i + 'a';
    }

    // Print the members of the structure
    for (int i = 0; i < LENGTH; i++) {
        printf("Num. value: %d; char. value: %c\n", 
        alphabet.letters_array[i].num_val, alphabet.letters_array[i].char_val);
    }

    // Add missing new line and return 0
    printf("\n");
    return 0;
}