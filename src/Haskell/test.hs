-- Using haskell-stack
-- `# stack ghci --package random`
import System.Random(randomRIO)

-- Define main function
main :: IO ()
main = do
    -- Define range of numbers
    let min = 1
    let max = 10

    -- Generate a random number between min and max
    randomNumber <- randomRIO (min, max)

    -- Ask user to guess the number between min and max
    -- Concatenate the string with the min and max values
    putStrLn $ "Guess a number between " ++ show min ++ " and " ++ show max

    -- Read user input
    userGuess <- getLine

    -- Convert user input to integer
    let userGuessInt = read userGuess :: Int

    -- Check if user input is correct
    if userGuessInt == randomNumber
    -- If correct, print "You got it!"
    then putStrLn "You got it!"
    -- If incorrect, print "Try again"
    else putStrLn "Better luck next time!"

    -- Run main function again (recursion)
    main
