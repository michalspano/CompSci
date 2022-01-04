// Create the main function
fn main() {
    // Display the factorials of the numbers 1 through 15
    let mut i = 1;
    while i <= 15 {
        println!("{}! = {}", i, factorial(i));
        i = i + 1;
    }
}

// Recursive factorial function
fn factorial(n: u64) -> u64 {
    // Base case
    if n == 1 {
        1
    } else {
        // Recursive case
        n * factorial(n - 1)
    }
}