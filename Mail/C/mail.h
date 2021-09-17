// Mail header file

// Macros
#define DOMAIN "gmail.com"
#define ERROR "Usage: ./mail $INPUT_PATH $OUTPUT_PATH\n"

// Include function prototypes
int fileError(char *PATH);
void writeDomain(FILE *ip);

// Create a function to output an error at a given path
int fileError(char *PATH)
{
    fprintf(stderr, "%s not available.\n", PATH);
    return 1;
}

// Create a function to assign each domain
void writeDomain(FILE *ip)
{
    // Write to a text
    fputc('@', ip);
    fputs(DOMAIN, ip);
}