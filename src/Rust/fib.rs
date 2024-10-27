fn main() {
    // Var dump
    let args: Vec<String> = std::env::args().collect();
    let file: String = args[0].clone();

    // Check usage
    // Usage: ./file <n: int>
    if args.len() != 2 {
        println!("Usage: {} <n: int>", file);
        return;
    }

    // Convert the argument to an integer
    // Handle parse error
    let n: u64 = match args[1].parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Usage: {} <n: int>", file);
            return;
        }
    };

    // Print all fibonacci numbers less then n
    let mut a = 0;
    let mut b = 1;
    while b <= n {
        println!("{}", b);
        let c = a + b;
        a = b;
        b = c;
    }
}