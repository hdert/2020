using System;

namespace Calculator
{
    class Interact
    {
        static void Main()
        {
            while (true)
            {
                Console.WriteLine("Please enter your first number press enter then enter your second number");
                checked
                {
                    try
                    {
                        Console.WriteLine($"Your answer: {Calculation.Logic(Console.ReadLine(), Console.ReadLine())}");
                        break;
                    }
                    catch (System.FormatException)
                    {
                        Console.WriteLine("Sorry but your input wasn't in the correct format.");
                    }
                }
            }
        }
    }
}