/*
Name:	 	Rylie Malbrough
Date:		10/11/2023
Course:		CSC 220 - Data Structures
*/

public class LinkedList<Type> extends AbstractLinkedList<Type> {
	/**
	 * Default Constructor - Newly constructed lists have no nodes,
	 * so head and tail point to null.
	 */
	public LinkedList() {
		// No nodes in base linked list
		head = null;
		current = null;
		tail = null;
		numElements = 0;
	}

	/**
	 * Copy constructor - copies each element from the given linked list
	 * into the one being constructed.
	 * @param 			l - the linked list being copied from
	 */
	public LinkedList(LinkedList<Type> l) {
		// Set the initial elements to null
		head = null;
		current = null;
		tail = null;
		numElements = 0;

		// Create a new linked list
		LinkedList<Type> list = new LinkedList<Type>();

		// Set the initial node to head of the parameter list
		Node<Type> tempNode = l.head;

		// Loop through the list until you reach the end
		for (int index = 0; index < l.size(); index++)
		{
			// If we are at the head node, we must denote it as such
			if (index == 0)
			{
				// The head is the current node we are at
				head = tempNode;
				// Add the data to the new list we created
				// List is empty; we don't have to worry about indexes
				list.add(head.getData());
				// Increase the number of elements
				numElements++;
			}

			// If we are at the tail node, we must denoate it as such
			if (index == l.size()-1)
			{
				// The tail is the current node we are at 
				tail = tempNode;
				// Add the data to the new list we created
				// List is no longer empty, but we can just
				// Add to end of the list
				list.add(tail.getData());
				// Increase number of elements
				numElements++;
				// Break from the loop because we don't want
				// To continue adding more nodes after the tail
				break;
			}

			// Loop through the nodes in the parameter list
			tempNode = tempNode.getLink();
			// Add each node from the parameter list at the index to the 
			// New list at that same index
			list.add(index, tempNode.getData());
			// Increase number of elements
			numElements++;			

		}

	}

	/**
	 * Returns a String representation of the list ("NULL" if empty)
	 * @return 			String representation of the linked list
	 */
	public String toString() {
		if (head == null)
		{
			return "NULL";
		}
		else
		{
			// Initialize string representation of the linked list
			String s = "";

			// Start traversing the list at the head
			Node<Type> temp = head;

			// Loop through linked list 
			while (temp != null)
			{	
				// Gets data in node
				s += temp.getData() + " ";

				// Updates memory address to next link
				temp = temp.getLink();
			}

			return s;
		}
	}

	/**
	 * Returns the number of elements in the list (not the max capacity)
	 * @return 			number of elements in the linked list
	 */
	public int size() {
		return numElements;
	}

	/**
	 * Returns true if there are no elements in the list
	 * @return 			true if list is empty, false otherwise
	 */
	public boolean isEmpty() {
		// Evaluates to true or false
		return (numElements == 0);
	}

	/**
	 * Returns true if the number of elements in the list is equal to MAX_SIZE
	 * @return 			true if list is full, false otherwise
	 */
	public boolean isFull() {
		// Evaluates to true of false 
		return (numElements == MAX_SIZE);
	}

	/**
	 * Set the current Node reference to the head node
	 */
	public void first() {
		current = head;
		
	}

	/**
	 * Set current to the next node in the list
	 */
	public void next() {
		current = (current != null) ? current.getLink() : current;
		// Runs the left if current is not null (true), right if current is null (false) 
		// Prevents you from crashing your program
		
	}

	/**
	 * Return the element at the current node
	 * @return 			element stored at the current node
	 */
	public Type getCurrent() {
		return (current != null) ? current.getData() : null;
	}

	/**
	 * Adds the specified element to the end of the list.
	 * Not possible for a full list.
	 * @param 			element - element to add to the linked list
	 */
	public void add(Type element) {
		// Don't add anything if the list is full
		if(!isFull())
		{
			//If the list is empty, the new node becomes the head
			if (isEmpty()){
				head = new Node<Type>();
				head.setData(element);
				current = head;
				tail = head;
			}

			//If the list is not empty, the new node is added to the end of the list
			else
			{
				tail.setLink(new Node<Type>());
				tail = tail.getLink();				// Set the tail to the new node
				tail.setData(element);				// Get the data from parameter

			}

			// Increment number of elements
			numElements++;

		}
		
	}

	/**
	 * Adds the specified element to the list at the given index
	 * Not possible for a full list
	 * @param			index - the position in the list to add the element
	 * @param			element - the element to be added to the list
	 */
	public void add(int index, Type element){
		// Only add if list isn't full and if index is valid
		if (!isFull() && index >= 0 && index <= MAX_SIZE - 1)
		{
			// If we want to add something to take the place of the head node
			if (index == 0)									
			{
				// Create a new node to add into the list
				Node<Type> newNode = new Node<Type>();

				// Set link to head node
				newNode.setLink(head);

				// Set the head equal to the new node
				head = newNode;
				// Set the head node's data to the data we passed in as a parameter
				head.setData(element);
				// Increase the number of elements
				numElements++;
				// end 
				return;
			}

			// if index is out of bounds
			if (index > numElements - 1)
			{
				return;
			}

			// If we need to add to end of list
			if (index == numElements-1)
			{
				Node<Type> newNode = new Node<Type>();
				tail.setLink(newNode);
				tail = newNode;
				newNode.setData(element);
				numElements++;
				return;
			}
			// Otherwise, we have to loop through the list in order to find the index we must replace
			// Create the node to add into
			Node<Type> newNode = new Node<Type>();

			// Create a temporary node to loop through the list
			Node<Type> currentNode = head;

			// Current node will be at the index we passed in until we shift it to the right (update it's link)
			// Loop through linked list to find the node at that index
			for (int i = 0; i < index && currentNode != null; i++)
			{
				currentNode = currentNode.getLink();
			}

			// Set our new node's link to the node at its index
			// Once we shift the old node to the right, we need our new 
			// node to point towards it
			newNode.setLink(currentNode);

			// Set the link of the previous node to point towards the new node
			// Loop until we reach the index right before where want to insert our node
			Node<Type> previousNode = head;
			for (int i = 0; i < index - 1 && previousNode != null; i++)
			{
				previousNode = previousNode.getLink();
			}

			// Set the previous' link to the new node 
			previousNode.setLink(newNode);

			// Update the data of the new node
			newNode.setData(element);

			// Increase number of elements
			numElements++;
		}
	}

	/**
	 * Returns the value in the node at the given index
	 * @param 			index - the position in the list to get the element from
	 * @return 			the element at index
	 */
	public Type get(int index) {
		// Don't traverse the list if the index is out of bounds
		if(!(index < 0 || index >= numElements))
		{
			Node<Type> temp = head;
			int i = 0;

			// Traverse the list starting at the head until index is reached
			while(i < index)
			{
				temp = temp.getLink();
				i++;
			}

			return temp.getData();
		}
		else
		{
			return null;
		}
	}

	/**
	 * Returns the value in the head node
	 * @return 			the value in the head node
	 */
	public Type getFirst() {
		return (head != null) ? head.getData() : null;

	}

	/**
	 * Returns the value in the tail node
	 * @return 			the value in the tail node
	 */
	public Type getLast() {
		return (tail != null) ? tail.getData() : null;
	}

	/**
	 * Removes the element at the specified index.
	 * Not possible for an empty list
	 * @param			index - the position in the list of the element to be removed
	 */
	public void remove(int index) {
		// Making sure index is valid and the list is not empty
		if(index <= numElements - 1 && index >= 0 && numElements > 0)
		{
			// If we want to remove the head node, we can just update it to the next node
			if (index == 0)
			{
				head = head.getLink();
				// Decrease number of elements
				numElements--;
			}

			// If we want to remove the tail node
			if (index == numElements-1)
			{
				// Create a node to represent the new tail node
				Node<Type> newTailNode = head;
				
				// Loop under we find the node right before the current tail node
				for (int i = 0; i < index - 1; i++)
				{
					newTailNode = newTailNode.getLink();
					
				}

				// The node before our current tail will become the tail node
				// Set the new tail node's link to null (effectively 'deleting' the previous tail node)
				newTailNode.setLink(null);
				// Update tail to the new node
				tail = newTailNode;
				
			}

			// Otherwise, we want to get rid of nodes in the middle of the list
			else if (index > 0 && index < numElements - 1)
			{
				// Create a variable to represent the previous node in the list
				Node<Type> previousNode = head;

				// Loop through list until you find the previous node at index - 1
				for(int i = 0; i < index - 1; i++)
				{
					previousNode = previousNode.getLink();
				}

				// Create a variable to store the following node
				// Get that node by traveling two nodes down from the previous 
				Node<Type> followingNode = previousNode.getLink().getLink();

				// Set the previous' node link to the following node
				// This effectively 'skips' over the original node placed at that index 
				previousNode.setLink(followingNode);
				// Decrease the number of elements
				numElements--;
			
			}
			
			

		}
	}

	/**
	 * Replaces the element at the specified index with the given element
	 * @param			index - the position in the list of the element to replace
	 * @param			element - the element to replace the current element at index
	 */
	public void set(int index, Type element) {
		// Make sure index is valid
		if (index <= MAX_SIZE - 1 && index >= 0)
			// If we want to replace the head node, we just need update its data
			if (index == 0)
			{
				head.setData(element);
			}
			// Otherwise, we need to 
			// Traverse list until we reach desired index
			Node<Type> temp = head;

			for (int i = 0; i < index; i++)
			{
				temp = temp.getLink();
			}
			// Update the data to be the data we pass in
			temp.setData(element);
	}

	/**
	 * Returns the index of the first occurrence of the specified element.
	 * Returns -1 if the list does not contain the element.
	 * @param			element - the element whose index is being searched for
	 * @return 			the index of element, or -1 if it doesn't exist
	 */
	public int indexOf(Type element) {
		// Check to see if it's the head node
		if (head != null && head.getData() == element)
		{
			return 0;
		}

		// Otherwise, we must
		// Traverse through the list
		Node<Type> temp = head;
		int i = 1;
		while(temp != null)
		{
			temp = temp.getLink();
			if (temp != null && temp.getData() == element)
			{
				return i;
			}
			i++;
		}

		// If element is not found
		return -1;
	}
}
