/*
Name:		[Rylie Malbrough]
Date:		[10/23/2023]
Course:		CSC 220 - Data Structures
*/
import java.util.ArrayList;
import java.util.*;


public class InfixToPostfix extends AbstractInfixToPostfix {
	/**
	 * Evaluate the result of two String operands (a & b) and a String operator and return the result as a String
	 * @param 			a - the first operand
	 * @param 			b - the second operand
	 * @param 			operator - the operator
	 * @return 			The result of "a operator b"
	 */

	public String evaluate(String a, String b, String operator) {
		// parse the operands
		int numA, numB;
		try
		{
			numA = Integer.parseInt(a); 
			numB = Integer.parseInt(b); 
		}

		catch(NumberFormatException e)	
		{
			System.out.println("Invalid operand found during evaluation: ");
			System.out.println("\ta=" + a + ", b=" + b);
			return null;
		}

		if (operator.equals("+")) return ("" + (int)(numA + numB)); 
		else if (operator.equals("-")) return ("" + (int)(numA - numB));
		else if (operator.equals("*")) return ("" + (int)(numA * numB));
		else if (operator.equals("/")) return ("" + (int)(numA / numB));
		else if (operator.equals("^")) return ("" + (int)(Math.pow(numA, numB)));
		else
		{
			System.out.println("Invalid operator found during evaluation");
			return null;
		}


	}

	/**
	 * Returns true if the given token is an integer
	 * @param 			token - the token to test
	 * @return 			true if token is an integer, false otherwise
	 */
	public boolean isOperand(String token) {
		try
		{
			Integer.parseInt(token);
			return true;
		}
		catch (NumberFormatException e)
		{
			return false;
		}
		
	}

	/**
	 * Returns the infix ranking of the given operator, or 0 by default
	 * @param 			operator - the operator to analyze
	 * @return 			the infix rank of operator
	 */
	public int infixOpRank(String operator) {
		if (operator.equals("(")) return 4;
		else if (operator.equals("^")) return 3;
		else if (operator.equals("*") || operator.equals("/")) return 2;
		else if (operator.equals("+") || operator.equals("-")) return 1;
		else return 0; 
	}

	/**
	 * Returns the operator stack ranking of the given operator, or 0 by default
	 * @param			operator - the operator to analyze
	 * @return 			the operator stack rank of operator
	 */
	public int opStackRank(String operator) {
		if (operator.equals("^")) return 2;
		else if (operator.equals("*") || operator.equals("/")) return 2;
		else if (operator.equals("+") || operator.equals("-")) return 1;
		else return 0; 
	}

	/**
	 * Separates a space separated mathematical expression in String representation
	 * and returns an array of Strings containing the individual elements
	 * @param 			expressionString - the expression in String format to separate
	 * @return 			An array of the operands and operators in expressionString
	 */
	public String[] parseExpression(String expressionString) {
		return expressionString.split(" ");
	}

	/**
	 * Returns the string representation of an expression
	 * @param			expression - an array of operands and operators forming a mathematical expression
	 * @return 			expression as a single, space separated String
	 */
	public String expressionToString(String[] expression) {
		String expString = "";
		if (expression.length > 0)
		{
			for (int i = 0; i < expression.length - 1; i++)
			{
				expString += expression[i] + " ";
			}
			expString += expression[expression.length-1];
		}
		return expString;
	}

	/**
	 * Evaluate a postfix expression
	 * Integers only, so the division operation is integer division (no remainder from division)
	 * @param 			postfixExpression - the postfix expression to evaluate
	 * @return 			The result from evaluating postfixExpression
	 */
	public String evaluatePostfix(String[] postfixExpression) {
		// Create an empty stack
		Stack<String> s = new Stack<String>();

		// For each token within our postfix expression
		for ( String token : postfixExpression){

			// If it's an operand, we want to push it to the stack
			if (isOperand(token)){
				s.push(token);
			}

			// Otherwise, our token is an operator
			// We need to pop t he top two items from the stack
			// Evaluate them with the operator
			// Push result back onto stack
			else if (!isOperand(token)){
				// Create two strings that contain the values
				// of our two popped numbers
				String num2 = s.pop();
				String num1 = s.pop();

				// Use evaluate function to evaluate
				// Since our stack is LIFO, thr first value we pop is actually
				// the operand to the left of our operator
				String answer = evaluate(num1, num2, token);

				// Afterwards, push that result onto the stack
				s.push(answer);
			}
		}
		return s.pop();
	}

	/**
	 * Convert an infix expression to a postfix expression
	 * @param 			infixExpression - the infix expression to convert to postfix
	 * @return 			The postfix expression representation of infixExpression
	 */
    public String[] infixToPostfix(String[] infixExpression) {
    	// Create a stack to hold operators
        Stack<String> operatorStack = new Stack<>();
        // Create an empty queue to eventually hold the final postfix expression
        Queue<String> postfixQueue = new Queue<String>();
        // create an infix queue to store the tokens
        Queue<String> infixQueue = new Queue<String>();

        // Loops through each token in the infix expression
        for (String token : infixExpression) {
            // If our token is an operand
            if (isOperand(token)) 
            {
                // Add it to postfix queue
                postfixQueue.enqueue(token);
            } 

            // If token is a right parenthesis, we need to get all the
            // operators of the stack and enqueue them to the postfix queue
            // until a left parenthesis is found (popped but not queued)
            else if (token.equals(")")) 
            {
                // While the stack is not empty and does not equal the left parentheses
                while (!operatorStack.isEmpty() && !operatorStack.peek().equals("(")) {
                    // Enqueue the popped operator 
                    postfixQueue.enqueue(operatorStack.pop());
                }

                // if we reach left parenthesis
                if (!operatorStack.isEmpty() && operatorStack.peek().equals("(")) {
                    //Pop the left parenthesis off the stack, discard the "("
                    operatorStack.pop();
                } 

            } 

            else 
            {
            	// While the operator stack priority of the operator on top the operator 
                // is greater than or equal to the infix operator priority of the token
                // and make sure stack is not empty
                while (!operatorStack.isEmpty() && opStackRank(operatorStack.peek()) >= infixOpRank(token)) {
                    // Pop the operator from the operator stack and enqueue it to the
                    // postfix queue
                    postfixQueue.enqueue(operatorStack.pop());
                }
                // Once this is finished, all operators on the operator on the operator stack
                // of greater or equal priority to the token will be in the postfix queue
                // We then just push the token on top of the operator stack
                operatorStack.push(token);
            }
        }

        // Now we just need to pop all the operators off the stack and
        // add them to the postfix queue
        // until the stack is empty
        while (!operatorStack.isEmpty()) 
        {
          postfixQueue.enqueue(operatorStack.pop());  
        }

        // Create a string array to be the expression
        String[] postfixString = new String[postfixQueue.size()];

        int index = 0;
        // loop until queue is empty
        while (!postfixQueue.isEmpty())
        {
        	// get the value of the queue at i
            String value = postfixQueue.dequeue();
            // and set that value equal to the string at index i
            postfixString[index] = value;
            index++;
        }
        // return value
        return postfixString;
    }
 
}