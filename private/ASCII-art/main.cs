// Require libraries
using System;
using System.Threading;
using System.Linq;

class Program {
    static int Main (string[] argv) {

        // Handle correct number of command line arguments - 1
        if (argv.Length != 2) {
            Console.WriteLine("Usage: ./main.exe $INPUT_FILE_PATH $ANIMATION_SPAN");
            return 1;
        }

        // Assign desired file path
        string inputPath = argv[0];

        // Assign animation span type int
        int animationSpan = Convert.ToInt32(argv[1]);

        Console.WriteLine("Hello!, Press <Control> + <C> to abort.\n\n");  // Initial header
        Thread.Sleep(750);
        Console.Clear();

        // Write lyrics
        string[] text = System.IO.File.ReadAllLines(inputPath);

        // Display each text line
        int x = 0;
        foreach (string t in text[1..]) {
            Console.WriteLine(string.Concat(Enumerable.Repeat("\t", x + 1)) + t);
            Thread.Sleep(800);
            x++;
        }
        Console.Clear();

        /* 
        ASCII ART SOURCE
        -> https://fsymbols.com/text-art/heart/
        */

        // Number of constant scenes
        const int MAX = 4;

        // Constant Console color scenes
        ConsoleColor[] colors = {ConsoleColor.Red,
                                ConsoleColor.Green, 
                                ConsoleColor.Blue, 
                                ConsoleColor.Yellow};

        for (int k = 0; k < animationSpan; k++) {
            for (int i = 0; i < MAX; i++) {

                // Load lines from the current scene 
                string[] lines = System.IO.File.ReadAllLines($"scene/frame{i + 1}.txt");

                // Display each line of the current theme
                foreach (string line in lines) {

                    // Change Console color every iter
                    Console.ForegroundColor = colors[i];

                    // Write each row
                    Console.WriteLine(line, Console.ForegroundColor);
                }

                // Threading
                Thread.Sleep(350);
                Console.Clear();
            }
        }

        // Indicate successful file completion
        return 0;
    }
}
