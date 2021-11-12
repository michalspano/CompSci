// Read content of a file
// Usage: node readFile.js <file>

// Define a class with a constructor and a method
class IO {
    constructor(path) {
        this.path = path;
    }
    // Create a method to read a file
    readFile() {    
        var fs = require('fs');
        fs.readFile(this.path, 'utf8', function(err, data) {
            if (err) throw err;
            console.log(data);
            });
        }
    // Create a method to check if a file exits, return true or false
    fileExists() {
        var fs = require('fs');
        try {
            fs.statSync(this.path);
            return true;
        } catch(err) {
            return false;
        }
    }
}

// Create a function to return the number of command line arguments
function getNumberOfArguments() {
    return process.argv.length;
}

// Check if number of arguments is correct
if (getNumberOfArguments() < 3) {
    console.log("Usage: node readFile.js <file>");
    process.exit(1);
}

// Assign file name to variable
var PATH = process.argv[2];

// Check if file exists
if (!new IO(PATH).fileExists()) {
    console.log("File does not exist");
    process.exit(1);
}

// Create an instance of the class
var io = new IO(PATH);
io.readFile();

