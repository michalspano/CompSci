-- Main function
main :: IO ()

main = do
    -- Read IO
    putStr "Max range of numbers: "
    input <- getLine

    putStr "Divisor: "
    div <- getLine

    -- Type conversion
    let number = read input :: Int
    let divisor = read div :: Int

    -- Print the result of the function
    print (findNum number divisor)

-- Find all numbers divisible by n until number m
findNum :: Int -> Int -> [Int]
findNum m n = [x | x <- [1..m], x `mod` n == 0]

