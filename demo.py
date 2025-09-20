"""
Demo script for Password Complexity Checker

This script demonstrates various password checking scenarios.
"""

from password_checker import PasswordChecker


def print_separator(title):
    """Print a formatted separator with title"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print('='*60)


def print_result(password, result):
    """Print formatted password check result"""
    print(f"\nPassword: '{password}'")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/50")
    print(f"Strong: {'Yes' if result['is_strong'] else 'No'}")
    print("Feedback:")
    for item in result['feedback']:
        print(f"  • {item}")


def main():
    """Main demo function"""
    print("Password Complexity Checker - Demo")
    print("=" * 50)
    
    # Initialize checker
    checker = PasswordChecker()
    
    # Demo passwords with different strength levels
    demo_passwords = [
        # Very Weak
        ("123", "Very Weak Password"),
        ("abc", "Very Weak Password"),
        ("password", "Common Weak Password"),
        
        # Weak
        ("password123", "Weak Password"),
        ("qwerty", "Keyboard Pattern"),
        ("abc123", "Sequential Pattern"),
        
        # Fair
        ("MyPassword", "Fair Password"),
        ("test1234", "Fair Password"),
        ("Secure123", "Fair Password"),
        
        # Good
        ("MyPass123", "Good Password"),
        ("Secure123!", "Good Password with Special Char"),
        ("GoodPass1", "Good Password"),
        
        # Strong
        ("MySecure123!", "Strong Password"),
        ("P@ssw0rd2024", "Strong Password"),
        ("Str0ng!Pass", "Strong Password"),
        
        # Very Strong
        ("MyV3ryS3cur3P@ssw0rd!", "Very Strong Password"),
        ("C0mpl3x!P@ss2024", "Very Strong Password"),
        ("Str0ng!P@ssw0rd#2024", "Very Strong Password"),
    ]
    
    # Display results
    for password, description in demo_passwords:
        print(f"\n{description}:")
        result = checker.check_password(password)
        print_result(password, result)
    
    # Special cases demo
    print_separator("Special Cases")
    
    special_cases = [
        ("", "Empty Password"),
        ("a" * 200, "Very Long Password (200 chars)"),
        ("pássw0rd123!", "Unicode Password"),
        ("A" * 50, "Repeated Character Pattern"),
        ("qwertyuiop", "Keyboard Row Pattern"),
        ("1234567890", "Sequential Numbers"),
    ]
    
    for password, description in special_cases:
        print(f"\n{description}:")
        if password == "":
            print("Password: (empty)")
        elif len(password) > 50:
            print(f"Password: '{password[:20]}...' ({len(password)} chars)")
        else:
            print(f"Password: '{password}'")
        
        result = checker.check_password(password)
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}/50")
        print(f"Strong: {'Yes' if result['is_strong'] else 'No'}")
        print("Feedback:")
        for item in result['feedback']:
            print(f"  • {item}")
    
    # Summary
    print_separator("Demo Summary")
    print("This demo showcased:")
    print("• Different password strength levels")
    print("• Pattern detection (sequential, repeated)")
    print("• Special character handling")
    print("• Unicode password support")
    print("• Edge case handling")
    print("\nThe Password Complexity Checker provides comprehensive")
    print("password analysis to help users create strong, secure passwords.")


if __name__ == "__main__":
    main()
