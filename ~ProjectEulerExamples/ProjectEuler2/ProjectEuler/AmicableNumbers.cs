using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace ProjectEuler
{
    /// <summary>
    /// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    /// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
    /// each of a and b are called amicable numbers.
    /// 
    /// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    /// therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    /// Evaluate the sum of all the amicable numbers under 10000.
    /// </summary>
    class AmicableNumbers
    {
        /// <summary>
        /// Sums up all the amicable numbers under given n.
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        public BigInteger sumAmicableLessThan(int n)
        {
            HashSet<BigInteger> set = new HashSet<BigInteger>();
            BigInteger sum = 0;
            for (int i = 1; i < n; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    if (j != i)
                        if (isAmicable(i, j))
                        {
                            set.Add(i);
                            set.Add(j);
                        }
                }
            }
            foreach (BigInteger bi in set)
                sum += bi;
            return sum;
        }

        public bool isAmicable(int a, int b)
        {
            if (sumDivisors(a) == b && sumDivisors(b) == a)
            {
                return (a != b);
            }
            return false;
        }
                
        /// <summary>
        /// find Sum of proper divisors
        /// </summary>
        /// <param name="n"> integer to find proper divisors of</param>
        /// <returns>BigInteger which is the sum of the divisors</returns>
        public BigInteger sumDivisors(int n)
        {
            BigInteger sum = 1;
            List<int> divisors = new List<int>();
            divisors.Add(1);
            //find divisors
            for (int i = 2; i < Math.Sqrt(n); i++)
            {
                if (n % i == 0)
                {
                    //divisor!
                    divisors.Add(i);
                    int d2 = n/i;
                    divisors.Add(d2);
                    sum += i + d2;
                }
            }
            
            return sum;
        }


        public AmicableNumbers(int n)
        {
            Console.WriteLine(this.sumAmicableLessThan(n));
        }
    }
}
