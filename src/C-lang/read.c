#include <stdio.h>

// Constant number of valid command-line arguments
#define LENGTH 2

// Create the main function
int main(int argc, char *argv[]) {
    // Get the path to the file
    if (argc != 2) {
        printf("Usage: ./read <file_path>\n");
        return 1;
    }

    // Define path from command-line
    char* path = argv[1];

    // Open file at path
    FILE *file = fopen(path, "r");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    // Print each character in the file
    char c;
    while ((c = fgetc(file)) != EOF) {
        printf("%c", c);
    }
    printf("\n");
}