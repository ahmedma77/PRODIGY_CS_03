"""
Password Complexity Checker - GUI Interface

A GUI application for checking password strength using tkinter.
Features real-time password analysis with visual feedback.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from password_checker import PasswordChecker, PasswordStrength


class PasswordCheckerGUI:
    """Main GUI application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Initialize password checker
        self.checker = PasswordChecker()
        
        # Create GUI elements
        self.create_widgets()
        
        # Bind events
        self.setup_events()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Password Complexity Checker", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Password input section
        self.create_password_input_section(main_frame)
        
        # Strength display section
        self.create_strength_display_section(main_frame)
        
        # Feedback section
        self.create_feedback_section(main_frame)
        
        # Buttons section
        self.create_buttons_section(main_frame)
    
    def create_password_input_section(self, parent):
        """Create password input section"""
        # Password label
        password_label = ttk.Label(parent, text="Enter Password:", font=("Arial", 12, "bold"))
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Password entry frame
        password_frame = ttk.Frame(parent)
        password_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Password entry with show/hide toggle
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(password_frame, textvariable=self.password_var, 
                                       show="*", font=("Arial", 12))
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Show/Hide button
        self.show_password_var = tk.BooleanVar()
        self.show_password_btn = ttk.Checkbutton(password_frame, text="Show", 
                                                variable=self.show_password_var,
                                                command=self.toggle_password_visibility)
        self.show_password_btn.pack(side=tk.RIGHT)
    
    def create_strength_display_section(self, parent):
        """Create strength display section"""
        # Strength label
        strength_label = ttk.Label(parent, text="Password Strength:", font=("Arial", 12, "bold"))
        strength_label.pack(anchor=tk.W, pady=(10, 5))
        
        # Strength display frame
        strength_frame = ttk.Frame(parent)
        strength_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Strength text
        self.strength_text = ttk.Label(strength_frame, text="Enter a password to check", 
                                      font=("Arial", 14, "bold"))
        self.strength_text.pack(side=tk.LEFT)
        
        # Score label
        self.score_text = ttk.Label(strength_frame, text="")
        self.score_text.pack(side=tk.RIGHT)
        
        # Progress bar
        self.strength_progress = ttk.Progressbar(strength_frame, length=400, 
                                                mode='determinate', maximum=50)
        self.strength_progress.pack(fill=tk.X, pady=(5, 0))
    
    def create_feedback_section(self, parent):
        """Create feedback section"""
        # Feedback label
        feedback_label = ttk.Label(parent, text="Feedback:", font=("Arial", 12, "bold"))
        feedback_label.pack(anchor=tk.W, pady=(10, 5))
        
        # Feedback text area
        self.feedback_text = scrolledtext.ScrolledText(parent, height=6, width=50, 
                                                      font=("Arial", 10), wrap=tk.WORD)
        self.feedback_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    def create_buttons_section(self, parent):
        """Create buttons section"""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(pady=10)
        
        # Check button
        self.check_btn = ttk.Button(buttons_frame, text="Check Password", 
                                   command=self.check_password)
        self.check_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = ttk.Button(buttons_frame, text="Clear", 
                                   command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Generate button
        self.generate_btn = ttk.Button(buttons_frame, text="Generate Strong Password", 
                                      command=self.generate_password)
        self.generate_btn.pack(side=tk.LEFT)
    
    
    def setup_events(self):
        """Setup event bindings"""
        # Bind password entry to real-time checking
        self.password_var.trace('w', self.on_password_change)
        
        # Bind Enter key to check password
        self.password_entry.bind('<Return>', lambda e: self.check_password())
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def on_password_change(self, *args):
        """Handle password change for real-time checking"""
        # Use threading to avoid blocking the GUI
        threading.Thread(target=self.real_time_check, daemon=True).start()
    
    def real_time_check(self):
        """Perform real-time password checking"""
        password = self.password_var.get()
        
        if len(password) > 0:
            result = self.checker.check_password(password)
            self.update_display(result)
        else:
            self.clear_display()
    
    def check_password(self):
        """Check password and display results"""
        password = self.password_var.get()
        
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to check.")
            return
        
        # Perform check
        result = self.checker.check_password(password)
        
        # Update display
        self.update_display(result)
    
    def update_display(self, result):
        """Update the display with check results"""
        # Update strength text and color
        strength = result['strength']
        score = result['score']
        
        self.strength_text.config(text=strength)
        self.score_text.config(text=f"Score: {score}/50")
        
        # Update progress bar
        self.strength_progress['value'] = score
        
        # Update feedback
        self.feedback_text.delete(1.0, tk.END)
        for item in result['feedback']:
            self.feedback_text.insert(tk.END, f"• {item}\n")
    
    def clear_display(self):
        """Clear the display"""
        self.strength_text.config(text="Enter a password to check")
        self.score_text.config(text="")
        self.strength_progress['value'] = 0
        self.feedback_text.delete(1.0, tk.END)
    
    def clear_all(self):
        """Clear all inputs and displays"""
        self.password_var.set("")
        self.clear_display()
    
    def generate_password(self):
        """Generate a strong password"""
        import secrets
        import string
        
        # Generate a strong password
        length = 16
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Set the generated password
        self.password_var.set(password)
        self.show_password_var.set(True)
        self.toggle_password_visibility()
        
        # Check the generated password
        self.check_password()
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = PasswordCheckerGUI(root)
    app.run()


if __name__ == "__main__":
    main()
