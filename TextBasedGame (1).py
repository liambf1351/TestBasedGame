# TextBasedGame.py
# Author: Liam Farrell
# Haunted High School Escape - Final Project for IT 140

# Show the game instructions
def show_instructions():
    print("Haunted High School Escape")
    print("Collect 6 sacred artifacts to escape the haunted school.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type your commands carefully. Beware of the ghost...")

# Show the player's current status
def show_status(current_room, inventory, rooms):
    print("\n---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)
    item = rooms[current_room].get('item', '')
    if item and item != 'Ghost':
        print("You see a", item)
    print("---------------------------")

# Main game logic
def main():
    # Room dictionary with connections and items
    rooms = {
        'Main Entrance': {'North': 'Library', 'South': 'Cafeteria', 'East': 'Science Lab', 'West': 'Gymnasium'},
        'Library': {'South': 'Main Entrance', 'item': 'Ancient Book'},
        'Science Lab': {'West': 'Main Entrance', 'item': 'Beaker of Ghost Mist'},
        'Gymnasium': {'East': 'Main Entrance', 'item': 'Sacred Whistle'},
        'Cafeteria': {'North': 'Main Entrance', 'item': 'Silver Spoon'},
        'Art Room': {'East': 'Auditorium', 'item': 'Paintbrush of Light'},
        'Auditorium': {'West': 'Art Room', 'North': "Principal's Office", 'item': 'Echoing Bell'},
        "Principal's Office": {'South': 'Auditorium', 'item': 'Ghost'}  # Villain room
    }

    # Initial state
    current_room = 'Main Entrance'
    inventory = []

    # Add access to Art Room from Gym and Science Lab
    rooms['Gymnasium']['South'] = 'Art Room'
    rooms['Science Lab']['South'] = 'Art Room'
    rooms['Art Room']['North'] = 'Gymnasium'
    rooms['Art Room']['West'] = 'Science Lab'

    show_instructions()

    # Game loop
    while True:
        show_status(current_room, inventory, rooms)

        # Player input
        move = input("Enter your move: ").strip()

        # Handle movement
        if move.lower().startswith('go '):
            direction = move[3:].capitalize()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Check for losing condition
                if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Ghost':
                    print("\nYou entered the Principal's Office without all artifacts...")
                    print("Your soul is mine now...forever....GAME OVER!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break

                # Check for winning condition
                if current_room == "Principal's Office" and len(inventory) == 6:
                    print("\nYou step into the Principal's Office, all artifacts in hand.")
                    print("You use the Ancient Book to speak the ghost's name.")
                    print("The ghost fades... You WIN!")
                    print("Congratulations! You escaped the Haunted High School.")
                    break
            else:
                print("You can't go that way.")

        # Handle getting item
        elif move.lower().startswith('get '):
            item_requested = move[4:].strip()
            item_in_room = rooms[current_room].get('item', '')

            if item_in_room.lower() == item_requested.lower() and item_requested not in inventory:
                inventory.append(item_requested)
                del rooms[current_room]['item']
                print(item_requested + " retrieved!")
            else:
                print("Can't get " + item_requested + ".")

        else:
            print("Invalid command. Try 'go [direction]' or 'get [item]'.")

# Run the game
if __name__ == "__main__":
    main()
