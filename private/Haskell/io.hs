{-
*** Reading Contents of Files in Haskell ***
$ ghci io.hs
$ *Main> :main [<file>]
-}

-- Global import(s)
import System.Directory.Internal.Prelude (getArgs)

-- Create the main function
main :: IO ()
main = do
    -- Get the arguments
    args <- getArgs

    -- Check if a filename was provided
    case args of
        -- If no file name was supplied, print an error message and exit
        [] -> putStrLn "Please supply a file name"

        -- Otherwise, proceed to check the contents of the file
        (fileName:_) -> do
            contents <- readFile fileName -- Load contents
            putStr contents -- Display contents
