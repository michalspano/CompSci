// Create a function to return an array with all primes up to a given number.
// Include type annotations.
function getPrimes(num) {
    var primes = [];
    for (var i = 2; i <= num; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}
// Create a function to return true if a number is prime.
// Include type annotations.
function isPrime(num) {
    for (var i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}
// Call the function to get the primes
var primes = getPrimes(20);
console.log(primes);
