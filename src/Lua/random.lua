-- Randomisation in Lua

-- Read user input
io.write("Enter the range of numbers: ")
local range = tonumber(io.read())

-- Check for nil value
if range == nil then
  return 
end

-- Function to verify the desired range
function verify_range(r, min, max)
  if r < min or r > max then
    return false
  end
  return true
end

-- Check if the range is valid
if not verify_range(range, 1, 100) then
  return
end

-- Populate the table with random values 
table = {}
math.randomseed(os.time())
for i = 1, range do
  table[i] = math.random(100)
end

-- Read the table
for j = 1, #table do
  io.write(table[j], " ")
end

print()
