// Include libraries
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Include local header with macros and functionality
#include "mail.h"


// Using command-line arguments to parse input
int main(int argc, char *argv[])
{
    // Check for number of command-line arguments (expected 3)
    if (argc != 3)
    {
        fprintf(stderr, ERROR);
        return 1;
    }

    // Open a text files as a file pointer of type 'FILE'
    FILE *inputTextFile = fopen(argv[1], "r");
    FILE *outputTextFile = fopen(argv[2], "w");

    // Check for any errors
    if (inputTextFile == NULL)
    {
        return fileError(argv[1]);
    }

    if (outputTextFile == NULL)
    {
        return fileError(argv[2]);
    }

    // Declare a buffer of type char (read single char at once)
    char buffer;

    // Declare a temp string
    char temp[200];

    // Read char by char from a text file 'fgetc'
    int i = 0;
    while ((buffer = fgetc(inputTextFile)) != EOF)
    {
        // Assign individual chars to a temp string
        temp[i] = buffer;
        i++;
    }

    /* 
    Each string is denoted by '\n' at the end of each line
    */

    // Iterate over all chars in the temp. string    
    for (int i = 0, n = strlen(temp); i < n; i++)
    {
        // Transform all chars to lower-case
        char chr = tolower(temp[i]);

        // Replace ';' with '.' -> proper mail structure
        if (chr == ';') {chr = '.';}

        // Detect '\n' in the following index and asssign respective domain from macros
        if (temp[i+1] == '\n')
        {
            // Write to a text 
            writeDomain(outputTextFile);
        }

        // Otherwise print out remaining chars
        else
        {
            // Write to a text file
            fputc(chr, outputTextFile);
        }
    }

    // Print out domain for the last row (once EOF is met) -> break
    writeDomain(outputTextFile);

    // Close text file
    fclose(inputTextFile);
    fclose(outputTextFile);

    // Return 0 after successful completion
    return 0;
}
