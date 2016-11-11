-- second haskell file

main = do
    putStrLn "Hello, what's your name?"
    name <- getLine
    putStrLn $ "Hey "++name++", you rock!"