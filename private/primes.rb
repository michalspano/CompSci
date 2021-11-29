# Ruby module - 'prime'
require 'prime'

# Create a function to return a list of primes until n
def find_primes_until_n(n)
    # Create an empty array to store primes
    primes = []
    # Loop through numbers from 2 to n and push primes to array
    for i in 2..n
        if Prime.prime?(i)
         primes << i
        end
    end
    # Return the array of primes
    return primes
end

# Call primes function with a desired range of values
range = 100
puts find_primes_until_n(range)