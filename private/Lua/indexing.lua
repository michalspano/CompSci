function populateTable(isUpperCase)
    t = {}

    if isUpperCase then
        shift = 65
    else
        shift = 97
    end

    for k = 0, 25 do
        t[k] = string.char(k + shift)
    end

    return t
end

-- Colors
GREEN = "\27[32m"
RESET = "\27[0m"

local indent = 1
table = populateTable(false)

for i = 0, #table do
    io.write(GREEN, '|', RESET) -- Start pipe
    for _ = 1, i do
        for _ = 1, indent do
            io.write('-') -- Linear indent
        end
    end
    io.write(GREEN, table[i], '\n', RESET)
end
io.write('\n')