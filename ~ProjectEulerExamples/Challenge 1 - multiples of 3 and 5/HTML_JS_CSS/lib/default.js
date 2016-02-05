
(function () {
    "use strict";

    window.addEventListener("load", function load(event) {
        window.removeEventListener("load", load, false);
        init();
    }, false);

    function init() {
        document.getElementById("link").addEventListener("click", showSum, false);
    }
	
	//get input from textbox and put result in result label
	function showSum(){
		var upperBound = document.getElementById("input").value;
		
		document.getElementById("result").innerHTML = findSum(upperBound);
	}
	
	//If we list all the natural numbers below 10 that are multiples 
    // of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    // 
    // Find the sum of all the multiples of 3 or 5 below 1000.
	function findSum(upperBound){
		var sum = 0;
		var n = upperBound;
		var initialMultiples = [3,5];
		var multiples = [3,5];
		var endFlag = false, firstPass = true;
		
		while(!endFlag){
			endFlag = true;
			firstPass = true;
			for(var i = 0; i < multiples.length; i++){
				if(multiples[i] < n ){
					if(firstPass || multiples[i] % initialMultiples[1] != 0){
						sum += multiples[i];
						endFlag = false;
					}
					firstPass = false;
					
				}
				multiples[i] += initialMultiples[i];
			}
		}
		return sum;
	}
	
	//return true if at least one element in the array is less than n
	function oneIsLessThan(array, n){
		for(var i = 0; i < array.length; i++){
			if(array[i] < n){
				return true;
			}
		}
		return false;
	}
	
}());