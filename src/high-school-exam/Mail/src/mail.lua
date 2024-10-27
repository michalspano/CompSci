--[[
    Database reader in Lua
    11/09/2021
    Michal Spano
]]

-- Declare an input database
inputFile = io.open("in/data_set.csv", "r")

-- Declare an output file
outputFile = io.open("dist/output.txt", "w")

-- Declare a function to create valid mail addresses
function MailFormat(currentLine)

    -- Detect the index of the default separator
    s = string.find(currentLine, ';')

    -- Create substrings
    name = string.sub(currentLine, 0, s - 1)
    surname = string.sub(currentLine, s + 1, #currentLine - 1) -- Omit '\n'

    -- Return valid form of mail address (in lower case)
    return string.lower(name .. '.' .. surname .. '@gmail.com')
end

i = 0

-- Iterate over all lines in the database
for line in inputFile:lines() do

    -- Skip header
    if i >= 1 then

        -- Receive mail and write to to the specified output
        data = MailFormat(line)
        outputFile:write(data, '\n')
    end
    i = i + 1
end

-- Close IOs
inputFile:close()
outputFile:close()
