"""
Breakout #1 – Personalized Greeting Form
Author: [Team Five]
Date: June 2, 2025

Description:
This program creates an interactive GUI application that accepts a user's name
and displays a personalized greeting. It demonstrates the relationship between
Entry widgets, StringVar, and event-driven functions in Tkinter.

Requirements Implemented:
1. Prompt Label - instructs user to enter their name
2. Entry Field - where user types their name
3. Greeting Label - displays personalized greeting
4. Button - triggers the greeting function
5. Bonus: Clears entry field after greeting
6. Bonus: Default greeting when input is blank
"""

# Import required modules
import tkinter as tk
from tkinter import ttk  # ttk provides themed widgets for better appearance

# ====================================================================
# MAIN APPLICATION SETUP
# ====================================================================

def create_personalized_greeting_app():
    """
    Creates and configures the main application window for the personalized
    greeting form. This function sets up the window properties and title.
    
    Returns:
        tk.Tk: The main application window object
    """
    # Create the main application window
    root = tk.Tk()
    
    # Set the window title (appears in the title bar)
    root.title("Personalized Greeting Form - Breakout #1")
    
    # Set the window size (width x height in pixels)
    root.geometry("400x300")
    
    # Optional: Make the window non-resizable for consistent layout
    root.resizable(False, False)
    
    # Optional: Center the window on screen (bonus enhancement)
    root.eval('tk::PlaceWindow . center')
    
    return root


# ====================================================================
# STRING VARIABLES FOR DATA BINDING
# ====================================================================

def setup_string_variables():
    """
    Creates StringVar objects that will be used to bind data between
    the GUI widgets and our application logic. StringVar provides
    automatic updating of widget content when the variable changes.
    
    Returns:
        tuple: (name_var, greeting_var) - The StringVar objects for
               user input and greeting display
    """
    # StringVar for storing the user's name input
    # This automatically syncs with the Entry widget
    name_var = tk.StringVar()
    
    # StringVar for storing the greeting message
    # This automatically syncs with the greeting Label
    # Set default greeting message as per bonus requirement
    greeting_var = tk.StringVar(value="Hello, friend!")
    
    return name_var, greeting_var


# ====================================================================
# EVENT HANDLER FUNCTIONS
# ====================================================================

def create_greet_function(name_var, greeting_var):
    """
    Creates the greet function that will be called when the user clicks
    the "Greet Me" button. This function demonstrates event-driven programming.
    
    Args:
        name_var (tk.StringVar): Variable containing the user's input
        greeting_var (tk.StringVar): Variable for displaying the greeting
    
    Returns:
        function: The greet function to be used as button command
    """
    def greet():
        """
        Event handler function that processes user input and updates the greeting.
        This function is called when the "Greet Me" button is clicked.
        
        Algorithm:
        1. Get the user's name from the entry field
        2. Check if name is provided (not empty or just whitespace)
        3. Create personalized greeting or use default
        4. Update the greeting label
        5. Clear the entry field (bonus feature)
        """
        # Get the current value from the name entry field
        # .strip() removes leading/trailing whitespace
        user_name = name_var.get().strip()
        
        # Check if the user provided a name
        if user_name:
            # Create personalized greeting with the user's name
            personalized_message = f"Hello, {user_name}!"
            greeting_var.set(personalized_message)
            
            # Print to console for debugging (can be removed in production)
            print(f"Greeting created for: {user_name}")
        else:
            # Use default greeting when no name is provided (bonus feature)
            greeting_var.set("Hello, friend!")
            print("Default greeting used - no name provided")
        
        # Clear the entry field after greeting (bonus feature)
        # This makes the form ready for the next input
        name_var.set("")
    
    return greet


# ====================================================================
# GUI WIDGET CREATION AND LAYOUT
# ====================================================================

def create_widgets(root, name_var, greeting_var, greet_function):
    """
    Creates and arranges all the GUI widgets according to the requirements.
    Uses the pack geometry manager for simple vertical layout.
    
    Args:
        root (tk.Tk): The main application window
        name_var (tk.StringVar): Variable for user name input
        greeting_var (tk.StringVar): Variable for greeting display
        greet_function (function): Function to call when button is clicked
    """
    
    # ----------------------------------------------------------------
    # 1. PROMPT LABEL (Requirement #1)
    # ----------------------------------------------------------------
    prompt_label = ttk.Label(
        root, 
        text="Enter your name:",
        font=("Arial", 12, "bold")  # Make it visually prominent
    )
    prompt_label.pack(pady=(20, 10))  # Add padding: 20px top, 10px bottom
    
    
    # ----------------------------------------------------------------
    # 2. ENTRY FIELD (Requirement #2)
    # ----------------------------------------------------------------
    name_entry = ttk.Entry(
        root,
        textvariable=name_var,  # Bind to our StringVar for automatic sync
        font=("Arial", 11),
        width=25,  # Set width to accommodate reasonable name lengths
        justify='center'  # Center the text for better appearance
    )
    name_entry.pack(pady=10)
    
    # Set focus to the entry field so user can start typing immediately
    name_entry.focus()
    
    # Bind Enter key to trigger greeting (bonus enhancement)
    # This allows users to press Enter instead of clicking the button
    name_entry.bind('<Return>', lambda event: greet_function())
    
    
    # ----------------------------------------------------------------
    # 3. GREETING LABEL (Requirement #3)
    # ----------------------------------------------------------------
    greeting_label = ttk.Label(
        root,
        textvariable=greeting_var,  # Bind to our StringVar for automatic updates
        font=("Arial", 14, "bold"),
        foreground="blue",  # Make the greeting visually distinct
        background="lightgray",  # Add background color
        padding=10  # Add padding around the text
    )
    greeting_label.pack(pady=20)
    
    
    # ----------------------------------------------------------------
    # 4. GREET BUTTON (Requirement #4)
    # ----------------------------------------------------------------
    greet_button = ttk.Button(
        root,
        text="Greet Me",  # Button label as specified
        command=greet_function,  # Function to call when clicked
        width=15  # Set consistent button width
    )
    greet_button.pack(pady=10)
    
    
    # ----------------------------------------------------------------
    # ADDITIONAL UI ELEMENTS (Optional Enhancements)
    # ----------------------------------------------------------------
    
    # Add a separator line for visual organization
    separator = ttk.Separator(root, orient='horizontal')
    separator.pack(fill='x', padx=20, pady=10)
    
    # Add a close button for better user experience
    close_button = ttk.Button(
        root,
        text="Close Application",
        command=root.destroy,  # Built-in function to close the window
        width=15
    )
    close_button.pack(pady=5)
    
    # Add instructions label
    instructions_label = ttk.Label(
        root,
        text="Tip: You can also press Enter after typing your name!",
        font=("Arial", 9),
        foreground="gray"
    )
    instructions_label.pack(pady=(5, 10))


# ====================================================================
# MAIN APPLICATION ENTRY POINT
# ====================================================================

def main():
    """
    Main function that orchestrates the creation and execution of the
    personalized greeting application.
    
    This function follows the Model-View-Controller (MVC) pattern:
    - Model: StringVar objects for data storage
    - View: Tkinter widgets for user interface
    - Controller: Event handler functions for user interactions
    """
    print("Starting Personalized Greeting Form Application...")
    print("=" * 50)
    
    # Step 1: Create the main application window
    root = create_personalized_greeting_app()
    
    # Step 2: Set up data binding variables
    name_var, greeting_var = setup_string_variables()
    
    # Step 3: Create the event handler function
    greet_function = create_greet_function(name_var, greeting_var)
    
    # Step 4: Create and arrange all GUI widgets
    create_widgets(root, name_var, greeting_var, greet_function)
    
    # Step 5: Start the GUI event loop
    print("Application window created successfully!")
    print("User can now interact with the GUI...")
    print("Close the window or click 'Close Application' to exit.")
    
    # Start the main event loop - this keeps the application running
    # and responsive to user interactions until the window is closed
    root.mainloop()
    
    print("Application closed successfully!")


# ====================================================================
# PROGRAM EXECUTION
# ====================================================================

# This ensures the main() function only runs when this file is executed directly,
# not when it's imported as a module in other files
if __name__ == "__main__":
    main()


# ====================================================================
# TEAM NOTES AND DOCUMENTATION
# ====================================================================

"""
IMPLEMENTATION NOTES FOR TEAM:

1. ARCHITECTURE OVERVIEW:
   - Modular design with separate functions for different concerns
   - Clear separation between UI creation and business logic
   - Uses StringVar for automatic data binding between widgets and variables

2. KEY CONCEPTS DEMONSTRATED:
   - Event-driven programming with button clicks and Enter key binding
   - Data binding using StringVar objects
   - Widget layout using the pack geometry manager
   - Function closures for event handlers with access to variables

3. BONUS FEATURES IMPLEMENTED:
   ✅ Entry field clears automatically after greeting
   ✅ Default greeting "Hello, friend!" when input is blank
   ✅ Enter key binding for better user experience
   ✅ Visual enhancements (fonts, colors, padding)
   ✅ Close button for better UX

4. TESTING CHECKLIST:
   □ Enter a name and click "Greet Me" - should show "Hello, [name]!"
   □ Click "Greet Me" with empty field - should show "Hello, friend!"
   □ Entry field should clear after greeting
   □ Enter key should work same as clicking button
   □ Close button should exit application
   □ Window should be properly sized and centered

5. POSSIBLE EXTENSIONS:
   - Add input validation (e.g., no numbers in names)
   - Store greeting history
   - Add different greeting styles or languages
   - Include time-based greetings (Good morning, etc.)

6. ERROR HANDLING:
   - Current implementation handles empty input gracefully
   - Strip() method removes accidental whitespace
   - Default values prevent crashes

REMEMBER: Always test your changes and document any modifications!
"""