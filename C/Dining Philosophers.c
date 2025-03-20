// Name: Rylie Malbrough
// Assignment: HW3-Dining Philosopher's Problem
// Supplemental Resources: https://www.geeksforgeeks.org/dining-philosopher-problem-using-semaphores/
//                         https://chat.openai.com/ 
//                         https://www.geeksforgeeks.org/use-posix-semaphores-c/    
//                         https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html                     

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

// definitions for philosopher's states
#define EATING 2
#define HUNGRY 1
#define THINKING 0

int numOfPhils; // number of phils, passed in as argument[1]
int numOfTimesToEat; // number of times to eat each, passed in as argument[2]
sem_t *chopsticks; // semaphore used to represent chopsticks
int *state; // represents state of philosopher
int *phils; 
int *meals; // individual philosophers' meal count

// puts chopsticks back down (denotes when philosopher is thinking)
void putDownChopstick(int phil)
{
    // once the philosopher puts down the chopsticks, he can no longer eat
    // enter a THINKING state
    state[phil] = THINKING;

    // print out state
    printf("Philosopher %d is THINKING. . .\n", phil);
    // simulate thinking
    sleep(2);
}

// used to check state of philosopher and state of each chopstick
void test(int phil) 
{
    int left_phil = (phil == 0) ? numOfPhils - 1 : phil - 1;    // 4-29-24 ChatGPT : "Am I accessing the philosopher indexes correctly: phil - 1 for the left?"
    int right_phil = (phil == numOfPhils - 1) ? 0 : phil + 1;   // Gave me this code snippet to make sure my indexes didn't go out of bounds 

    // if philosopher is hungry and both left and right are satisifed
    if (state[phil] == HUNGRY && state[left_phil] != EATING && state[right_phil] != EATING)
    {
        // then they should be able to eat now
        state[phil] = EATING;

        // print out state
        printf("Philosopher %d is EATING. . .\n", phil);
        // simulate eating
        sleep(2);
    
        // once the philosopher is done eating, he no longer needs the chopsticks
        // call putDownChopstick to release the semaphores and change state
        putDownChopstick(phil);

        // release the semaphores of the chopsticks around the philosopher
        sem_post(&chopsticks[phil]);
        // chopstick to the left, makes sure index wraps around circularly
        sem_post(&chopsticks[(phil + 1) % numOfPhils]);

    }  
} 
             
// waits to grab chopsticks for philosopher (denotes when philospher is hungry)
void pickupChopstick(int phil)
{
    // wait for right and left chopsticks to become available
    sem_wait(&chopsticks[phil]);
    sem_wait(&chopsticks[(phil + 1) % numOfPhils]);

    // set philosopher's state to HUNGRY (1)
    state[phil] = HUNGRY;

    // print out state
    printf("Philosopher %d is HUNGRY. . .\n", phil);
    // simulate being hungry
    sleep(2);

    // test if philosopher can eat, logic is taken care of in the test function
    test(phil);
}

// denotes when a philosopher is originally thinking and then becomes hungry
void getHungry(int phil)
{
    // print out state
    printf("Philosopher %d is THINKING. . .\n", phil);

    // simulate thinking
    sleep(2);

    // change state to hungry
    state[phil] = HUNGRY;
}

// must be a pointer when working with threading
// determines first action of a philospher when thread is created
void *philosopher(void *arg) 
{
    // get the philosopher number by dereferencing the argument pointer passed in
    // 4-29-24 ChatGPT : "How do I cast a pointer to an integer?"
    int phil = *((int*)arg);

    while(meals[phil] < numOfTimesToEat)
    {
        // if the first state of the philosopher gets set to thinking
        // call the get hungry function so they don't think indefinitely
        if(state[phil] == THINKING)
        {
            getHungry(phil);
        }

        // if the philosopher is hungry, try picking up a chopstick 
        if(state[phil] == HUNGRY)
        {
            // try eating
            pickupChopstick(phil);

            // after eating, put down the chopstick
            putDownChopstick(phil);

            // increase number of times each individual philosopher has eaten
            // 5-2-2024 "How do I ensure each philosopher eats the stated number of times?"
            // ChatGPT recommended making a meal array whose index matches an individual phil
            // originally just had an integer, but the first phil was eating one less than other phils
            meals[phil]++;

            // if the meals of invidual phil exceeds numoftimestoeat, immediately exit loop and move on
            if (meals[phil] == numOfTimesToEat)
            {
                break;
            }
        }
    }
}
                    
int main(int argc, char *argv[]) {

    // Assigning arguments to variables
    // casting to integer
    numOfPhils = atoi(argv[1]);
    numOfTimesToEat = atoi(argv[2]);

    // hold thread identifiers
    pthread_t threads[numOfPhils];

    // memory allocation for chopsticks, state, and philosphers
    chopsticks = malloc(numOfPhils * sizeof(sem_t));
    state = malloc(numOfPhils * sizeof(int));
    phils = malloc(numOfPhils * sizeof(int));
    meals = malloc(numOfPhils * sizeof(int));

    // initialize semaphores and
    // create chopsticks for each phil
    // create meal amount for each phil as well, initialized at zero
    // initialize a random state as well
    for (int i = 0; i < numOfPhils; i++) 
    {
        sem_init(&chopsticks[i], 0, 1); // Initialize each semaphore with an initial value of 1
        meals[i] = 0;

        // return a random value between 0 and 1 for thinking or hungry
        state[i] = rand() % 2;
    }   

    // create philosphers and give them a state based on numOfPhils
    for(int i=0; i < numOfPhils; i++)
    {
        // philosopher ids
        phils[i] = i;
        pthread_create(&threads[i], NULL, philosopher, &phils[i]);
    }

    // wait for each thread to finish
    for(int i=0; i < numOfPhils; i++)
    {
        pthread_join(threads[i], NULL);
    }

    // destroy semaphores
    for(int i=0; i < numOfPhils; i++)
    {
        sem_destroy(&chopsticks[i]);
    }

    // free allocated memory
    free(chopsticks);
    free(state);
    free(phils);
    free(meals);
    return 0;
}
