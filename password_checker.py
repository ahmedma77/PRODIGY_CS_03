"""
Password Complexity Checker

A tool that assesses password strength based on:
- Length requirements
- Character variety (uppercase, lowercase, numbers, special characters)
- Common password patterns
"""

import re
from typing import Dict, List
from enum import Enum


class PasswordStrength(Enum):
    """Password strength levels"""
    VERY_WEAK = "Very Weak"
    WEAK = "Weak"
    FAIR = "Fair"
    GOOD = "Good"
    STRONG = "Strong"
    VERY_STRONG = "Very Strong"


class PasswordChecker:
    """Main password complexity checker class"""
    
    def __init__(self):
        # Common weak passwords
        self.common_passwords = {
            "password", "123456", "123456789", "qwerty", "abc123",
            "password123", "admin", "letmein", "welcome", "monkey"
        }
        
    def check_password(self, password: str) -> Dict:
        """
        Check password strength based on length, character variety, and patterns
        
        Args:
            password (str): Password to analyze
            
        Returns:
            Dict: Analysis results with strength, score, and feedback
        """
        if not password:
            return self._create_result(PasswordStrength.VERY_WEAK, 0, ["Password cannot be empty"])
        
        # Basic checks
        length_score = self._check_length(password)
        char_variety_score = self._check_character_variety(password)
        pattern_score = self._check_patterns(password)
        
        # Calculate total score
        total_score = length_score + char_variety_score + pattern_score
        
        # Determine strength level
        strength = self._determine_strength(total_score)
        
        # Generate feedback
        feedback = self._generate_feedback(password, strength)
        
        return self._create_result(strength, total_score, feedback)
    
    def _check_length(self, password: str) -> int:
        """Check password length and award points"""
        length = len(password)
        
        if length < 6:
            return 0
        elif length < 8:
            return 5
        elif length < 12:
            return 10
        else:
            return 15
    
    def _check_character_variety(self, password: str) -> int:
        """Check for different character types"""
        score = 0
        
        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 5
        
        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 5
        
        # Check for digits
        if re.search(r'\d', password):
            score += 5
        
        # Check for special characters
        if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
            score += 5
        
        return score
    
    def _check_patterns(self, password: str) -> int:
        """Check for common patterns and weak passwords"""
        password_lower = password.lower()
        
        # Check against common passwords
        if password_lower in self.common_passwords:
            return -10
        
        # Check for sequential patterns
        if self._has_sequential_chars(password):
            return -5
        
        # Check for repeated characters
        if self._has_repeated_chars(password):
            return -5
        
        return 0
    
    
    def _has_sequential_chars(self, password: str) -> bool:
        """Check for sequential characters (abc, 123, etc.)"""
        for i in range(len(password) - 2):
            if (ord(password[i+1]) == ord(password[i]) + 1 and 
                ord(password[i+2]) == ord(password[i]) + 2):
                return True
        return False
    
    def _has_repeated_chars(self, password: str) -> bool:
        """Check for repeated characters"""
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return True
        return False
    
    
    def _determine_strength(self, score: int) -> PasswordStrength:
        """Determine password strength based on score"""
        if score < 5:
            return PasswordStrength.VERY_WEAK
        elif score < 10:
            return PasswordStrength.WEAK
        elif score < 20:
            return PasswordStrength.FAIR
        elif score < 30:
            return PasswordStrength.GOOD
        elif score < 40:
            return PasswordStrength.STRONG
        else:
            return PasswordStrength.VERY_STRONG
    
    def _generate_feedback(self, password: str, strength: PasswordStrength) -> List[str]:
        """Generate helpful feedback for the user"""
        feedback = []
        
        # Length feedback
        length = len(password)
        if length < 8:
            feedback.append(f"Password is too short ({length} characters). Use at least 8 characters.")
        elif length < 12:
            feedback.append(f"Consider using a longer password ({length} characters). 12+ characters recommended.")
        else:
            feedback.append(f"Good password length ({length} characters).")
        
        # Character variety feedback
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
        
        if not has_lower:
            feedback.append("Add lowercase letters (a-z)")
        if not has_upper:
            feedback.append("Add uppercase letters (A-Z)")
        if not has_digits:
            feedback.append("Add numbers (0-9)")
        if not has_special:
            feedback.append("Add special characters (!@#$%^&*)")
        
        # Pattern feedback
        if self._has_sequential_chars(password):
            feedback.append("Avoid sequential characters (abc, 123)")
        if self._has_repeated_chars(password):
            feedback.append("Avoid repeated characters (aaa, 111)")
        
        # Strength-specific feedback
        if strength in [PasswordStrength.VERY_WEAK, PasswordStrength.WEAK]:
            feedback.append("Password is too weak. Consider using a password manager.")
        elif strength == PasswordStrength.FAIR:
            feedback.append("Password is acceptable but could be stronger.")
        elif strength in [PasswordStrength.GOOD, PasswordStrength.STRONG, PasswordStrength.VERY_STRONG]:
            feedback.append("Great! This is a strong password.")
        
        return feedback
    
    def _create_result(self, strength: PasswordStrength, score: int, feedback: List[str]) -> Dict:
        """Create the final result dictionary"""
        return {
            'strength': strength.value,
            'score': score,
            'feedback': feedback,
            'is_strong': strength in [PasswordStrength.GOOD, PasswordStrength.STRONG, PasswordStrength.VERY_STRONG]
        }


def main():
    """Main function for command-line usage"""
    checker = PasswordChecker()
    
    print("Password Complexity Checker")
    print("=" * 30)
    
    while True:
        password = input("\nEnter password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
        
        result = checker.check_password(password)
        
        print(f"\nPassword Strength: {result['strength']}")
        print(f"Score: {result['score']}/50")
        print(f"Strong Password: {'Yes' if result['is_strong'] else 'No'}")
        print("\nFeedback:")
        for item in result['feedback']:
            print(f"  • {item}")


if __name__ == "__main__":
    main()
