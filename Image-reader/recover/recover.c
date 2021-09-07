#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

// Create a struct of a BYTE or 8 bits
typedef uint8_t BYTE;

// Define a constant unit size of 512 B
#define UNIT_SIZE 512

// Define const header format for first 3 bytes
const BYTE header[3] = {0xff, 0xd8, 0xff};

// Function prototype(s)
bool isHeader(BYTE buffer[UNIT_SIZE]);
void writeBlock(BYTE buffer[UNIT_SIZE], FILE *output);
bool invalidInputFile(char *fileName);

// Recover JPEG Files
int main(int argc, char *argv[])
{
    // Accept only 1 command line
    if (argc != 2)
    {
        // Prompt the user with an error
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Load the card file
    char *inputFile = argv[1];
    FILE *memoryCard = fopen(inputFile, "r");

    // Handle possible file erros
    if (memoryCard == NULL)
    {
        invalidInputFile(inputFile);
    }

    // Create a counter (to determine how many JPEG files were created), default set to -1
    int counter = -1;

    // Create a buffer of size 512B
    BYTE buffer[UNIT_SIZE];

    // Container for output file name
    char FILENAME[8]; // ###.jpg\0

    // Instance of type FILE for JPG output files, default set to 'NULL'
    FILE *output = NULL;

    while (fread(buffer, sizeof(UNIT_SIZE), 1, memoryCard))
    {
        // Header was detected
        if (isHeader(buffer))
        {
            // Increment the counter
            counter++;

            // Create a name file name with the updated counter int variable
            sprintf(FILENAME, "%03i.jpg", counter);

            // Create the output file
            if (output == NULL)
            {
                // No output file detected
                output = fopen(FILENAME, "w");

                // Handle possible file errors
                if (output == NULL)
                {
                    return invalidInputFile(FILENAME);
                }

                // Write the header to the JPG file
                writeBlock(buffer, output);
            }
            else
            {
                // An existing file was already detected
                fclose(output);

                // Create a new one
                output = fopen(FILENAME, "w");

                // Handle possible file errors
                if (output == NULL)
                {
                    // Handle faulty file
                    return invalidInputFile(FILENAME);
                }

                // Write the header to the JPG file
                writeBlock(buffer, output);
            }
        }
        else
        {
            if (output != NULL)
            {
                // Write to that text file
                writeBlock(buffer, output);
            }
        }
    }

    // Close file(s)
    fclose(memoryCard);
    fclose(output);
    return 0;
}

// Check for valid headers
bool isHeader(BYTE buffer[UNIT_SIZE])
{
    // Create a counter for valid header
    int validHeaderCount = 0; // => int: 3 (i.e., sizeof(header));

    // Check for the first 3 bytes from the header
    for (int i = 0; i <= 2; i++)
    {
        // Check for every i-th element from the pre-defined arr
        if (buffer[i] == header[i])
        {
            // Increment the counter
            validHeaderCount++;
        }

        // Proceed if the number of valid header matches
        if (validHeaderCount == sizeof(header))
        {
            // The first 3 bytes from the header are correct
            /*
            Determine the validity of the 4th byte!
            Using Bit-wise arithmetic, checking for the beginning of the first 4 bites from the byte
            */
            if ((buffer[3] & 0xf0) == 0xe0)
            {
                // Return true if valid header was found
                return true;
            }
        }
    }
    // Return false if no valid header was found
    return false;
}

void writeBlock(BYTE buffer[UNIT_SIZE], FILE *output)
{
    // Write using 'fwrite()'
    fwrite(buffer, sizeof(UNIT_SIZE), 1, output);
}

// Function to handle invalid inputs
bool invalidInputFile(char *fileName)
{
    // Indicate error, return non-zero int variable
    fprintf(stderr, "Could not open %s\n", fileName);
    return 1;
}