if #arg ~= 1 then
    -- Ensure proper usage
    print("Usage: fib.lua <n>")
    os.exit(1)
end

-- Parse range
local n = tonumber(arg[1])

if n <= 1 then
    print("The range must be greater than 1.")
    os.exit(1)
end

local a, b = 0, 1
while b <= n do
    print(b)
    a, b = b, a + b
end
os.exit(0)