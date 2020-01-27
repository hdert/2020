using System;

namespace Calculator
{
    class Calculation
    {
        static public decimal Logic(string inputOne, string inputTwo)
        {
            var firstNumber = Convert.ToDecimal(inputOne);
            var secondNumber = Convert.ToDecimal(inputTwo);
            decimal result = firstNumber + secondNumber;
            return result;

        }
    }
}