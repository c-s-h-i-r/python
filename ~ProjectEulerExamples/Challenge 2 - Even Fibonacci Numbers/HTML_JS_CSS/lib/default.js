
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
	
	function findSum(upperBound){
		
	}
	
	
	
}());