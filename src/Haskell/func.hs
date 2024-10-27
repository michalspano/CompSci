-- Test file in Haskell for custom functions and return values
-- Custom function to handle powers of natural numbers
pow :: Int -> Int -> Int
pow num1 num2 = num1 ^ num2

-- Custom function to trim a list and return type list int
cutList :: [Int] -> [Int]
cutList list = [head list, last list]

-- Connect str list of length 2 to str
convert :: [String] -> String
convert list = list !! 0 ++ list !! 1 

-- Declare the main function
main :: IO ()
main = do
    print (pow 2 5)
    print (cutList [1, 2, 3, 4])
    putStrLn (convert ["Mi", "ke"])
