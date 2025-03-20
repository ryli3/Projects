/*
Name:     	Rylie Malbrough
Date:       11/6/2023
Course:     CSC 220 - Data Structures
*/

import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

public class Sort extends AbstractSort {

	public static void main(String[] args) 
	{
		/*
		Sort s = new Sort();
		int[] quickArray = {13, 9, 5, 7, 12, 2, 3, 14, 6, 1};

		// Quick sort
		
		System.out.println(" #### Testing Shell Sort #### ");
		System.out.println("Initial Array:" + Arrays.toString(quickArray));
		s.shellSort(quickArray, 3);
		System.out.println("Sorted Array: " + Arrays.toString(quickArray));
		
		System.out.println(" #### Testing Heap Sort #### ");
		System.out.println("Initial Array:" + Arrays.toString(quickArray));
		s.heapSort(quickArray);
		System.out.println("Sorted Array: " + Arrays.toString(quickArray));

		*/
	}

	/**
	 * Returns an array of random integers between 0-99 given a size and seed
	 * @param 			size - the desired size of the array being generated
	 * @param 			seed - the seed used to initialize the random number generator
	 * @return 			an array of random integers between 0-99 (without duplicates)
	 */
	public int[] generateRandomArray(int size, int seed) {
		Random r = new Random(seed);

		// Create the choices bank
		ArrayList<Integer> bank = new ArrayList<Integer>();
		for (int i = 0; i < 100; i++) bank.add(i);

		// fill an array with random selections from the choices bank (no duplicates)
		int[] array = new int[size];
		for (int i = 0; i < size; i++) array[i] = bank.remove(r.nextInt(bank.size()));

		return array;
	}

	/**
	 * Public interface to the quick sort algorithm. 
	 * @param 			array - the array of integers to sort
	 */
	public void quickSort(int[] array) {
		quickSort(array, 0, array.length - 1);
		
	}

	/**
	 * Recursive quickSort algorithm.  This version always chooses the first element as the pivot,
	 * but this is not the only or best method for choosing a pivot!
	 * Uses the private quickSort method to do the sorting.
	 * @param 			array - the array of integers to sort
	 * @param			first - the index of the first element in the current subarray being sorted
	 * @param			last - the index of the last element in the current subarray being sorted
	 */
	private void quickSort(int[] array, int first, int last) {
		// Choose a pivot number and position the left and right cursors
		int pivot = array[first];
		int leftCursor = first + 1;
		int rightCursor = last + 1;

		// Search for swaps until the two cursors meet
		while (leftCursor != rightCursor)
		{
			// Search for a value larger than the pivot with the left cursor
			while (leftCursor != rightCursor)
			{
				if (array[leftCursor] > pivot) break;
				leftCursor++;
			}

			// Search for a value smaller than the pivot with the right cursor
			while (leftCursor != rightCursor)
			{
				rightCursor--;
				if (array[rightCursor] < pivot) break;	
			}

			// Swap values if the cursors haven't met yet
			if (leftCursor != rightCursor)
			{
				int temp = array[leftCursor];
				array[leftCursor] = array[rightCursor];
				array[rightCursor] = temp;
			}

		}

		// Swap the pivot with the value at the cursors
		array[first] = array[leftCursor - 1];
		array[leftCursor - 1] = pivot;

		// Recursively sort the sub array to the left of the cursors
		if ((leftCursor - 2) - first > 0)
		{
			quickSort(array, first, leftCursor - 2);
		}

		// Recursively sort the sub array to the right of the cursors
		if (last - rightCursor > 0)
		{
			quickSort(array, rightCursor, last);
		}
		
	}

	/**
	 * The shell sort algorithm.
	 * @param			array - the array of integers to sort
	 * @param			k - the spacing counter used by shell sort
	 */
	public void shellSort(int[] array, int k) {
		// k is the spacing counter; we need to make sure it's greater than zero 
		while (k > 0)
		{
			// This value keeps track of every time we call insertion sort 
			int i = 0;
			while (i < k)
			{
				// Call insertion sort
				insertionSort(array, k, i);

				// Increase to next number
				i++;
			}
			// We then need to decrease the space between indexes
			k--;
		}
	}

	public static void insertionSort(int[] array, int k, int startIndex)
	{
		// We need to begin with the 'second' index that we are looking at
		// We have to make sure we stay under the size of the array
		// And we increment by the k-value every loop
		for (int i = startIndex + k; i < array.length; i += k)
		{
			// Set up our values/indexes
			int secondValue = array[i];
			int firstIndex = i - k;

			// Loop through until our first element is no longer bigger than the second 
			while(firstIndex >= startIndex && array[firstIndex] > secondValue){
				array[firstIndex + k] = array[firstIndex];
				firstIndex -= k;
			}

			// Swap our values
			array[firstIndex + k] = secondValue;
		}
	}

	/**
	 * The heap sort algorithm.
	 * @param			array - the array of integers to sort
	 */
	public void heapSort(int[] array) 
	{
		// Create a heap to store the array elements
		Heap heap = new Heap();
		// Loop through each element in the array
		for(int element : array)
		{
			// And add it to the heap
			heap.add(element);
		}

		// This is looping through the array right to left
		for (int i = array.length - 1; i >= 0; i--)
		{
			// get the max element from the heap
			int element = heap.getMax();
			// add to end of the list
			array[i] = element;
		}
	}
}