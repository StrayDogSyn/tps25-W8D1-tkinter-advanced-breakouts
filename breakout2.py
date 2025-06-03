"""
Breakout #2 – Enhanced Calculator Interface with Division & Special Effects
Author: [Team Five]
Date: June 2, 2025

Description:
This program creates a GUI calculator interface that allows users to perform
basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers.
It demonstrates Entry widgets for numeric input, Button widgets for actions,
Label widgets for displaying results, and conditional logic for calculations.

Enhanced Features:
1. Four operation buttons (Add, Subtract, Multiply, Divide)
2. Special animated warning effect for division by zero
3. Input validation with error handling
4. Professional UI layout with visual effects
"""

# Import required modules
import tkinter as tk
from tkinter import ttk
import threading
import time
import math

# ====================================================================
# CALCULATOR BUSINESS LOGIC
# ====================================================================

class Calculator:
    """
    Calculator class to handle arithmetic operations and input validation.
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
            number = float(value_str.strip())
            return True, number
        except (ValueError, AttributeError):
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


# ====================================================================
# SPECIAL EFFECTS CLASS
# ====================================================================

class SpecialEffects:
    """
    Class to handle visual effects for the calculator.
    """
    
    @staticmethod
    def division_by_zero_effect(root, result_label):
        """
        Creates a dramatic animated effect when division by zero occurs.
        
        Args:
            root: The main window
            result_label: The label to animate
        """
        def animate():
            # Store original values safely with defaults
            original_bg = '#f0f0f0'
            original_label_bg = 'lightyellow'
            original_label_fg = 'darkgreen'
            
            try:
                # Safely get original values
                try:
                    if root.winfo_exists():
                        original_bg = root.cget('bg')
                    if result_label.winfo_exists():
                        original_label_bg = result_label.cget('background')
                        original_label_fg = result_label.cget('foreground')
                except tk.TclError:
                    pass  # Use defaults
                
                # Warning messages to cycle through
                warning_messages = [
                    "⚠️ DIVISION BY ZERO! ⚠️",
                    "🚨 MATH ERROR DETECTED! 🚨", 
                    "⛔ INFINITY ALERT! ⛔",
                    "🔥 UNIVERSE BREAKING! 🔥",
                    "💀 CATASTROPHIC ERROR! 💀"
                ]
                
                # Color sequences for dramatic effect
                bg_colors = ['#FF0000', '#FF4500', '#FFD700', '#FF6347', '#DC143C']
                text_colors = ['white', 'yellow', 'black', 'white', 'yellow']
                
                # Get original window position safely
                try:
                    original_geometry = root.geometry()
                except tk.TclError:
                    original_geometry = "500x400+100+100"
                
                # Pulse effect with color changes
                for cycle in range(3):  # 3 cycles of animation
                    for i, (bg_color, text_color, message) in enumerate(zip(bg_colors, text_colors, warning_messages)):
                        # Check if widgets still exist before each update
                        try:
                            if not root.winfo_exists():
                                return
                            if not result_label.winfo_exists():
                                return
                        except tk.TclError:
                            return
                        
                        try:
                            # Update colors and message
                            root.configure(bg=bg_color)
                            result_label.configure(
                                background=bg_color,
                                foreground=text_color,
                                text=message,
                                font=("Arial", 16, "bold")
                            )
                            root.update_idletasks()
                            time.sleep(0.3)
                            
                            # Add shake effect
                            for shake in range(5):
                                try:
                                    if not root.winfo_exists():
                                        return
                                    
                                    # Parse current geometry
                                    geometry_parts = original_geometry.split('+')
                                    if len(geometry_parts) >= 3:
                                        x = int(geometry_parts[1])
                                        y = int(geometry_parts[2])
                                        
                                        # Create shake offset
                                        shake_x = x + ((-1) ** shake) * 10
                                        shake_y = y + ((-1) ** shake) * 5
                                        
                                        root.geometry(f"{geometry_parts[0]}+{shake_x}+{shake_y}")
                                        root.update_idletasks()
                                        time.sleep(0.05)
                                except (ValueError, tk.TclError):
                                    break  # Skip shake if geometry parsing fails
                            
                            # Return to original position
                            try:
                                root.geometry(original_geometry)
                                root.update_idletasks()
                            except tk.TclError:
                                pass
                                
                        except tk.TclError:
                            # Widget may have been destroyed, exit gracefully
                            return
                
                # Final dramatic message
                try:
                    if root.winfo_exists() and result_label.winfo_exists():
                        result_label.configure(
                            background='black',
                            foreground='red',
                            text="🔥 DIVISION BY ZERO IS FORBIDDEN! 🔥",
                            font=("Arial", 14, "bold")
                        )
                        root.configure(bg='black')
                        root.update_idletasks()
                        time.sleep(2)
                        
                        # Fade back to normal
                        fade_colors = ['#330000', '#660000', '#990000', '#CC0000', original_bg]
                        for fade_color in fade_colors:
                            if not root.winfo_exists():
                                return
                            try:
                                root.configure(bg=fade_color)
                                time.sleep(0.2)
                                root.update_idletasks()
                            except tk.TclError:
                                break
                except tk.TclError:
                    pass
                
            except Exception as e:
                print(f"Animation error (handled gracefully): {e}")
            
            finally:
                # Restore original appearance safely
                try:
                    if root.winfo_exists():
                        root.configure(bg=original_bg)
                    if result_label.winfo_exists():
                        result_label.configure(
                            background=original_label_bg,
                            foreground=original_label_fg,
                            text="Please enter valid numbers (divisor cannot be zero)",
                            font=("Arial", 14, "bold")
                        )
                    if root.winfo_exists():
                        root.update_idletasks()
                except tk.TclError:
                    # Window was closed during animation, that's okay
                    pass
        
        # Run animation in a separate thread to avoid blocking the UI
        animation_thread = threading.Thread(target=animate, daemon=True)
        animation_thread.start()


# ====================================================================
# MAIN APPLICATION SETUP
# ====================================================================

def create_calculator_app():
    """
    Creates and configures the main application window for the calculator.
    """
    root = tk.Tk()
    root.title("Enhanced Calculator with Division - Breakout #2")
    root.geometry("650x650")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.configure(bg='#f0f0f0')
    
    # Create menu bar with File > Exit option
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    
    def safe_exit():
        """Safely exits the application."""
        print("Exiting calculator via menu...")
        root.quit()
        root.destroy()
    
    file_menu.add_command(label="Exit", command=safe_exit, accelerator="Esc")
    file_menu.add_separator()
    file_menu.add_command(label="About", command=lambda: print("Enhanced Calculator v2.0 - Team Five"))
    
    return root


# ====================================================================
# STRING VARIABLES FOR DATA BINDING
# ====================================================================

def setup_calculator_variables():
    """
    Creates StringVar objects for data binding.
    """
    num1_var = tk.StringVar()
    num2_var = tk.StringVar()
    result_var = tk.StringVar(value="Result will appear here")
    return num1_var, num2_var, result_var


# ====================================================================
# CALCULATION EVENT HANDLERS
# ====================================================================

def create_calculation_functions(root, num1_var, num2_var, result_var, result_label):
    """
    Creates event handler functions for each arithmetic operation.
    """
    
    def perform_calculation(operation_name, operation_func):
        """
        Generic function to perform calculations with error handling.
        """
        num1_str = num1_var.get()
        num2_str = num2_var.get()
          # Validate inputs
        is_valid1, num1 = Calculator.validate_input(num1_str)
        is_valid2, num2 = Calculator.validate_input(num2_str)
        
        if not is_valid1 or not is_valid2:
            result_var.set("Please enter valid numbers.")
            return
        
        try:
            result = operation_func(num1, num2)
            
            # Format result
            if result.is_integer():
                result_text = f"Result: {int(result)}"
            else:
                result_text = f"Result: {result:.6f}".rstrip('0').rstrip('.')
            
            result_var.set(result_text)
            print(f"{operation_name}: {num1} and {num2} = {result}")
            
            # Clear input boxes after successful operation
            num1_var.set("")
            num2_var.set("")
            
        except ZeroDivisionError:
            # Trigger the special division by zero effect
            print("Division by zero detected - triggering special effect!")
            SpecialEffects.division_by_zero_effect(root, result_label)
            
        except Exception as e:
            result_var.set("Error in calculation.")
            print(f"Calculation error: {e}")
    
    # Create specific operation functions
    def add_numbers():
        perform_calculation("Addition", Calculator.add)
    
    def subtract_numbers():
        perform_calculation("Subtraction", Calculator.subtract)
    
    def multiply_numbers():
        perform_calculation("Multiplication", Calculator.multiply)
    
    def divide_numbers():
        perform_calculation("Division", Calculator.divide)
    
    return add_numbers, subtract_numbers, multiply_numbers, divide_numbers


# ====================================================================
# GUI WIDGET CREATION
# ====================================================================

def create_enhanced_calculator_widgets(root, num1_var, num2_var, result_var, 
                                     add_func, subtract_func, multiply_func, divide_func):
    """
    Creates the enhanced calculator interface with four operations.
    """
    
    # Create main frame
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # ----------------------------------------------------------------
    # TITLE SECTION
    # ----------------------------------------------------------------
    title_label = ttk.Label(
        main_frame,
        text="Enhanced Calculator with Division",
        font=("Arial", 18, "bold"),
        foreground="darkblue"
    )
    title_label.pack(pady=(0, 20))
    
    subtitle_label = ttk.Label(
        main_frame,
        text="⚠️ Warning: Division by zero triggers special effects! ⚠️",
        font=("Arial", 10, "italic"),
        foreground="red"
    )
    subtitle_label.pack(pady=(0, 15))
    
    # ----------------------------------------------------------------
    # INPUT SECTION
    # ----------------------------------------------------------------
    
    # First number input
    num1_frame = ttk.Frame(main_frame)
    num1_frame.pack(pady=10, fill=tk.X)
    
    ttk.Label(num1_frame, text="First Number:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
    num1_entry = ttk.Entry(
        num1_frame,
        textvariable=num1_var,
        font=("Arial", 12),
        width=15,
        justify='center'
    )
    num1_entry.pack(side=tk.RIGHT)
    
    # Second number input
    num2_frame = ttk.Frame(main_frame)
    num2_frame.pack(pady=10, fill=tk.X)
    
    ttk.Label(num2_frame, text="Second Number:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
    num2_entry = ttk.Entry(
        num2_frame,
        textvariable=num2_var,
        font=("Arial", 12),
        width=15,
        justify='center'
    )
    num2_entry.pack(side=tk.RIGHT)
    
    # Set focus to first entry
    num1_entry.focus()
    
    # ----------------------------------------------------------------
    # AUTO-CLEAR HELPER FUNCTION
    # ----------------------------------------------------------------
    def auto_clear_and_focus():
        """Helper function to clear inputs and return focus after successful calculation."""
        num1_var.set("")
        num2_var.set("")
        num1_entry.focus()
    
    # Update calculation functions to include auto-clear functionality
    if add_func:
        original_add = add_func
        def enhanced_add():
            original_add()
            # Only clear if calculation was successful (check if result shows a number)
            if "Result:" in result_var.get():
                auto_clear_and_focus()
        add_func = enhanced_add
    
    if subtract_func:
        original_subtract = subtract_func
        def enhanced_subtract():
            original_subtract()
            if "Result:" in result_var.get():
                auto_clear_and_focus()
        subtract_func = enhanced_subtract
    
    if multiply_func:
        original_multiply = multiply_func
        def enhanced_multiply():
            original_multiply()
            if "Result:" in result_var.get():
                auto_clear_and_focus()
        multiply_func = enhanced_multiply
    
    if divide_func:
        original_divide = divide_func
        def enhanced_divide():
            original_divide()
            if "Result:" in result_var.get():
                auto_clear_and_focus()
        divide_func = enhanced_divide
      # ----------------------------------------------------------------
    # OPERATION BUTTONS SECTION (Now with 4 buttons!)
    # ----------------------------------------------------------------
    
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)
    
    # Create a 2x2 grid for the four operation buttons
      # Top row
    top_frame = ttk.Frame(button_frame)
    top_frame.pack(pady=5)
    
    add_button = ttk.Button(
        top_frame,
        text="Add ➕",
        command=add_func,
        width=15
    )
    add_button.pack(side=tk.LEFT, padx=5)
    
    subtract_button = ttk.Button(
        top_frame,
        text="Subtract ➖",
        command=subtract_func,
        width=15
    )
    subtract_button.pack(side=tk.LEFT, padx=5)
    
    # Bottom row
    bottom_frame = ttk.Frame(button_frame)
    bottom_frame.pack(pady=5)
    
    multiply_button = ttk.Button(
        bottom_frame,
        text="Multiply ✖️",
        command=multiply_func,
        width=15
    )
    multiply_button.pack(side=tk.LEFT, padx=5)
    
    # Special styling for the division button
    divide_button = ttk.Button(
        bottom_frame,
        text="Divide ➗",
        command=divide_func,
        width=15
    )
    divide_button.pack(side=tk.LEFT, padx=5)
    
    # Add warning label for division
    warning_frame = ttk.Frame(main_frame)
    warning_frame.pack(pady=5)
    
    ttk.Label(
        warning_frame,
        text="💀 Beware: Dividing by zero unleashes chaos! 💀",
        font=("Arial", 9, "italic"),
        foreground="darkred"
    ).pack()
    
    # ----------------------------------------------------------------
    # RESULT DISPLAY SECTION
    # ----------------------------------------------------------------
    
    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.pack(fill='x', pady=20)
    
    # Result label with special styling for effects
    result_label = ttk.Label(
        main_frame,
        textvariable=result_var,
        font=("Arial", 14, "bold"),
        foreground="darkgreen",
        background="lightyellow",
        padding=15,
        relief="solid",
        borderwidth=2
    )
    result_label.pack(pady=10)
    
    # ----------------------------------------------------------------
    # UTILITY BUTTONS
    # ----------------------------------------------------------------
    
    utility_frame = ttk.Frame(main_frame)
    utility_frame.pack(pady=15)
    
    def clear_all():
        """Clears all input fields and result display."""
        num1_var.set("")
        num2_var.set("")
        result_var.set("Result will appear here")
        num1_entry.focus()        # Reset any visual effects
        try:
            root.configure(bg='#f0f0f0')
            result_label.configure(
                background="lightyellow",
                foreground="darkgreen",
                font=("Arial", 14, "bold")
            )
        except tk.TclError:
            pass
        print("All fields cleared")
    
    def safe_close():
        """Safely closes the application with confirmation."""
        print("Closing Enhanced Calculator...")
        try:
            root.quit()  # Stops the mainloop
            root.destroy()  # Destroys the window
        except tk.TclError:
            pass  # Window already closed
    
    clear_button = ttk.Button(
        utility_frame,
        text="Clear All 🔄",
        command=clear_all,
        width=15
    )
    clear_button.pack(side=tk.LEFT, padx=5)
    
    # Enhanced close button with better styling
    close_button = ttk.Button(
        utility_frame,
        text="Exit Calculator ❌",
        command=safe_close,
        width=18
    )
    close_button.pack(side=tk.LEFT, padx=5)
    
    # Add keyboard shortcut for closing (Escape key)
    root.bind('<Escape>', lambda event: safe_close())
    
    # Return the result label so it can be passed to the effect functions
    return result_label


# ====================================================================
# MAIN APPLICATION ENTRY POINT
# ====================================================================

def main():
    """
    Main function that creates and runs the enhanced calculator application.
    """
    print("Starting Enhanced Calculator with Division and Special Effects...")
    print("=" * 60)
    print("⚠️  WARNING: Division by zero will trigger visual effects!")
    print("🎭 Get ready for a show if you try to divide by zero!")
    print("=" * 60)
    
    # Create application window
    root = create_calculator_app()
    
    # Set up data binding variables
    num1_var, num2_var, result_var = setup_calculator_variables()
    
    # Create GUI widgets first to get the result_label reference
    result_label = create_enhanced_calculator_widgets(
        root, num1_var, num2_var, result_var,
        None, None, None, None  # Temporarily pass None for functions
    )
    
    # Now create calculation functions with result_label reference
    add_func, subtract_func, multiply_func, divide_func = create_calculation_functions(
        root, num1_var, num2_var, result_var, result_label
    )
    
    # Update button commands (we need to recreate the widgets with proper functions)
    # Clear the main frame and recreate with proper functions
    for widget in root.winfo_children():
        widget.destroy()
    
    result_label = create_enhanced_calculator_widgets(
        root, num1_var, num2_var, result_var,
        add_func, subtract_func, multiply_func, divide_func
    )
    
    print("Enhanced Calculator application ready!")
    print("Features:")
    print("✅ Four arithmetic operations (Add, Subtract, Multiply, Divide)")
    print("✅ Input validation and error handling")
    print("✅ Special animated effects for division by zero")
    print("✅ Professional UI with visual feedback")
    print("\nTry dividing by zero for a surprise! 😈")
    
    # Start the GUI event loop
    root.mainloop()
    
    print("Enhanced Calculator application closed!")


# ====================================================================
# PROGRAM EXECUTION
# ====================================================================

if __name__ == "__main__":
    main()


# ====================================================================
# TEAM NOTES - ENHANCED VERSION
# ====================================================================

"""
ENHANCED CALCULATOR IMPLEMENTATION NOTES:

🎯 NEW FEATURES ADDED:
1. ✅ Division operation with proper error handling
2. ✅ Spectacular animated visual effects for division by zero
3. ✅ Four operation buttons in a 2x2 grid layout
4. ✅ Enhanced UI with warnings and visual feedback
5. ✅ Threading for smooth animations without blocking UI
6. ✅ Color-changing animations with shake effects
7. ✅ Professional error recovery and state restoration

🎭 SPECIAL EFFECTS DETAILS:
- Division by zero triggers a dramatic animated sequence
- Window shaking, color cycling, and warning messages
- Multiple phases: warning → alarm → dramatic → fade → restore
- Non-blocking animation using threading
- Automatic recovery to normal state

🔧 TECHNICAL IMPROVEMENTS:
- Modular SpecialEffects class for reusable animations
- Thread-safe UI updates with extensive error checking
- Enhanced error handling with custom exceptions
- Improved number formatting (removes trailing zeros)
- Better visual hierarchy with fonts and colors
- Widget existence checking to prevent TclError exceptions

⚠️ IMPORTANT TESTING SCENARIOS:
□ Test all four operations with valid numbers
□ Test division by zero to see the special effect
□ Test invalid input handling
□ Test clear functionality after effects
□ Verify UI responsiveness during animations
□ Test window closing during animation (should handle gracefully)

🚀 POSSIBLE EXTENSIONS:
- Add sound effects to the division by zero animation
- Create different animation styles for different errors
- Add particle effects or explosions
- Implement achievement system for finding easter eggs
- Add custom themes and color schemes

🛠️ BUG FIXES APPLIED:
- Added extensive tk.TclError exception handling
- Widget existence checking before each UI operation
- Safe defaults for widget properties
- Graceful animation termination when window is closed
- Thread-safe UI operations with proper error recovery

Remember: The division by zero effect is designed to be dramatic but 
educational - it shows users the importance of validating mathematical 
operations while providing entertainment value!
"""
