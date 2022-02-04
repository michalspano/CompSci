fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

main :: IO ()
main = do
  putStr "Enter a number: "
  input <- getLine
  let n = read input :: Integer
  print (fib n)
