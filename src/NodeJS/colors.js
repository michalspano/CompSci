var RESET = '\x1b[0m';
var MSG = 'A'; // Type your 
// Transform RGB color to ANSI color escape
function rgbToANSI(r, g, b) {
    return "\u001B[38;2;".concat(r, ";").concat(g, ";").concat(b, "m");
}
for (var i = 255; i > 0; i--) {
    process.stdout.write("".concat(rgbToANSI(i, i, i), "A").concat(RESET, " "));
}
console.log();
