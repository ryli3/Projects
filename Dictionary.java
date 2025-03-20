/*
Name:     	Rylie Malbrough
Date:       11/7/2023
Course:     CSC 220 - Data Structures
*/

public class Dictionary extends AbstractDictionary {
	/**
	 * Default Constructor
	 */
	public Dictionary() {
		hashTable = new KVPair[MAX_SIZE];
		DELETED = new KVPair("DELETED", 0.0);
		numKVPairs = 0;
	}

	/*
	public static void main (String[] args)
	{
		Dictionary dictionary = new Dictionary();
		System.out.println("	1	");
		dictionary.add("dd", 79.0); 
		System.out.println("Target Index should be: " + hash(preHash("dd"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	2	");
		dictionary.add("ba", 93.0); 
		System.out.println("Target Index should be: " + hash(preHash("ba"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	3	");
		dictionary.add("ac", 7.0);
		System.out.println("Target Index should be: " + hash(preHash("ac"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	4	");
		dictionary.add("cc", 30.0); 
		System.out.println("Target Index should be: " + hash(preHash("cc"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	5	");
		dictionary.add("bc", 29.0);
		System.out.println("Target Index should be: " + hash(preHash("bc"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary); 

		System.out.println("	6	");
		dictionary.add("ab", 88.0);
		System.out.println("Target Index should be: " + hash(preHash("ab"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	7	");
		dictionary.add("bb", 60.0); 
		System.out.println("Target Index should be: " + hash(preHash("bb"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);


		System.out.println("	8	");
		dictionary.add("ca", 20.0);
		System.out.println("Target Index should be: " + hash(preHash("ca"), dictionary.MAX_SIZE)); 
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	9	");
		dictionary.add("bd", 58.0);
		System.out.println("Target Index should be: " + hash(preHash("bd"), dictionary.MAX_SIZE));
		System.out.println();
		System.out.println(dictionary);

		System.out.println("	10	");
		System.out.println(dictionary.hashTable[9]);
		dictionary.add("cd", 76.0);
		System.out.println("Target Index should be: " + hash(preHash("cd"), dictionary.MAX_SIZE));
		System.out.println(dictionary);
		System.out.println();
	*/	

	

	// Returns true if the Dictionary is empty or full, respectively
	public boolean isEmpty() {return numKVPairs == 0;}
	public boolean isFull() {return numKVPairs == MAX_SIZE;}
	/**
	 * Returns the number of key-value pairs in the dictionary
	 * @return 			the number of key-value pairs
	 */
	public int getSize() {
		return numKVPairs;
	}

	/**
	 * Returns a vertical string representation of the dictionary's hash table
	 * This includes null and deleted KVPairs
	 * @return 			String representation of the dictionary's hash table
	 */
	public String toString() {
		String s = "";
		for (KVPair kvp : hashTable)
		{
			if (kvp == null ) s += "-NULL-\n";
			else if (kvp == DELETED) s += "-DELETED-\n";
			else s += kvp + "\n";
		}

		return s;
	}

	/**
	 * Adds the key and value given to the dictionary as a KVPair by storing it in its proper position
	 * in the backend hash table.  Uses open addressing with linear probing to handle collisions.
	 * @param			key - the key of the KVPair to be added to the dictionary
	 * @param			value - the value of the KVPair to be added to the dictionary
	 */
	public void add(String key, double value) 
	{
		// Make sure dictionary isn't full
		if (!isFull())
		{
			// Get the integer representation of the string key
			int asciiValues = preHash(key);
			// Route that to the hash function in order to get the proper index
			int index = hash(asciiValues, MAX_SIZE);
			//System.out.println("The current target index is: " + index);

			// If the hash table at the index is already filled, we need to do some linear probing to find the next valid index
			// System.out.println(key);
			// System.out.println(index);

			if (hashTable[index] != DELETED && hashTable[index] != null)
			{
				//System.out.println("Probing. . .");
				index = linearProbe(index);
				//System.out.println("New index after probing: " + index);
			}

			// Create a new key value pair with the appropriate values
			KVPair kvp = new KVPair(key, value);
			// Store the KVP at the appropriate index
			hashTable[index] = kvp;
			// Increase number of pairs
			numKVPairs++;
		}
	}

	/**
	 * Returns the value stored in the Dictionary for the given key
	 * @param			key - the key of the KVPair to lookup in the dictionary
	 * @return 			the value of the KVPair containing key
	 */
	public double get(String key) 
	{
		// Make sure dictionary isn't empty
		if (!isEmpty())
		{
			// Look through every key value pair within the hash table
			for (KVPair kvp : hashTable)
			{
				// If the key in the valid kvp matches our key
				if(kvp != null && kvp != DELETED && kvp.getKey() == key)
				{
					// Return the value of that key
					return kvp.getValue();
				}
			}
		}
		// Return invalid index because dictionary would be empty
		return -1;

	}

	/**
	 * Removes the KVPair associated with the given key
	 * @param			key - the key of the KVPair to remove from the dictionary
	 */
	public void remove(String key) 
	{
		// Make sure dictionary isn't empty
		if (!isEmpty())
		{
			// Start index value at zero
			int i = 0;
			// Look through every kvp in the hash table
			for (KVPair kvp : hashTable)
			{
				// Once we find the key we are looking for 
				if(kvp != null && kvp != DELETED && kvp.getKey() == key)
				{
					// Update the hash table kvp to deleted
					hashTable[i] = DELETED;
				}
				// Otherwise, we move onto the next kvp pair
				// Need to increment index as well 
				i++;
			}
			// Decrease number of kvp
			numKVPairs--;
		}

	}

	// Returns the integer representation of our key
	public static int preHash(String key)
	{
		// Set initial values to zero
		int value = 0;
		int index = 0;

		// Loop through the string
		while(index < key.length())
		{
			// Get the first character
			char element = key.charAt(index);
			// Typecast into an integer and add that to our value
			value += (int) element;
			// Move onto next character
			index++;
		}
		// Return the calculated value
		return value;
	}

	// Returns the appropriate index value for the kvp
	public static int hash(int preHashValue, int arrayLength)
	{
		// Take the modulus between the prehash value and the array length to find the index
		// Make sure index is an integer
		int index = preHashValue % arrayLength;
		// Return index
		return index;

	}

	// Finds next appropriate index within the list linearly
	public int linearProbe(int index)
	{
		// Make sure dictionary isn't already full
		// If it is full, there will be no valid indexes for our key
		if (!isFull())
		{
			// Start to the right of our index and increase linearly
			//System.out.println("Searching to the right of the index . . .");
			for (int i = index; i < MAX_SIZE; i++)
			{
				// If the hashtable at that index is null or deleted, we can add
				// our new key there
				if (hashTable[i] == null || hashTable[i] == DELETED) 
				{
					//System.out.println("Found available index at: " + i);
					return i;
				}
			}

			// If we break out of the for loop above, that means that there are no
			// valid indexes to the right of the target index
			// We should now look at indexes to the left of our target index starting
			// at 0
			//System.out.println("Searching to the left of the index . . .");
			for (int i = 0; i < index; i++)
			{
				// If the hashtable at that index is null or deleted, we can add
				// our new key there
				if (hashTable[i] == null || hashTable[i] == DELETED) 
				{
					//System.out.println("Found available index at: " + i);
					return i;
				}
			}
		}

		// Otherwise, our dictionary is full, so we return an invalid index
		return -1;
	}

	// Returns true if there is a duplicate key 
	public boolean search(String key)
	{
		// Make sure dictionary isn't empty
		if(!isEmpty())
		{
			// Get appropriate index from the prehash and hash functions
			int asciiValues = preHash(key);
			int index = hash(asciiValues, getSize());

			// Search through the kvp of the hash table
			for (KVPair kvp : hashTable)
			{
				// As long as those kvp aren't null or deleted
				if (kvp != null && kvp != DELETED)
				{
					// Get the key of the kvp and convert that to the correct index
					String kvpKey = kvp.getKey();
					int kvpASCII = preHash(kvpKey);
					int kvpIndex = hash(kvpASCII, getSize());

					// If the index passed in and the kvp index match, we have a duplicate key
					// Return that index
					if (kvpIndex == index) 
					{
						//System.out.println("Found a duplicate key!");
						return true;
					}
			
				}
				
			}
		}

		// Otherwise, the list is either empty or there are no duplicate keys
		return false;
	}
	    
		
		
		
}
