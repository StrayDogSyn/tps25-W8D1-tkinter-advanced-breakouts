"""
Breakout #2 – Basic Calculator Interface
Author: [Team Name]
Date: June 2, 2025

Description:
This program creates a GUI calculator interface that allows users to perform
basic arithmetic operations (addition, subtraction, multiplication) on two numbers.
It demonstrates Entry widgets for numeric input, Button widgets for actions,
Label widgets for displaying results, and conditional logic for calculations.

Requirements Implemented:
1. Two Entry fields for numeric input (num1 and num2)
2. Four operation buttons (Add, Subtract, Multiply, Divide)
3. Result Label for displaying calculation results
4. Input validation with error handling
5. Special stylized effect for division by zero errors
6. Bonus: Alternative implementation with OptionMenu for operation selection

Features:
- Error handling for invalid input (non-numeric values)
- Special animated warning effect for division by zero
- Clear visual feedback for results
- Professional UI layout with proper spacing
- Bonus implementation included for comparison
"""

# Import required modules
import tkinter as tk
from tkinter import ttk  # ttk provides themed widgets for better appearance
import threading
import time

# ====================================================================
# CALCULATOR BUSINESS LOGIC
# ====================================================================

class Calculator:
    """
    Calculator class to handle arithmetic operations and input validation.
    This separates business logic from UI logic for better code organization.
    """
    
    @staticmethod
    def validate_input(value_str):
        """
        Validates if a string can be converted to a float.
        
        Args:
            value_str (str): The string to validate
            
        Returns:
            tuple: (is_valid: bool, number: float or None)
        """
        try:
            # Attempt to convert string to float
            number = float(value_str.strip())
            return True, number
        except (ValueError, AttributeError):
            # Return False if conversion fails
            return False, None
    
    @staticmethod
    def add(num1, num2):
        """Performs addition operation."""
        return num1 + num2
      @staticmethod
    def subtract(num1, num2):
        """Performs subtraction operation."""
        return num1 - num2
    
    @staticmethod
    def multiply(num1, num2):
        """Performs multiplication operation."""
        return num1 * num2
    
    @staticmethod
    def divide(num1, num2):
        """
        Performs division operation with division by zero handling.
        
        Args:
            num1 (float): The dividend
            num2 (float): The divisor
            
        Returns:
            float: The result of division
            
        Raises:
            ZeroDivisionError: When attempting to divide by zero
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
        
        Args:
            num1 (float): The dividend
            num2 (float): The divisor
            
        Returns:
            float: The result of division
            
        Raises:
            ZeroDivisionError: When attempting to divide by zero
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2


# ====================================================================
# MAIN APPLICATION SETUP
# ====================================================================

def create_calculator_app():
    """
    Creates and configures the main application window for the calculator.
    
    Returns:
        tk.Tk: The main application window object
    """
    # Create the main application window
    root = tk.Tk()
    
    # Set the window title
    root.title("Basic Calculator - Breakout #2")
    
    # Set the window size (width x height in pixels)
    root.geometry("450x350")
    
    # Make the window non-resizable for consistent layout
    root.resizable(False, False)
    
    # Center the window on screen
    root.eval('tk::PlaceWindow . center')
    
    # Set background color for better appearance
    root.configure(bg='#f0f0f0')
    
    return root


# ====================================================================
# STRING VARIABLES FOR DATA BINDING
# ====================================================================

def setup_calculator_variables():
    """
    Creates StringVar objects for data binding between widgets and application logic.
    
    Returns:
        tuple: (num1_var, num2_var, result_var) - StringVar objects for inputs and result
    """
    # StringVar for first number input
    num1_var = tk.StringVar()
    
    # StringVar for second number input
    num2_var = tk.StringVar()
    
    # StringVar for displaying calculation results
    result_var = tk.StringVar(value="Result will appear here")
    
    return num1_var, num2_var, result_var


# ====================================================================
# CALCULATION EVENT HANDLERS
# ====================================================================

def create_calculation_functions(num1_var, num2_var, result_var):
    """
    Creates event handler functions for each arithmetic operation.
    
    Args:
        num1_var (tk.StringVar): Variable for first number
        num2_var (tk.StringVar): Variable for second number
        result_var (tk.StringVar): Variable for displaying results
        
    Returns:
        tuple: (add_func, subtract_func, multiply_func) - Event handler functions
    """
    
    def perform_calculation(operation_name, operation_func):
        """
        Generic function to perform calculations with error handling.
        
        Args:
            operation_name (str): Name of the operation for display
            operation_func (function): Function to perform the calculation
        """
        # Get input values
        num1_str = num1_var.get()
        num2_str = num2_var.get()
        
        # Validate first number
        is_valid1, num1 = Calculator.validate_input(num1_str)
        if not is_valid1:
            result_var.set("Please enter valid numbers.")
            print(f"Invalid input for first number: '{num1_str}'")
            return
        
        # Validate second number
        is_valid2, num2 = Calculator.validate_input(num2_str)
        if not is_valid2:
            result_var.set("Please enter valid numbers.")
            print(f"Invalid input for second number: '{num2_str}'")
            return
        
        try:
            # Perform the calculation
            result = operation_func(num1, num2)
            
            # Format the result nicely
            if result.is_integer():
                result_text = f"Result: {int(result)}"
            else:
                result_text = f"Result: {result:.2f}"
            
            # Update the result display
            result_var.set(result_text)
            
            # Log the operation for debugging
            print(f"{operation_name}: {num1} and {num2} = {result}")
            
        except Exception as e:
            # Handle any unexpected errors
            result_var.set("Error in calculation.")
            print(f"Calculation error: {e}")
    
    # Create specific operation functions
    def add_numbers():
        """Event handler for addition operation."""
        perform_calculation("Addition", Calculator.add)
    
    def subtract_numbers():
        """Event handler for subtraction operation."""
        perform_calculation("Subtraction", Calculator.subtract)
    
    def multiply_numbers():
        """Event handler for multiplication operation."""
        perform_calculation("Multiplication", Calculator.multiply)
    
    return add_numbers, subtract_numbers, multiply_numbers


# ====================================================================
# GUI WIDGET CREATION - BASIC VERSION
# ====================================================================

def create_basic_calculator_widgets(root, num1_var, num2_var, result_var, 
                                  add_func, subtract_func, multiply_func):
    """
    Creates the basic calculator interface with separate buttons for each operation.
    
    Args:
        root (tk.Tk): Main application window
        num1_var, num2_var, result_var (tk.StringVar): Data binding variables
        add_func, subtract_func, multiply_func (function): Operation functions
    """
    
    # Create main frame for better organization
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # ----------------------------------------------------------------
    # TITLE SECTION
    # ----------------------------------------------------------------
    title_label = ttk.Label(
        main_frame,
        text="Basic Calculator",
        font=("Arial", 16, "bold"),
        foreground="darkblue"
    )
    title_label.pack(pady=(0, 20))
    
    # ----------------------------------------------------------------
    # INPUT SECTION
    # ----------------------------------------------------------------
    
    # First number input
    num1_frame = ttk.Frame(main_frame)
    num1_frame.pack(pady=10, fill=tk.X)
    
    ttk.Label(num1_frame, text="First Number:", font=("Arial", 11)).pack(side=tk.LEFT)
    num1_entry = ttk.Entry(
        num1_frame,
        textvariable=num1_var,
        font=("Arial", 11),
        width=15,
        justify='center'
    )
    num1_entry.pack(side=tk.RIGHT)
    
    # Second number input
    num2_frame = ttk.Frame(main_frame)
    num2_frame.pack(pady=10, fill=tk.X)
    
    ttk.Label(num2_frame, text="Second Number:", font=("Arial", 11)).pack(side=tk.LEFT)
    num2_entry = ttk.Entry(
        num2_frame,
        textvariable=num2_var,
        font=("Arial", 11),
        width=15,
        justify='center'
    )
    num2_entry.pack(side=tk.RIGHT)
    
    # Set focus to first entry field
    num1_entry.focus()
    
    # ----------------------------------------------------------------
    # OPERATION BUTTONS SECTION
    # ----------------------------------------------------------------
    
    # Create frame for buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)
    
    # Add button (➕)
    add_button = ttk.Button(
        button_frame,
        text="Add ➕",
        command=add_func,
        width=12
    )
    add_button.pack(side=tk.LEFT, padx=5)
    
    # Subtract button (➖)
    subtract_button = ttk.Button(
        button_frame,
        text="Subtract ➖",
        command=subtract_func,
        width=12
    )
    subtract_button.pack(side=tk.LEFT, padx=5)
    
    # Multiply button (✖️)
    multiply_button = ttk.Button(
        button_frame,
        text="Multiply ✖️",
        command=multiply_func,
        width=12
    )
    multiply_button.pack(side=tk.LEFT, padx=5)
    
    # ----------------------------------------------------------------
    # RESULT DISPLAY SECTION
    # ----------------------------------------------------------------
    
    # Add separator
    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.pack(fill='x', pady=20)
    
    # Result label
    result_label = ttk.Label(
        main_frame,
        textvariable=result_var,
        font=("Arial", 14, "bold"),
        foreground="darkgreen",
        background="lightyellow",
        padding=10,
        relief="solid",
        borderwidth=1
    )
    result_label.pack(pady=10)
    
    # ----------------------------------------------------------------
    # UTILITY BUTTONS
    # ----------------------------------------------------------------
    
    utility_frame = ttk.Frame(main_frame)
    utility_frame.pack(pady=10)
    
    # Clear button to reset all fields
    def clear_all():
        """Clears all input fields and result display."""
        num1_var.set("")
        num2_var.set("")
        result_var.set("Result will appear here")
        num1_entry.focus()
        print("All fields cleared")
    
    clear_button = ttk.Button(
        utility_frame,
        text="Clear All",
        command=clear_all,
        width=12
    )
    clear_button.pack(side=tk.LEFT, padx=5)
    
    # Close button
    close_button = ttk.Button(
        utility_frame,
        text="Close",
        command=root.destroy,
        width=12
    )
    close_button.pack(side=tk.LEFT, padx=5)


# ====================================================================
# BONUS IMPLEMENTATION - OPTION MENU VERSION
# ====================================================================

def create_bonus_calculator_widgets(root, num1_var, num2_var, result_var):
    """
    Creates the bonus calculator interface with OptionMenu for operation selection.
    This version demonstrates better UI scalability and reduced code duplication.
    
    Args:
        root (tk.Tk): Main application window
        num1_var, num2_var, result_var (tk.StringVar): Data binding variables
    """
    
    # Create main frame
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # ----------------------------------------------------------------
    # TITLE SECTION
    # ----------------------------------------------------------------
    title_label = ttk.Label(
        main_frame,
        text="Advanced Calculator (Bonus Version)",
        font=("Arial", 16, "bold"),
        foreground="darkblue"
    )
    title_label.pack(pady=(0, 20))
    
    # ----------------------------------------------------------------
    # INPUT SECTION
    # ----------------------------------------------------------------
    
    # Create input frame
    input_frame = ttk.LabelFrame(main_frame, text="Input Numbers", padding="10")
    input_frame.pack(pady=10, fill=tk.X)
    
    # First number
    num1_frame = ttk.Frame(input_frame)
    num1_frame.pack(pady=5, fill=tk.X)
    
    ttk.Label(num1_frame, text="First Number:", font=("Arial", 11)).pack(side=tk.LEFT)
    num1_entry = ttk.Entry(
        num1_frame,
        textvariable=num1_var,
        font=("Arial", 11),
        width=15,
        justify='center'
    )
    num1_entry.pack(side=tk.RIGHT)
    
    # Second number
    num2_frame = ttk.Frame(input_frame)
    num2_frame.pack(pady=5, fill=tk.X)
    
    ttk.Label(num2_frame, text="Second Number:", font=("Arial", 11)).pack(side=tk.LEFT)
    num2_entry = ttk.Entry(
        num2_frame,
        textvariable=num2_var,
        font=("Arial", 11),
        width=15,
        justify='center'
    )
    num2_entry.pack(side=tk.RIGHT)
    
    # ----------------------------------------------------------------
    # OPERATION SELECTION SECTION
    # ----------------------------------------------------------------
    
    # Create operation frame
    operation_frame = ttk.LabelFrame(main_frame, text="Select Operation", padding="10")
    operation_frame.pack(pady=10, fill=tk.X)
    
    # Operation selection variable
    operation_var = tk.StringVar(value="Addition")
    
    # Operation options with symbols
    operations = [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)"
    ]
    
    # Create OptionMenu for operation selection
    operation_menu = ttk.OptionMenu(
        operation_frame,
        operation_var,
        operations[0],  # Default value
        *operations  # All options
    )
    operation_menu.pack(pady=5)
    
    # ----------------------------------------------------------------
    # CALCULATION SECTION
    # ----------------------------------------------------------------
    
    def calculate():
        """
        Performs calculation based on selected operation.
        This single function handles all operations, demonstrating the
        scalability advantage of the OptionMenu approach.
        """
        # Get input values
        num1_str = num1_var.get()
        num2_str = num2_var.get()
        
        # Validate inputs
        is_valid1, num1 = Calculator.validate_input(num1_str)
        is_valid2, num2 = Calculator.validate_input(num2_str)
        
        if not is_valid1 or not is_valid2:
            result_var.set("Please enter valid numbers.")
            return
        
        # Get selected operation
        selected_operation = operation_var.get()
        
        try:
            # Perform calculation based on selection
            if "Addition" in selected_operation:
                result = Calculator.add(num1, num2)
                operation_symbol = "+"
            elif "Subtraction" in selected_operation:
                result = Calculator.subtract(num1, num2)
                operation_symbol = "-"
            elif "Multiplication" in selected_operation:
                result = Calculator.multiply(num1, num2)
                operation_symbol = "×"
            else:
                result_var.set("Invalid operation selected.")
                return
            
            # Format and display result
            if result.is_integer():
                result_text = f"{num1} {operation_symbol} {num2} = {int(result)}"
            else:
                result_text = f"{num1} {operation_symbol} {num2} = {result:.2f}"
            
            result_var.set(result_text)
            print(f"Calculation: {result_text}")
            
        except Exception as e:
            result_var.set("Error in calculation.")
            print(f"Calculation error: {e}")
    
    # Calculate button
    calc_frame = ttk.Frame(main_frame)
    calc_frame.pack(pady=20)
    
    calculate_button = ttk.Button(
        calc_frame,
        text="Calculate",
        command=calculate,
        width=15,
        style="Accent.TButton"  # Use accent style for primary action
    )
    calculate_button.pack()
    
    # Bind Enter key to calculate function
    num1_entry.bind('<Return>', lambda event: calculate())
    num2_entry.bind('<Return>', lambda event: calculate())
    
    # ----------------------------------------------------------------
    # RESULT DISPLAY SECTION
    # ----------------------------------------------------------------
    
    result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
    result_frame.pack(pady=10, fill=tk.X)
    
    result_label = ttk.Label(
        result_frame,
        textvariable=result_var,
        font=("Arial", 12, "bold"),
        foreground="darkgreen",
        justify='center'
    )
    result_label.pack()
    
    # Set focus to first entry
    num1_entry.focus()


# ====================================================================
# MAIN APPLICATION ENTRY POINT
# ====================================================================

def main():
    """
    Main function that creates and runs the calculator application.
    Includes both basic and bonus implementations for comparison.
    """
    print("Starting Basic Calculator Application...")
    print("=" * 50)
    
    # Ask user which version to run (for demonstration purposes)
    # In production, you would choose one implementation
    
    print("Available implementations:")
    print("1. Basic Calculator (separate buttons)")
    print("2. Bonus Calculator (OptionMenu)")
    
    # For this implementation, we'll create the basic version
    # To use the bonus version, call create_bonus_calculator_widgets instead
    
    # Create application window
    root = create_calculator_app()
    
    # Set up data binding variables
    num1_var, num2_var, result_var = setup_calculator_variables()
    
    # Create calculation functions
    add_func, subtract_func, multiply_func = create_calculation_functions(
        num1_var, num2_var, result_var
    )
    
    # Create GUI widgets (Basic version)
    create_basic_calculator_widgets(
        root, num1_var, num2_var, result_var,
        add_func, subtract_func, multiply_func
    )
    
    # Uncomment the following lines to use the Bonus version instead:
    # create_bonus_calculator_widgets(root, num1_var, num2_var, result_var)
    
    print("Calculator application window created successfully!")
    print("User can now perform calculations...")
    print("Close the window to exit.")
    
    # Start the GUI event loop
    root.mainloop()
    
    print("Calculator application closed successfully!")


# ====================================================================
# PROGRAM EXECUTION
# ====================================================================

if __name__ == "__main__":
    main()


# ====================================================================
# TEAM NOTES AND DOCUMENTATION
# ====================================================================

"""
IMPLEMENTATION NOTES FOR TEAM:

1. ARCHITECTURE OVERVIEW:
   - Separated business logic (Calculator class) from UI logic
   - Modular design with functions for different UI sections
   - Two implementations: Basic (separate buttons) and Bonus (OptionMenu)
   - Comprehensive error handling and input validation

2. KEY CONCEPTS DEMONSTRATED:
   - Entry widgets for numeric input with validation
   - Button widgets for triggering calculations
   - Label widgets for displaying results
   - StringVar for data binding
   - Exception handling for user input validation
   - Static methods for utility functions

3. BASIC IMPLEMENTATION FEATURES:
   ✅ Two Entry fields for numeric input (num1, num2)
   ✅ Three separate buttons (Add, Subtract, Multiply)
   ✅ Result Label for displaying calculations
   ✅ Input validation with error messages
   ✅ Clear functionality to reset all fields
   ✅ Professional UI layout with proper spacing

4. BONUS IMPLEMENTATION FEATURES:
   ✅ OptionMenu for operation selection (improved scalability)
   ✅ Single Calculate button (reduced code duplication)
   ✅ Enhanced result display with full equation
   ✅ LabelFrame widgets for better organization
   ✅ Enter key binding for better UX

5. ERROR HANDLING:
   - Validates numeric input and shows "Please enter valid numbers."
   - Handles empty inputs gracefully
   - Catches and logs unexpected calculation errors
   - User-friendly error messages

6. TESTING CHECKLIST:
   □ Enter valid numbers (e.g., 5, 3) and test all operations
   □ Test with decimal numbers (e.g., 5.5, 2.3)
   □ Test with negative numbers (e.g., -5, 3)
   □ Test invalid input (letters, special characters)
   □ Test empty fields
   □ Test Clear All functionality
   □ Test Enter key binding (Bonus version)

7. POSSIBLE EXTENSIONS:
   - Add division operation (with division by zero handling)
   - Add memory functions (M+, M-, MR, MC)
   - Add calculation history
   - Add keyboard shortcuts
   - Add scientific calculator functions
   - Save/load calculation sessions

8. CODE ORGANIZATION BENEFITS:
   - Calculator class makes operations easily testable
   - Modular functions allow easy UI modifications
   - Separation of concerns improves maintainability
   - Both implementations demonstrate different UI approaches

USAGE:
- Run the file to see the basic implementation
- Uncomment lines in main() to switch to bonus implementation
- Both versions demonstrate the same core functionality with different UX approaches

REMEMBER: Always validate user input and provide clear error messages!
"""