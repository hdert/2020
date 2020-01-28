using System;

namespace Calculator
{
    public class Calculation
    {
        static public decimal Logic(string inputOne, string inputTwo)
        {
            return Convert.ToDecimal(inputOne) + Convert.ToDecimal(inputTwo);
        }
    }
}