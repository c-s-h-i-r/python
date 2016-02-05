using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApplication1
{
    /// <summary>
    /// If we list all the natural numbers below 10 that are multiples 
    /// of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    /// 
    /// Find the sum of all the multiples of 3 or 5 below 1000.
    /// </summary>
    public partial class MainWindow : Window
    {
        private int upperBound = 1000; 
        public MainWindow()
        {
            InitializeComponent(); 
            
        }
        /// <summary>
        /// disregard duplicates!!!
        /// </summary>
        /// <returns>sum of multiples of 3 and 5's STRICTLY below upperBound</returns>
        private int findSums(){
            //for 3 and 5
            
            int n = upperBound;
            int sum = 0;
            int threes = 3;
            int fives = 5;
            while(threes < n || fives < n)
            {


                if (threes < n)
                {
                    sum += threes;
                }
                //not divisible by the other (3)
                if (fives < n && fives % 3 != 0)
                {
                    sum += fives;
                }
                //increment to next multiple of numbers to find ie. 3,5
                threes+=3;
                fives+=5;
            }
            return sum;

        }//findSums

        private void Submit_Click(object sender, RoutedEventArgs e)
        {
            int anInteger;
            try
            {
                anInteger = int.Parse(userInput.Text);
            }
            catch (Exception)
            {
                return;
            }
                upperBound = anInteger;
            Result.Content = findSums();

        }
    }
}
