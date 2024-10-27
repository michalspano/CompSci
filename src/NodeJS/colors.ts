declare var process: any;

const RESET: string = '\x1b[0m'
const MSG: string   = 'A'; // Type your 

// Transform RGB color to ANSI color escape
function rgbToANSI(r: number, g: number, b: number): string {
  return `\x1b[38;2;${r};${g};${b}m`;
}

for (let i: number = 255; i > 0; i--) {
  process.stdout.write(`${rgbToANSI(i, i, i)}A${RESET} `);
}

console.log();
