using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    /// <summary>
    /// A permutation is an ordered arrangement of objects. 
    /// For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
    /// If all of the permutations are listed numerically or alphabetically,
    /// we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    /// 012   021   102   120   201   210
    /// 
    /// What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    /// </summary>
    class LexicographicPermutations
    {
        private int[] digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        private SortedSet<long> permutations = new SortedSet<long>();
        public LexicographicPermutations()
        {
            //find permutations
            foreach (int i in digits)
            {
                string number = i.ToString();
                int[] digitsMinusOne = digits.Except(new int[] { i }).ToArray();
                foreach()
                foreach (int j in digitsMinusOne)
                {
                    number += j.ToString();
                }
                permutations.Add(long.Parse(number));
            }
            Console.WriteLine(permutations.ElementAt(1000000));
            
        }
    }
}
