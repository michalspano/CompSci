// MATRIX EFFECT in JavaScript NodeJS

// Receive command-line arguments
var args = process.argv.slice(2);

// Check valid amount of command-line arguments - 1
if (args.length != 1) {
        process.exit(1);
}

// Transform to integers
var LINE_MAX = Number(args[0]);
var windowLimit = Number(process.stdout.columns);

// Check valid range 
if ((LINE_MAX) * 2.1 > windowLimit) {
        console.log('The window limit was exceeded.');
        process.exit(1);
}

// Array with binary options
const matrixArray = ['0', '1'];

// Array with console colors
const consoleColors = ["\x1b[32m", "\x1b[37m"]

// var item = items[Math.floor(Math.random()*items.length)];

// Create matrix function
function matrix() 
{
    // Loop forever (not the best option, for simplistic purposes only)
    while (true)
    {
        // Define an empty string container
        var matrixString = String();

        // Invoke a loop with a boundary of 'LINE_MAX'
        for (let j = 0; j < LINE_MAX; j++)
        {
            // Choose random element from the binary array
            var identifier = Math.floor(Math.random() * matrixArray.length);

            // Pick a random color
            var randomColor = consoleColors[Math.floor(Math.random() * consoleColors.length)];

            // Add it to the string separated by a space (with a randomly chosen color)
            matrixString += randomColor + identifier + ' ';
        }
        // Print out the final string repeatedly in the main while loop
        console.log(matrixString);
    }  
}

// Invoke the matrix function
matrix();


