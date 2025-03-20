/*
Name:       Rylie Malbrough
Date:       10/30/2023
Course:     CSC 220 - Data Structures
*/

public class Heap extends AbstractHeap {
    /**
     * Default constructor - initializes data to have a size equal to MAX_SIZE
     */
    public Heap() {
        data = new int[MAX_SIZE];
    }
    
    // Methods for getting the index of a node's left child, right child, or parent
    protected int getLeftIndex(int index) {return 2 * index + 1;}
    protected int getRightIndex(int index) {return 2 * index + 2;}
    protected int getParentIndex(int index) {return (index - 1) /2; }

    // Methods for getting the data stored at some index in the heap
    protected int getLeftData(int index) {return data[getLeftIndex(index)];}
    protected int getRightData(int index) {return data[getRightIndex(index)];}
    protected int getParentData(int index) {return data[getParentIndex(index)];}


    // Methods for checking if a node has a left child, right child, or parent
    protected boolean hasLeft(int index) {return getLeftIndex(index) < size;}
    protected boolean hasRight(int index) {return getRightIndex(index) < size;}
    protected boolean hasParent(int index) {return getParentIndex(index) >= 0;}


    // Checks if the heap is empty/full
    public boolean isEmpty() { return size == 0;}
    public boolean isFull() { return size == MAX_SIZE;}


    /**
     * Returns the String representation of the heap
     * @return          the heap as a String
     */
    public String toString() {
        String s = "";
        for (int i = 0; i < size; i++)
        {
            s += data[i] + " ";
        }
        return s.trim();
    }
    
    /**
     * Swap the data stored at two different indices in the heap
     * @param           index0 - the index whose data will be swapped with the data at index1
     * @param           index1 - the index whose data will be swapped with the data at index0
     */
    public void swap(int index0, int index1) {
        // Stores the value at index 0 into a temp variable
        int tempValue = data[index0];
        // Sets the value at index 0 to its new value
        data[index0] = data[index1];
        // Sets the value at index 1 to the value originally at index 0
        data[index1] = tempValue;
    }
    
    /**
     * Adds a new node to the heap
     * @param           element - the data to add to the heap
     */
    public void add(int element) {
        // Make sure list isn't full
        if (isFull())
        {
            return;
        }
       
        // Add element to the end of list
        data[size] = element;
        // Increase number of nodes in  list
        size++;

        // Since we added it to the end, we need to position it correctly within
        // the list. We need to call our maxHeapifyUp function because it starts
        // with the end node and positions it
        maxHeapifyUp();
    }

    /**
     * Removes and returns the data stored at the root (index 0)
     * @return          the data stored at the root
     */
    public int getMax() {
        // Make sure list isn't empty
        if (isEmpty())
        {
            // If it is, return -1 because we have no elements
            return -1;
        }

        // Get the element at root node before we remove it
        int max = data[0];
        // Get the end of the list
        int end = size - 1;
        // Swap end with the root node
        swap(end, 0);
        // Decrease the size to 'get rid' of the last leaf node
        size--;

        // We then need to position the new root node
        // Have to call maxHeapifyDown because it starts
        // at the root node
        maxHeapifyDown();

        // We still need to return the max item, which is the first element in list
        return max;
    }
    
    /**
     * Restores the heap property by repeatedly swapping the last leaf node up the heap until properly positioned
     */
    public void maxHeapifyUp() {
        // Get the location of the last 'leaf node'
        int end = size - 1;

        // While the data at our end is greater than its parent node
        while(hasParent(end) && data[end] > data[getParentIndex(end)])
        {
                // Swap it with the parent node
                swap(getParentIndex(end), end);
                // and now update the 'end' of our sorted stuff to the parent node that we just
                // swapped
                end = getParentIndex(end);
        }
        
        
    }
    
    /**
     * Restores the heap property by repeatedly swapping the root node down the heap until properly positioned
     */
    public void maxHeapifyDown() {


        // Set the temp max to the root node index
        int maxIndex = 0;

        // Runs while the root node has a greater child node
        while (hasLeft(maxIndex) && data[maxIndex] < getLeftData(maxIndex) || hasRight(maxIndex) && data[maxIndex] < getRightData(maxIndex))
        {
            int leftIndex = getLeftIndex(maxIndex);
            int rightIndex = getRightIndex(maxIndex);

            // If it only has a right child
            if (hasRight(maxIndex) && !hasLeft(maxIndex))
            {
                // It must be greater, so we need to swap
                swap(rightIndex, maxIndex);
                // Max index is now on the right
                maxIndex = rightIndex;
            }

            // If it only has a left child
            else if (hasLeft(maxIndex) && !hasRight(maxIndex))
            {
                // It must be greater, so we need to swap
                swap(leftIndex, maxIndex);
                // Max index is now on the left
                maxIndex = leftIndex;
            }

            // Otherwise, it has both children
            else
            {
                // Get data on each side
                int rightData = getRightData(maxIndex);
                int leftData = getLeftData(maxIndex);

                // If the data on the left is greater than data on right
                if (leftData > rightData)
                {
                    //We need to swap 
                    swap(leftIndex, maxIndex);
                    // Update max to left
                    maxIndex = leftIndex;
                }

                // If data on right is greater
                if (rightData > leftData)
                {
                    // We need to swap
                    swap(rightIndex, maxIndex);
                    // Update max to right
                    maxIndex = rightIndex;
                }

            }
        }
    }
}

