using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace ProjectEuler
{
    class FactorialDigitSum
    {
        private Dictionary<int, int> factorialDict = new Dictionary<int, int>();

        /// <summary>
        /// n! means n × (n − 1) × ... × 3 × 2 × 1
        /// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        /// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
        /// Find the sum of the digits in the number 100!
        /// </summary>


        public BigInteger factorial(int n)
        {
            if (n < 1) return 0;
            if (n == 1) return 1;
            BigInteger result = n;
            
            for (int i = n-1; i > 0; i--)
            {
                result *= i;

             
            }
            return result;

        }
        /// <summary>
        /// Count up the digits in a given integer.
        /// </summary>
        public BigInteger sumDigits(BigInteger n)
        {
            BigInteger sum = 0, digit = 0;
            List<BigInteger> digits = new List<BigInteger>();

            while (n > 10)
            {
                digit = n % 10; // get digit
                digits.Add(digit);
                sum += digit;
                n /= 10;
            }
            digits.Add(n);
            sum += n;
            string d = string.Empty;
            for (int i=digits.Count-1; i >= 0; i--)
            {
                d += digits[i].ToString();
            }
            
            return sum;
        }

        public FactorialDigitSum(int n)
        {
            Console.WriteLine(sumDigits(factorial(n)));
        }
            
    
    
    }
}
