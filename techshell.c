///////////////////////////////////////////
// Name: Rylie Malbrough                 //
// Class: CSC 222                        //
// Date: 2/22/2024                       //
///////////////////////////////////////////

///////////// LIBRARIES ///////////////////
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <errno.h>

/////////// PROTOTYPES ////////////////////
struct ShellCommand ParseCommandLine(char* input); 
char* commandPrompt();
void ExecuteCommand(struct ShellCommand command);

///////////// STRUCTURES /////////////////
struct ShellCommand
{
    char commandName[50];
    char *arguments[100];
    int numArguments;
};

///////////// FUNCTIONS //////////////////

// Displays current working directory and returns user input
char* commandPrompt()
{
    // wd stores the working directory name
    char wd[1024]; 

    // stores user input in an array of characters
    char *userInput = malloc(1024 * sizeof(char));
    
    // getcwd gets the name of the current working directory
    if (getcwd(wd, sizeof(wd)) != NULL)
    {
        // As long as there is a cwd, print it out
        printf("%s$ ", wd);
    }
    // print appropriate error if unable to find cwd
    else fprintf(stderr, "Unable to get directory");

    fflush(stdout);

    // Get user input from command line and make sure it's not NULL
    if (fgets(userInput, 1024, stdin) == NULL)
    {
        // print appropriate error if unable to read from stdin
        perror("Unable to get user input (fgets failure)");
        exit(EXIT_FAILURE);
    }

    // Remove newline
    userInput[strcspn(userInput,"\n")] = 0;

    return userInput;
} 

// Process user input as a shell command
struct ShellCommand ParseCommandLine(char* input)
{
    // Stores the command(s)
    struct ShellCommand command;

    // We are starting with zero arguments
    command.numArguments = 0;

    // Tokenize input based on spaces
    char* token = strtok(input, " ");

    // set the name of the command as the first token
    strcpy(command.commandName, token);

    // Continue tokenizing
    int i = 0;
    while ((token = strtok(NULL, " ")) != NULL)    
    {
        // allocating memory for command ("token") in array
        command.arguments[i] = malloc(strlen(token) + 1);

        // copying command to array
        strcpy(command.arguments[i], token);

        // Increase number of arguments
        command.numArguments++;
        // Increment i to move onto the next command ("token")
        i++;
    }
    // null terminate arguments so that it can be passed into execvp function
    command.arguments[i] = NULL;
    return command;

}

// Execute a shell command
void ExecuteCommand(struct ShellCommand command)
{
    // simply error-checking, makes sure there are arguments to work with
    if (command.arguments == NULL)
    {
        perror("No valid commands");
        return;
    }
     
    // Must account for cd, pwd, & exit command because they modify the state of the 
    // parent process, not child 
    if(strcmp(command.commandName, "cd")== 0)
    {
        // Checks if the user is using cd with a directory in mind
        if (command.numArguments > 0)
        {
            // Runs the chdir command with the user's argument 
            if (chdir(command.arguments[0]) != 0)
            {
                // Using errno to specify a permission error
                if (errno == EACCES)
                    fprintf(stderr, "Permission denied\n");
                // Otherwise, assuming it is an unkown directory
                else fprintf(stderr, "Unknown directory\n");
            }
        }
        // If the number of arguments is less than zero, the user
        // is using cd without a directory in mind
        else 
        {
            // Just return the home environment variable
            chdir(getenv("HOME"));
        }

        // return to main function because we don't want to execute within the child
        return;
    }

    // Checking if the user wants to print their working directory
    if(strcmp(command.commandName, "pwd")== 0)
    {
        // create an array of chars to hold directory
        char cwd[1024];
        // Print out the cwd using getcwd
        printf("%s\n", getcwd(cwd, 1024));
        // return to main function because we don't want to execute within the child
        return;
    }
    
    // Checking if user wants to exit
    if(strcmp(command.commandName, "exit")== 0)
    {
        // Exit
        exit(EXIT_SUCCESS);
    }

    // Fork into a child process
    pid_t pid = fork();

    // Error-checking
    if (pid == -1)
    {
        perror("FORK FAILED!");
        exit(EXIT_FAILURE);
    }

    // Child process that executes the command
    else if (pid == 0)
    {
        // Loop through all of the command arguments
        for (int i = 0; i < command.numArguments; i++)
        {
            // Checking if the user used file directions
            if(strcmp(command.arguments[i], "<") == 0 && i < command.numArguments - 1)
            {   
                // Opening file to the right of the direction argument for reading
                FILE* infile = fopen(command.arguments[i+1], "r");
            
                // Making sure file is valid
                if (infile == NULL)
                {
                    // Otherwise exit
                    perror("Error opening file");
                    exit(EXIT_FAILURE);
                }
            
                // Duplicating file so input is redirected to file
                dup2(fileno(infile), STDIN_FILENO);
                // close file
                fclose(infile);

                // make the redirection argument and file NULL
                // we don't want to execute these within the parent
                command.arguments[i] = NULL;
                command.arguments[i + 1] = NULL;

                // increment i to move along in the array
                i++;
            }

             // Checking if the user used file directions
            else if(strcmp(command.arguments[i], ">") == 0)
            {
                FILE* outfile = fopen(command.arguments[i+1], "w");

                if (outfile == NULL)
                {
                    perror("Error opening file");
                    exit(EXIT_FAILURE);
                }

                dup2(fileno(outfile), STDOUT_FILENO);
                fclose(outfile);
                
                command.arguments[i] = NULL;
                command.arguments[i+1] = NULL;
                i++;
            }
        }

        // Creating a new array to hold the command + its arguments
        // Using malloc to allocate the memory
        char** args = malloc((command.numArguments + 2) * sizeof(char*));
        args[0] = command.commandName; // First argument is the command name

        // Copy arguments from parameter into new array
        for (int i = 0; i < command.numArguments; i++)
        {
            args[i + 1] = command.arguments[i];
        }

        // null terminate end for execvp function
        args[command.numArguments + 1] = NULL;

        // run execvp function
        execvp(args[0], args);
        perror("Error executing command");
        exit(EXIT_FAILURE);
        return;    
    }

    else
    {
        // wait on child to finish executing
        int status;
        waitpid(pid, &status, 0);
    }
}

///////// MAIN /////////////////////////////////
int main() {
    char* input;
    struct ShellCommand command;

    // Repeatedly prompt user for input
    for(;;)
    {
        // get user input
        input = commandPrompt();

        // turn user input into shell command
        command = ParseCommandLine(input);

        // Execute command
        ExecuteCommand(command);

    }

    exit(0);

}





