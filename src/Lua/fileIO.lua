-- File input / output in Lua

-- Read input from user in standard input
print("Enter output path: ")
path = io.read()

t = {}
-- Populate table t with all lower-case letters
for i = 97, 122 do
    t[#t + 1] = string.char(i)
end

-- Create a function to write content of table t
-- to a file at path
function writeToTextFile(path, t)
    local file = io.open(path, "w")
    for i = 1, #t do
        file:write(t[i] .. "\n")
    end
    file:close()
end

-- Create a function to read content of a file
-- to standard output at path
function readFromTextFile(path)
    idx = 1
    local file = io.open(path, "r")
    for line in file:lines() do
        print(line)
        idx = idx + 1
    end
    file:close()
    -- Print the number of lines of the file
    print("Number of lines: " .. idx)
end

writeToTextFile(path, t)
readFromTextFile(path)