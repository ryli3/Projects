/*
Name: 		Rylie Malbrough
Date: 		9/20/2023
Course: 	CSC 220 - Data Structures
*/

public class ComplexityAnalyzer extends AbstractComplexityAnalyzer {
	/**
	 * Returns a String containing the names of the functions that could have
	 * possibly generated the output given the input
	 * @param 		input number
	 * @param 		output number
	 * @return 		names of possible functions
	 */
	public String analyzeComplexity(double input, double output) {
		// Takes input and output and compares them
		// If it has more than one answer, return all appropriate answers  
		// Create a string for the answer, initialize it as null
		String answer = null;

		// Check if values are constant
		if (output == 1){
			answer = "Constant";
		}

		// Check if values are logarithmic
		// Get the result of log2(input)
		double result = logBaseTwo(input);
		// Check to see if the result and output are the same
		if (result == output){
			// If the answer has been replaced with another string
			if (answer != null){
				// Add a comma space
				answer += ", Logarithmic";
			}
			// Otherwise, no other condition was added to the answer, just add the string
			else{
				answer = "Logarithmic";
			}

		}

		// Check if values are linear
		if (output == input){
			if (answer != null){
				answer += ", Linear";
			}
			else{
				answer = "Linear";
			}
		}

		// Check if values are Quasi-linear
		if (output == input * logBaseTwo(input)){
			if (answer != null) {
				answer += ", Quasi-Linear";
			}
			else
			{
				answer = "Quasi-Linear";
			}
		}

		// Check if values are quadratic 
		if (Math.pow(input,2) == output){
			if (answer != null)
			{
				answer += ", Quadratic";
			}
			else
			{
				answer = "Quadratic";
			}
			
		}
		// Check if values are cubic
		if (Math.pow(input, 3) == output){
			if (answer != null)
			{
				answer += ", Cubic";
			}
			else
			{
				answer = "Cubic";
			}
		}
		// Check if values are Exponential 
		if (output == Math.pow(2, input)){
			if (answer != null){
				answer += ", Exponential";
			}
			else
			{
				answer = "Exponential";
			}
		}

		return answer;
		
	}
	// Function that uses change of base to find logBaseTwo of a number
	public static double logBaseTwo(double x){
		return Math.log(x) / Math.log(2);		
	}


}
