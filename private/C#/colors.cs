using System;

class Program {
    // Define the main function
    static void Main(string[] argv) {
        // Constants
        const int N = 10;
        const string PROMPT = "*";

        // Load all possible ANSI colors
        foreach (ConsoleColor color in Enum.GetValues(typeof(ConsoleColor))) {
            // Change BG color
            Console.BackgroundColor = color;

            // Load N times PROMPT
            for (int i = 0; i < N; i++) {
                Console.Write(PROMPT);
            }
            // Add new line
            Console.WriteLine();
        }
    }
}