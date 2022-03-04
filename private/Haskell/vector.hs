-- Calculate the length (norm) of a 2D vector

main :: IO ()
main = do
  putStrLn "Calculate the length of a vector v[n,m]"

  -- User input
  putStr "Let n = "
  n <- getLine
  putStr "Let m = "
  m <- getLine
  
  -- Parse to double
  let n' = read n :: Double
      m' = read m :: Double

  -- Display result
  putStrLn $ "||v|| = " ++ show (calcLength n' m')

calcLength :: Double -> Double -> Double
calcLength n m = sqrt (n^2 + m^2)
