using System;
using Calculator;

namespace Calculator
{
    class Interact
    {
        static void @WriteLine(string str)
        {
            Console.WriteLine(str);
        }

        static void Main()
        {
            while (true)
            {
                Interact.@WriteLine("Please enter your first number press enter then enter your second number");
                string @inputOne = Console.ReadLine();
                string @inputTwo = Console.ReadLine();
                checked
                {
                    try
                    {
                        @WriteLine($"Calculation.Logic({@inputOne}, {@inputTwo})");
                        break;
                    }
                    catch (System.FormatException)
                    {
                        @WriteLine("Sorry but your input wasn't in the correct format.");
                    }
                }
            }
        }
    }
}