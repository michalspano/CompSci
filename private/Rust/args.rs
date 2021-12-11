// Create the main function for the program.
fn main() {
    // Append command-line arguments to the vector of type std::string
    let args: Vec<String> = std::env::args().collect();

    // Print the number of command line-arguments
    println!("Number of command-line arguments: {}", 
    args.len() - 1);

    // Print all command-line arguments
    // Skip the first argument
    for i in 1..args.len() {
        println!("Argument: {}", args[i]);
    }
}