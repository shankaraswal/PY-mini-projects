import tkinter as tk
from tkinter import messagebox

# Define all possible winning combinations by indices on the 3x3 grid (rows, cols, diagonals)
match_comb = [
    [0,1,2],  # Top row
    [3,4,5],  # Middle row
    [6,7,8],  # Bottom row
    [0,3,6],  # Left column
    [1,4,7],  # Middle column
    [2,5,8],  # Right column
    [0,4,8],  # Diagonal from top-left to bottom-right
    [2,4,6],  # Diagonal from top-right to bottom-left
]

def button_click(index):
    """
    This function is called when a button (cell) is clicked.
    It:
    - Updates the button text to current player's symbol if empty and game ongoing.
    - Updates the UI immediately so the player sees their move.
    - Checks for a winner.
    - If no winner, switches to the next player.
    - Checks if the game is a draw.
    """
    global winner
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player  # Set button text to 'X' or 'O'
        root.update()  # Refresh UI immediately so change is visible
        
        check_winner()  # Check if this move causes a win
        if not winner:
            toggle_player()  # Switch turns
            check_draw()     # Check if board is full without a winner

def check_winner():
    """
    Checks all defined winning combinations (match_comb).
    If a winning combination is found:
    - Sets the winner flag True.
    - Highlights the winning buttons with green background.
    - Immediately refreshes the UI to show colors.
    - Displays a message box announcing the winner.
    - Ends the game main loop.
    """
    global winner
    for mc in match_comb:
        if buttons[mc[0]]['text'] == buttons[mc[1]]['text'] == buttons[mc[2]]['text'] != "":
            winner = True  # Mark game as finished
            buttons[mc[0]].config(bg="green")  
            buttons[mc[1]].config(bg="green")  
            buttons[mc[2]].config(bg="green")
            root.update()  # Refresh UI to apply color change immediately
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[mc[0]]['text']} won!")  # Show winner alert
            root.quit()  # End the game

def check_draw():
    """
    Checks if all buttons are filled (no empty spots) and no winner yet.
    If so:
    - Updates the UI immediately.
    - Shows a message box declaring the game a draw.
    - Ends the game.
    """
    if all(button['text'] != "" for button in buttons):
        root.update()  # Refresh UI before showing message
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        root.quit()

def toggle_player():
    """
    Switches the current player from 'X' to 'O' or vice versa.
    Updates the label on the UI to indicate whose turn it is.
    """
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Create the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create 9 buttons for the Tic Tac Toe board (3x3 grid)
# Using a list comprehension to create buttons with empty text and a large font
# Each button calls button_click with its index when clicked
buttons = [tk.Button(root, text="", font=('bold', 50), width=4, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

# Place the buttons in a 3x3 grid layout using grid manager
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initial player is X
current_player = "X"
# Winner flag to track if game ended
winner = False

# Label below the grid showing which player's turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn now", font=("bold", 25))
label.grid(row=3, column=0, columnspan=3)


# Start the Tkinter event loop to run the game
root.mainloop()