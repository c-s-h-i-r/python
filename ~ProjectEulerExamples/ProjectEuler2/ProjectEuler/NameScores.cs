using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class NameScores
    {
        /// <summary>
        /// Using names.txt containing over five-thousand first names, 
        /// begin by sorting it into alphabetical order. 
        /// Then working out the alphabetical value for each name, 
        /// multiply this value by its alphabetical position in the list to obtain a name score.
        /// 
        /// For example, when the list is sorted into alphabetical order, 
        /// COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
        /// So, COLIN would obtain a score of 938 × 53 = 49714.
        /// What is the total of all the name scores in the file?
        /// </summary>
        public NameScores(string filename)
        {
            Console.WriteLine(getTotal(readNames(filename)));
        }
        
        public List<string> readNames(string filename)
        {
            string[] lines = null;
            try
            {
                lines = File.ReadAllLines(filename);
            }
            catch (Exception) { }

            lines[0] = lines[0].Replace("\"", "");
            lines = lines[0].Split(',');
            
            //sort
            List<string> l = lines.ToList();
            l.Sort();
            return l;
        }

        private long getTotal(List<string> l)
        {
            int i = 0;
            List<long> scores = new List<long>();

            //find alphabetical value
            foreach (string s in l)
            {
                i++;
                Names n = new Names(s, i, alphaValue(s));
                scores.Add(n.calculateScore());

            }
            long sum = 0;
            foreach (int j in scores)
            {
                sum += j;
            }
            return sum;
        }


        //compute sum of numerical value of characters in string ie.a = 1, b=2
        public int alphaValue(string s)
        {
            int sum = 0;
            foreach (char c in s.ToCharArray())
            {
                sum += (int)c % 32;
            }
            return sum;
        }
    }
    
    class Names
    {
        string name = "";
        int position = 0;//alphabetical position
        int value = 0;
        long score = 0;

        public Names(string name, int position, int value)
        {
            this.name = name;
            this.position = position;
            this.value = value;
        }
        public long calculateScore()
        {
            this.score = this.value * this.position;
            return this.score;
        }

    }
}
