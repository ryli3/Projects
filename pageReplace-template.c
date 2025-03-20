/*
Names: Rylie Malbrough & Robert Newman
Date: 5/14/2024
Description: Homework #4
*/

// libraries for program
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

// define variables
#define MAX_PAGE_REFERENCE_LENGTH 100
#define MAX_PAGE_NUMBER 9
#define DEBUG 0

// to keep track of number of frames
int numOfFrames;

// declarations for functions
int FIFO(int frames, int pages[]);
int LRU(int frames, int pages[]);
int OPT(int frames, int pages[]);
int search(int pages[], int startIndex, int value);
int getMaxIndex(int numbers[], int size);
int getMinIndex(int numbers[], int size, int pageTable[]);

// FIFO algorithms for page faults
int FIFO(int frames, int pages[])
{
    // keep track of page faults
    int pageFaults = 0;

    // keep track of table index
    int pageTableindex = 0;

    // setting an empty table of Arrays according to parameter of given frames by user input
    int tableArray[frames];

    // setting all values of the array to -1
    for (int i = 0; i < frames; i++)
    {
        tableArray[i] = -1;
    }
    
    // actual algorithm of FIFO
    for (int i = 0; i < 100; i++)
        {
            // setting found = 0 as a case if not found
            int found = 0;

            for(int j = 0; j < frames; j++)
            {   
                // checking if table array is equal to page array at a given index
                if (tableArray[j] == pages[i])
                {   
                    // setting found to '1' indicating that it was found
                    found = 1;
                    break; 
                }
            }
            // if not found this runs
            if (found == 0)
            {   
                // setting the the given number of index to the tableArray because there wasn't a duplicate in array
                tableArray[pageTableindex] = pages[i];
                pageTableindex = (pageTableindex + 1) % frames;

                // incrementing this variable to indicate that page fault has happened
                pageFaults++;
            }
        }
    // return value of pagefaults given by FIFO algorithm
    return pageFaults;
}

// LRU algorithms for page faults
int LRU(int frames, int pages[])
{
    // keep track of page faults
    int pageFaults = 0;

    // keep track of pages
    int pageCount = 0;

    // setting an empty table of Arrays according to parameter of given frames by user input
    int tableArray[frames];

    // making a record reference
    int pagesRecord[MAX_PAGE_NUMBER] = {-1};

    // setting all values of table array to -1
    for (int i = 0; i < frames; i++)
    {
        tableArray[i] = -1;
    }

    while(pageCount < 100)
    {
        // setting found = 0 as a default value bc nothing is found yet
        int found = 0;
        for (int i = 0; i < frames; i++)
        {
            if (tableArray[i] == pages[pageCount])
            {
               // value was found and will be replaced
               found = 1; 
               pagesRecord[i] = pageCount;
               break; 
            }
        }

        // will run if given value is not found
        if (found == 0)
        {   
            // replace given value 
            int replaceIndex = getMinIndex(pagesRecord, frames, tableArray);
            tableArray[replaceIndex] = pages[pageCount];
            
            // since replace was made.... must increment
            pageFaults++; 
        }  

        for (int i = 0; i < frames; i++)
        {
            // checking if value is found
            if (tableArray[i] == pages[pageCount])
            {   
                // value is found must replace
                pagesRecord[i] = pageCount;
            }
        }
        // increment 
        pageCount++;
    }

    return pageFaults;
}

int OPT(int frames, int pages[])
{   
    int pageFaults = 0;
    int pageCount = 0;
    int tableArray[frames];
    int pageIndexes[frames];

    for (int i = 0; i < frames; i++)
    {
        tableArray[i] = -1;
    }

    while(pageCount < 100)
    {
        int found = 0;
        for (int i = 0; i < frames; i++)
        {
            if (tableArray[i] == pages[pageCount])
            {
               found = 1; 
               break; 
            }
        }

        // will run if not found in page
        if (found == 0)
        { 
            for (int i = 0; i < frames; i++)
            {
                // function call to find value at given 'i' index
                pageIndexes[i] = search(pages, pageCount, tableArray[i]);
            }

            // making appropiate changes to new values
            int replaceIndex = getMaxIndex(pageIndexes, sizeof(pageIndexes)/sizeof(pageIndexes[0]));
            tableArray[replaceIndex] = pages[pageCount];

            // since change was made... must increment page fault
            pageFaults++;

        }

        pageCount++;
    }
    
    return pageFaults;
}

// helper function to search for a specific value in given page at current time
int search(int pages[], int startIndex, int value)
{
    for (int i = startIndex; i < 100; i++)
    {
        if(pages[i] == value)
        {
            return i;
        }
    }
    return 100;
}

// helper function to find max_index
int getMaxIndex(int numbers[], int size)
{
    int MAX = numbers[0];
    int MAXindex = 0;

    for (int i = 1; i < size; i++)
    {
        if (numbers[i] > MAX && numbers[i] >= 0)
        {
            MAX = numbers[i];
            MAXindex = i;
        }
    }

    return MAXindex;
}

// helper function to find min_index
int getMinIndex(int numbers[], int size, int pageTable[])
{
    int MIN = numbers[0];
    int MINindex = 0;

    for (int i = 1; i < size; i++)
    {
        if (pageTable[i] == -1)
        {
            return i;
        }
        else if (numbers[i] < MIN)
        {
            MIN = numbers[i];
            MINindex = i;
        }
    }
    return MINindex;
}

int main(int argc, char *argv[]) {
    // default test pages
    int testPages[] = {8,3,8,7,4,7,8,2,9,0,3,2,6,3,8,1,3,7,3,5,1,1,8,9,7,0,9,6,6,8,8,4,4,9,1,0,7,3,8,0,5,8,8,4,4,4,4,8,4,5,9,9,5,1,4,3,0,8,0,0,7,1,2,3,8,3,4,9,4,1,6,8,2,8,1,6,6,9,2,2,0,3,6,6,5,1,3,0,8,7,6,1,9,1,6,6,1,3,7,0};
    
    // error checking
    if (argc == 1)
    {
        printf("Incorrect usage");
        return 1;
    }
    
    // case with default test pages
    else if (argc == 2)
    {
        // parameter one
        int numOfFrames = atoi(argv[1]);

        // calling alg functions
        int FIFOpagefaults = FIFO(numOfFrames, testPages);
        int LRUpagefaults = LRU(numOfFrames, testPages);
        int OPTpagefaults = OPT(numOfFrames, testPages);
    
        //print statements to indicate the specific alg and its number of faults
        printf("Algorithm\t# Page Faults\n");
        printf("FIFO\t\t");
        printf("%d\n", FIFOpagefaults);
        printf("LRU\t\t");
        printf("%d\n", LRUpagefaults);
        printf("OPT\t\t");
        printf("%d\n", OPTpagefaults);
    }
    
    // case where test pages is generated with seed generator
    else if (argc == 3)
    {   
        // parameter one
        int frames = atoi(argv[1]);

        // parameter two
        int seed = atoi(argv[2]);

        srand(seed);
        int referenceString[MAX_PAGE_REFERENCE_LENGTH];
        
        // generating seed test pages
        for (int i = 0; i < MAX_PAGE_REFERENCE_LENGTH; i++)
        {
            referenceString[i] = (rand() % 10);
        }

        // set to true to show seed generated testpage
        if(DEBUG)
        {
            for(int i = 0; i < MAX_PAGE_REFERENCE_LENGTH; i++)
            {
                printf("%d, ", referenceString[i]);
            }
        }

        // calling alg functions
        int FIFOpagefaults = FIFO(frames, referenceString);
        int LRUpagefaults = LRU(frames, referenceString);
        int OPTpagefaults = OPT(frames, referenceString);
    
        //print statements to indicate the specific alg and its number of faults
        printf("Algorithm\t# Page Faults\n");
        printf("FIFO\t\t");
        printf("%d\n", FIFOpagefaults);
        printf("LRU\t\t");
        printf("%d\n", LRUpagefaults);
        printf("OPT\t\t");
        printf("%d\n", OPTpagefaults);
    }

    return 0;
}