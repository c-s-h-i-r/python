using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    /// <summary>
    /// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    /// For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
    /// which means that 28 is a perfect number.
    /// A number n is called deficient if the sum of its proper divisors is less than n and
    /// it is called abundant if this sum exceeds n.
    /// 
    /// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
    /// that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
    /// it can be shown that all integers greater than 28123 can be written as the sum of two 
    /// abundant numbers. However, this upper limit cannot be reduced any further by analysis even 
    /// though it is known that the greatest number that cannot be expressed as the sum of two abundant 
    /// numbers is less than this limit.
    /// 
    /// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    /// </summary>
    class NonAbundantSums
    {
        private const int UPPERBOUND = 28123;
        //find a list of abundant numbers under 28123 and check each value - more efficient
        List<int> abundantNumbers = new List<int>();

        public NonAbundantSums()
        {
            //find sum of positive integers...
            findAbundant();
            BigInteger sum = listOfSumOfAbundantNumbers(UPPERBOUND);
            
            Console.WriteLine("Sum = " + sum);
        }

        private BigInteger listOfSumOfAbundantNumbers(int n)
        {
            Console.WriteLine("Gathering list of abundant numbers");
            BigInteger sum = 0;

            List<int> l = Enumerable.Range(1, UPPERBOUND).ToList();
            
            List<int> no = new List<int>(abundantNumbers);
            
            foreach(int a in abundantNumbers){
                foreach(int num in abundantNumbers){
                    //all sums
                    int together = a + num;
                    if (together <= UPPERBOUND)
                    {
                        no.Add(together);
                    }
                }
            }
            l = l.Except(no).ToList();

            ////for all positive integers
            //for (int i = 1; i < n; i++)
            //{
            //    foreach (int j in abundantNumbers)
            //    {
            //        if (!abundantNumbers.Contains(i - j))
            //        {
            //            sum += i;
            //        }
            //    }
            //    Console.WriteLine((double)i/UPPERBOUND);
            //}
            //Console.Write(Environment.NewLine);

            foreach (int i in l)
            {
                sum += i;
            }
            return sum;
        }
        private void findAbundant(){
            for(int i = 1; i < UPPERBOUND; i++){
                if(isPerfect(i) == 1){
                    abundantNumbers.Add(i);
                }
            }
        }

        //1 abundant; 0 perfect; -1 deficient
        private int isPerfect(int n)
        {
            BigInteger sum = sumDivisors(n);
            //is perfect number -> sum of proper divisors == n
            if (sum == n)
                return 0;
            if (sum > n)
                return 1;
            return -1;
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
                    int d2 = n / i;
                    divisors.Add(d2);
                    sum += i + d2;
                }
            }

            return sum;
        }
    }
}
