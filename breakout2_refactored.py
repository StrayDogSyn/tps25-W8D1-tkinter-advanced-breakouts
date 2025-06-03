"""
Enhanced Calculator Interface with Division & Special Effects
Author: Team Five
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
5. Auto-clear functionality after successful operations
6. Exit button and menu system
"""

import tkinter as tk
from tkinter import ttk, messagebox


# ====================================================================
# CALCULATOR BUSINESS LOGIC
# ====================================================================

class Calculator:
    """Calculator class to handle arithmetic operations and input validation."""
    
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
    """Class to handle visual effects for the calculator."""
    
    @staticmethod
    def division_by_zero_effect(root, result_label):
        """
        Creates a dramatic animated effect when division by zero occurs.
        
        Args:
            root: The main window
            result_label: The label to animate
        """
        # Store original values safely with defaults
        original_bg = '#f0f0f0'
        original_label_bg = 'lightyellow'
        original_label_fg = 'darkgreen'
        
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
            original_geometry = "650x650+100+100"
        
        # Animation state
        animation_state = {
            'cycle': 0,
            'step': 0,
            'shake_count': 0,
            'phase': 'pulse'  # pulse, final, fade, restore
        }
        
        def animate_step():
            """Single animation step using root.after() for proper thread safety"""
            try:
                # Check if widgets still exist
                if not root.winfo_exists() or not result_label.winfo_exists():
                    return
                
                if animation_state['phase'] == 'pulse':
                    # Pulse effect with color changes
                    if animation_state['cycle'] < 3:  # 3 cycles
                        if animation_state['step'] < 5:  # 5 messages per cycle
                            i = animation_state['step']
                            bg_color = bg_colors[i]
                            text_color = text_colors[i]
                            message = warning_messages[i]
                            
                            # Update colors and message
                            root.configure(bg=bg_color)
                            result_label.configure(
                                background=bg_color,
                                foreground=text_color,
                                text=message,
                                font=("Arial", 16, "bold")
                            )
                            
                            # Schedule next step
                            animation_state['step'] += 1
                            root.after(300, animate_step)  # 300ms delay
                            
                        else:
                            # End of message cycle, start shake effect
                            animation_state['step'] = 0
                            animation_state['shake_count'] = 0
                            start_shake()
                    else:
                        # Move to final phase
                        animation_state['phase'] = 'final'
                        root.after(100, animate_step)
                
                elif animation_state['phase'] == 'final':
                    # Final dramatic message
                    result_label.configure(
                        background='black',
                        foreground='red',
                        text="🔥 DIVISION BY ZERO IS FORBIDDEN! 🔥",
                        font=("Arial", 14, "bold")
                    )
                    root.configure(bg='black')
                    
                    # Wait 5 seconds as requested by user, then move to fade
                    animation_state['phase'] = 'fade'
                    animation_state['step'] = 0
                    root.after(5000, animate_step)  # 5 second delay
                
                elif animation_state['phase'] == 'fade':
                    # Fade back to normal
                    fade_colors = ['#330000', '#660000', '#990000', '#CC0000', original_bg]
                    if animation_state['step'] < len(fade_colors):
                        fade_color = fade_colors[animation_state['step']]
                        root.configure(bg=fade_color)
                        animation_state['step'] += 1
                        root.after(200, animate_step)  # 200ms per fade step
                    else:
                        # Move to restore phase
                        animation_state['phase'] = 'restore'
                        root.after(100, animate_step)
                
                elif animation_state['phase'] == 'restore':
                    # Restore original appearance
                    root.configure(bg=original_bg)
                    result_label.configure(
                        background=original_label_bg,
                        foreground=original_label_fg,
                        text="Please enter valid numbers (divisor cannot be zero)",
                        font=("Arial", 14, "bold")
                    )
                    print("Division by zero animation completed!")
                    
            except tk.TclError:
                # Widget was destroyed during animation
                print("Animation stopped - window was closed")
                return
            except Exception as e:
                print(f"Animation error: {e}")
        
        def start_shake():
            """Start the shake effect"""
            def shake_step():
                try:
                    if not root.winfo_exists() or animation_state['shake_count'] >= 5:
                        # End shake, return to original position and continue with next cycle
                        try:
                            root.geometry(original_geometry)
                        except tk.TclError:
                            pass
                        animation_state['cycle'] += 1
                        animation_state['step'] = 0
                        animation_state['shake_count'] = 0
                        root.after(100, animate_step)
                        return
                    
                    # Parse current geometry for shake effect
                    try:
                        geometry_parts = original_geometry.split('+')
                        if len(geometry_parts) >= 3:
                            x = int(geometry_parts[1])
                            y = int(geometry_parts[2])
                            
                            # Create shake offset
                            shake_x = x + ((-1) ** animation_state['shake_count']) * 15
                            shake_y = y + ((-1) ** animation_state['shake_count']) * 8
                            
                            root.geometry(f"{geometry_parts[0]}+{shake_x}+{shake_y}")
                    except (ValueError, tk.TclError):
                        pass  # Skip this shake if geometry parsing fails
                    
                    animation_state['shake_count'] += 1
                    root.after(50, shake_step)  # 50ms shake interval
                    
                except tk.TclError:
                    return
            
            shake_step()
        
        # Start the animation
        print("Starting division by zero visual effect...")
        root.after(100, animate_step)  # Start after 100ms


# ====================================================================
# MAIN CALCULATOR APPLICATION CLASS
# ====================================================================

class CalculatorApp:
    """Main calculator application class for better organization."""
    
    def __init__(self):
        """Initialize the calculator application."""
        self.root = None
        self.num1_var = None
        self.num2_var = None
        self.result_var = None
        self.result_label = None
        self.num1_entry = None
        self.num2_entry = None
        
    def create_main_window(self):
        """Creates and configures the main application window."""
        self.root = tk.Tk()
        self.root.title("Enhanced Calculator with Division - Breakout #2")
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg='#f0f0f0')
        
        # Create menu bar
        self.create_menu()
        
        # Bind Escape key to exit
        self.root.bind('<Escape>', lambda event: self.safe_exit())
        
    def create_menu(self):
        """Creates the menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="Exit", command=self.safe_exit, accelerator="Esc")
        file_menu.add_separator()
        file_menu.add_command(
            label="About", 
            command=lambda: messagebox.showinfo(
                "About", 
                "Enhanced Calculator v2.0\\nTeam Five\\n\\nFeatures auto-clear and special effects!"
            )
        )
    
    def setup_variables(self):
        """Creates StringVar objects for data binding."""
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Result will appear here")
    
    def create_ui(self):
        """Creates the main user interface."""
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title section
        self.create_title_section(main_frame)
        
        # Input section
        self.create_input_section(main_frame)
        
        # Button section
        self.create_button_section(main_frame)
        
        # Result section
        self.create_result_section(main_frame)
        
        # Utility buttons
        self.create_utility_section(main_frame)
    
    def create_title_section(self, parent):
        """Creates the title section."""
        title_label = ttk.Label(
            parent,
            text="Enhanced Calculator with Division",
            font=("Arial", 18, "bold"),
            foreground="darkblue"
        )
        title_label.pack(pady=(0, 20))
        
        subtitle_label = ttk.Label(
            parent,
            text="⚠️ Warning: Division by zero triggers special effects! ⚠️",
            font=("Arial", 10, "italic"),
            foreground="red"
        )
        subtitle_label.pack(pady=(0, 15))
    
    def create_input_section(self, parent):
        """Creates the input section."""
        # First number input
        num1_frame = ttk.Frame(parent)
        num1_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(num1_frame, text="First Number:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        self.num1_entry = ttk.Entry(
            num1_frame,
            textvariable=self.num1_var,
            font=("Arial", 12),
            width=15,
            justify='center'
        )
        self.num1_entry.pack(side=tk.RIGHT)
        
        # Second number input
        num2_frame = ttk.Frame(parent)
        num2_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(num2_frame, text="Second Number:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        self.num2_entry = ttk.Entry(
            num2_frame,
            textvariable=self.num2_var,
            font=("Arial", 12),
            width=15,
            justify='center'
        )
        self.num2_entry.pack(side=tk.RIGHT)
        
        # Set focus to first entry
        self.num1_entry.focus()
    
    def create_button_section(self, parent):
        """Creates the operation buttons section."""
        button_frame = ttk.Frame(parent)
        button_frame.pack(pady=20)
        
        # Top row
        top_frame = ttk.Frame(button_frame)
        top_frame.pack(pady=5)
        
        ttk.Button(
            top_frame,
            text="Add ➕",
            command=self.add_numbers,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            top_frame,
            text="Subtract ➖",
            command=self.subtract_numbers,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        # Bottom row
        bottom_frame = ttk.Frame(button_frame)
        bottom_frame.pack(pady=5)
        
        ttk.Button(
            bottom_frame,
            text="Multiply ✖️",
            command=self.multiply_numbers,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame,
            text="Divide ➗",
            command=self.divide_numbers,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        # Warning label
        warning_frame = ttk.Frame(parent)
        warning_frame.pack(pady=5)
        
        ttk.Label(
            warning_frame,
            text="💀 Beware: Dividing by zero unleashes chaos! 💀",
            font=("Arial", 9, "italic"),
            foreground="darkred"
        ).pack()
    
    def create_result_section(self, parent):
        """Creates the result display section."""
        separator = ttk.Separator(parent, orient='horizontal')
        separator.pack(fill='x', pady=20)
        
        # Result label with special styling for effects
        self.result_label = ttk.Label(
            parent,
            textvariable=self.result_var,
            font=("Arial", 14, "bold"),
            foreground="darkgreen",
            background="lightyellow",
            padding=15,
            relief="solid",
            borderwidth=2
        )
        self.result_label.pack(pady=10)
    
    def create_utility_section(self, parent):
        """Creates the utility buttons section."""
        utility_frame = ttk.Frame(parent)
        utility_frame.pack(pady=15)
        
        ttk.Button(
            utility_frame,
            text="Clear All 🔄",
            command=self.clear_all,
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            utility_frame,
            text="Exit Calculator ❌",
            command=self.safe_exit,
            width=18
        ).pack(side=tk.LEFT, padx=5)
    
    def perform_calculation(self, operation_name, operation_func):
        """Generic function to perform calculations with error handling."""
        num1_str = self.num1_var.get()
        num2_str = self.num2_var.get()
        
        # Validate inputs
        is_valid1, num1 = Calculator.validate_input(num1_str)
        is_valid2, num2 = Calculator.validate_input(num2_str)
        
        if not is_valid1 or not is_valid2:
            self.result_var.set("Please enter valid numbers.")
            return
        
        try:
            result = operation_func(num1, num2)
            
            # Format result
            if result.is_integer():
                result_text = f"Result: {int(result)}"
            else:
                result_text = f"Result: {result:.6f}".rstrip('0').rstrip('.')
            
            self.result_var.set(result_text)
            print(f"{operation_name}: {num1} and {num2} = {result}")
            
            # Clear input boxes after successful operation
            self.clear_inputs_and_focus()
            
        except ZeroDivisionError:
            # Trigger the special division by zero effect
            print("Division by zero detected - triggering special effect!")
            SpecialEffects.division_by_zero_effect(self.root, self.result_label)
            
        except Exception as e:
            self.result_var.set("Error in calculation.")
            print(f"Calculation error: {e}")
    
    def clear_inputs_and_focus(self):
        """Clears input fields and returns focus to first field."""
        self.num1_var.set("")
        self.num2_var.set("")
        self.num1_entry.focus()
    
    def add_numbers(self):
        """Performs addition operation."""
        self.perform_calculation("Addition", Calculator.add)
    
    def subtract_numbers(self):
        """Performs subtraction operation."""
        self.perform_calculation("Subtraction", Calculator.subtract)
    
    def multiply_numbers(self):
        """Performs multiplication operation."""
        self.perform_calculation("Multiplication", Calculator.multiply)
    
    def divide_numbers(self):
        """Performs division operation."""
        self.perform_calculation("Division", Calculator.divide)
    
    def clear_all(self):
        """Clears all input fields and result display."""
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("Result will appear here")
        self.num1_entry.focus()
        
        # Reset any visual effects
        try:
            self.root.configure(bg='#f0f0f0')
            self.result_label.configure(
                background="lightyellow",
                foreground="darkgreen",
                font=("Arial", 14, "bold")
            )
        except tk.TclError:
            pass
        print("All fields cleared")
    
    def safe_exit(self):
        """Safely exits the application."""
        print("Closing Enhanced Calculator...")
        try:
            self.root.quit()
            self.root.destroy()
        except tk.TclError:
            pass
    
    def run(self):
        """Starts the calculator application."""
        print("Starting Enhanced Calculator with Division and Special Effects...")
        print("=" * 60)
        print("⚠️  WARNING: Division by zero will trigger visual effects!")
        print("🎭 Get ready for a show if you try to divide by zero!")
        print("=" * 60)
        
        # Create and configure the application
        self.create_main_window()
        self.setup_variables()
        self.create_ui()
        
        print("Enhanced Calculator application ready!")
        print("Features:")
        print("✅ Four arithmetic operations (Add, Subtract, Multiply, Divide)")
        print("✅ Input validation and error handling")
        print("✅ Special animated effects for division by zero")
        print("✅ Professional UI with visual feedback")
        print("✅ Auto-clear functionality after successful operations")
        print("✅ Exit button and menu system")
        print("\\nTry dividing by zero for a surprise! 😈")
        
        # Start the GUI event loop
        self.root.mainloop()
        
        print("Enhanced Calculator application closed!")


# ====================================================================
# MAIN APPLICATION ENTRY POINT
# ====================================================================

def main():
    """Main function that creates and runs the enhanced calculator application."""
    app = CalculatorApp()
    app.run()


# ====================================================================
# PROGRAM EXECUTION
# ====================================================================

if __name__ == "__main__":
    main()


# ====================================================================
# TEAM NOTES - REFACTORED VERSION
# ====================================================================

"""
REFACTORED CALCULATOR IMPLEMENTATION NOTES:

🎯 REFACTORING IMPROVEMENTS:
1. ✅ Created CalculatorApp class for better organization
2. ✅ Separated concerns into logical methods
3. ✅ Fixed all indentation and syntax errors
4. ✅ Improved code readability and maintainability
5. ✅ Removed duplicate/unused code
6. ✅ Better error handling and state management
7. ✅ Cleaner separation of UI and business logic

🔧 STRUCTURAL IMPROVEMENTS:
- Main application logic now in CalculatorApp class
- Clear separation of UI creation methods
- Better organization of event handlers
- Simplified main() function
- Proper encapsulation of variables and methods
- Thread-safe animation using root.after()

📈 CODE QUALITY ENHANCEMENTS:
- Consistent naming conventions
- Proper docstrings for all methods
- Better error handling throughout
- Cleaner code structure and flow
- Easier to maintain and extend
- Follows Python best practices

⚡ FUNCTIONALITY PRESERVED:
- All original features working correctly
- Division by zero special effects
- Auto-clear after successful operations
- Menu system with keyboard shortcuts
- Professional UI with visual feedback
- Input validation and error handling

🚀 EASIER TO EXTEND:
- Modular design makes adding features simple
- Clear separation of concerns
- Well-documented methods
- Reusable components
- Maintainable codebase
"""
