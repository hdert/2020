using System;

namespace Calculator
{
    class Calculation
    {
        static int Main()
        {
            Console.WriteLine("This is an addition calculator.");
            while (true)
            {
                Console.WriteLine("Input your first number, press enter, then input your second number, press enter.");
                checked
                {
                    try
                    {
                        Console.WriteLine($"Your result is: {Convert.ToDecimal(Console.ReadLine()) + Convert.ToDecimal(Console.ReadLine())}");
                        break;
                    }
                    catch (System.FormatException)
                    {
                        Console.WriteLine("Sorry but your input wasn't in the correct format.");
                    }
                }
            }
            return 0;
        }
    }
}