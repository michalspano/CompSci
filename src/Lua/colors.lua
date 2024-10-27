-- Function to display a message with all colors with a custom indent
function ANSI_codes(msg, indent)
    j = 1
    for i = 0, 255 do
        io.write(string.format("\27[38;5;%dm%s\27[0m ", i, msg))
        -- Add indent
        if j % indent == 0 then
            io.write("\n")
        end
        j = j + 1
    end
    io.write("\n")
end

-- Function call
ANSI_codes("foo", 20)