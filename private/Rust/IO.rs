fn main() {
    // Load command line arguments to a vector
    let args: Vec<String> = std::env::args().collect();

    // Check proper usage
    if args.len() != 2 {
        println!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }

    // Read contents of input file and catch exceptions
    let contents = std::fs::read_to_string(&args[1])
        .expect("Something went wrong reading the file");
    // Print the contents
    println!("{}:\n{}", &args[1], contents);
}