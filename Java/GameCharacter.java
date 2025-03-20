// Name: Rylie Malbrough
// Date: April 15, 2023
// Program: Program Five Game Character

public class GameCharacter {
    // Instance variable for name
    private String name;
    private int lives;

    // Instance variable for inventory; array of strings
    private String[] inventory;

    // Instance variable for a constant MAXLIVES
    private final int MAXLIVES = 5;

    // Default constructor
    public GameCharacter() {
        name = "Sam Sung";
        lives = MAXLIVES;
        inventory = new String[5];  // Intializes a new array for the inventory
        // Inventory has no accessor/mutator as it's an array and will not change
    }

    // Overloaded constructor that takes parameters for the name and lives
    public GameCharacter(String name, int lives) {
        // sets the instance variables equal to the parameter
        this.name = name;

        if (lives >= 0 && lives <= MAXLIVES) this.lives = lives;
        else this.lives = 5;

        // Default constructor inventory
        inventory = new String[5];
    }

    // Accessor for name, returns the name
    public String getName() {
        return name;
    }

    // Mutator for name, returns nothing but sets the name equal to parameter
    public void setName(String name) {
        this.name = name;
    }

    // Accessor for lives, returns the amount of lives as an integer
    public int getLives() {
        return lives;
    }

    // Mutator for lives, makes sure that the integer is between 0 and MAXLIVES defined as a constant above
    public void setLives(int lives) {
        if (lives >= 0 && lives <= MAXLIVES){
            this.lives = lives;
        }
        else{
            this.lives = 5;
        }
    }

    // Accessor for inventory
    public String[] getInventory(){
        return inventory;
    }

    // Mutator for inventory
    public void setInventory(String[] inventory){
        this.inventory = inventory;
    }

    // Tells whether or not a character is alive using a boolean
    public boolean isAlive() {
        if (lives > 0) return true;    // If a character's lives are greater than zero they are still alive
        else return false;
    }

    // Tells whether or not a character has a 'gun' or 'knife' in their inventory
    public boolean hasWeapon() {
        // For each loop that goes through each item in the inventory array
        for (String item : inventory) {
            // If the item is a knife OR a gun, return true
            if ("knife".equals(item) || "gun".equals(item)) {
                return true;
            }
        }
        return false;
    }

    // Returns the amount of valid items a player has in their inventory
    public int sizeOfInventory() {
        // set the count to zero 
        int count = 0;

        // For each loop that goes through each item in the inventory array 
        for (String item : inventory) {
            // If the item in the inventory is not null
            if (item != null) {
                // increase the count of items in inventory
                count++;
            }
        }
        return count;
    }

    // Sets a player's lives to maximum amount
    public void heal() {
        lives = MAXLIVES;
    }

    // Reduces lives of character by 1 if character is alive
    public void damage() {
        // Checks if player is alive
        if (isAlive()) {
            --lives;
        }
    }

    // Adds an item to the inventory if there is space for it, takes the item as the parameter
    public void pickUp(String item) {
        // For loop that goes through the length of the inventory
        for (int i = 0; i < inventory.length; i++) {
            // If there is nothing in the inventory (it's null)
            if (inventory[i] == null) {
                // then add the item at the index i to the inventory
                inventory[i] = item;
                break;
            }
        }
     }

    // Gets rid of an item in the inventory, takes the item as the parameter
    public void drop(String item) {
        // For loop that goes through length of inventory
        for (int i = 0; i < inventory.length; i++) {
            // If the item parameter equals the item in the inventory at index i
            if (item.equals(inventory[i])) {
                // Replace item at index i with null
                inventory[i] = null;
                break;
            }
        }
    }

    // String function that creates the string representation of the Game Character object
    public String toString() {

        // Stringbuilder class allows you to build a string array 
        // Start by instantiating the stringBuilder object
        StringBuilder stringBuilder = new StringBuilder();

        // Append the name, lives, and inventory title to stringbuilder
        stringBuilder.append("Name:" + name + "\n");
        stringBuilder.append("Lives: " + lives + "\n");
        stringBuilder.append("Inventory: ");

        // Adds the comma before the item only if its not first item
        boolean first = true;

        // Goes through the items in the inventory
        for (String item : inventory){
            // If the item is not null (i.e. the item exists)
            if (item != null){
                //if not first, add a comma before
                if (!first){
                    stringBuilder.append(", ");
                }

                // then append the item to the stringbuilder
                stringBuilder.append(item);
                first = false;
            }

        }

        stringBuilder.append("\n");
        return stringBuilder.toString();

        
    }
}
