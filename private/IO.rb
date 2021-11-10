puts "Enter a path: "
PATH = gets.chomp

# Check if files does exist
if File.file?(PATH)
  puts File.read(PATH)
else
  puts "File not found."
end
