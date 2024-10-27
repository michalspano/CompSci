-- Recursive modules in Haskell

-- Function to recursively call upon itself
loopedPrint :: Int -> IO ()
loopedPrint i = do
    if i <= 20
    then do 
        print i
        loopedPrint (i + 1)
    else putStrLn "Done."


-- Create a list of strings
listStr :: [String]
listStr = ["foo", "bar", "baz"]

printList :: Int -> IO ()
printList i = do
    let indexValue = listStr !! i
    if i <= 2
    then do 
        putStrLn (show (i + 1) ++ ". :" ++ indexValue)
        printList (i + 1)
    else putStrLn "Printed all elements.\n"

-- Recursive factorial function
factorial :: Int -> Int -> Int
factorial val sum = do
    if val >= 1
    then factorial (val - 1) (sum * val)
    else sum


-- Call factorial more times
loopedFactorial :: Int -> IO ()
loopedFactorial i = do
    if i >= 1
    then do 
        let result = factorial i 1
        putStrLn ("Factorial of '" ++ show (i) ++ "' is " ++ show (result))
        loopedFactorial (i - 1)
    else putStrLn "Done."


main :: IO ()
main = do

    -- Print each index until N
    putStrLn "Index print\n"
    loopedPrint 1

    -- Print out each element in a list
    putStrLn "List print\n"
    printList 0

    -- Compute nested factorial
    let range = 10
    loopedFactorial range
