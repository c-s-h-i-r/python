using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Program
    {
        
        static void Main(string[] args)
        {
            //CountSundays cs = new CountSundays();
            //AmicableNumbers an = new AmicableNumbers(10000);
            //FactorialDigitSum fds = new FactorialDigitSum();
           // NameScores n = new NameScores(@"../../../names.txt");
            //NonAbundantSums nas = new NonAbundantSums();

            int sequenceLength = 0;

           // for (int i = 1000; i > 1; i--)
           // {
            int i = 7;
                if (sequenceLength >= i)
                {
                    ;
                }

                int[] foundRemainders = new int[i];
                int value = 1;
                int position = 0;

                while (foundRemainders[value] == 0 && value != 0)
                {
                    foundRemainders[value] = position;
                    value *= 10;
                    value %= i;
                    position++;
                }

                if (position - foundRemainders[value] > sequenceLength)
                {
                    sequenceLength = position - foundRemainders[value];
                }
           // }
            Console.WriteLine(sequenceLength);
            Console.ReadLine();
        }
    }
}
