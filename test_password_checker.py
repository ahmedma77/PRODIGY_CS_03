"""
Test suite for Password Complexity Checker

Tests core functionality including edge cases and different password types.
"""

import unittest
from password_checker import PasswordChecker, PasswordStrength


class TestPasswordChecker(unittest.TestCase):
    """Test cases for PasswordChecker class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.checker = PasswordChecker()
    
    def test_empty_password(self):
        """Test empty password handling"""
        result = self.checker.check_password("")
        self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK.value)
        self.assertEqual(result['score'], 0)
        self.assertIn("Password cannot be empty", result['feedback'])
    
    def test_none_password(self):
        """Test None password handling"""
        result = self.checker.check_password(None)
        self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK.value)
        self.assertEqual(result['score'], 0)
    
    def test_very_weak_passwords(self):
        """Test very weak passwords"""
        weak_passwords = ["123", "abc", "123456"]
        
        for password in weak_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK.value)
                self.assertLess(result['score'], 5)
    
    def test_weak_passwords(self):
        """Test weak passwords"""
        weak_passwords = ["password", "a", "12", "qwerty", "abc123"]
        
        for password in weak_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertIn(result['strength'], [PasswordStrength.VERY_WEAK.value, PasswordStrength.WEAK.value])
                self.assertLess(result['score'], 10)
    
    def test_fair_passwords(self):
        """Test fair passwords"""
        fair_passwords = ["password123", "MyPassword", "test1234"]
        
        for password in fair_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertIn(result['strength'], [PasswordStrength.FAIR.value, PasswordStrength.GOOD.value])
                self.assertGreaterEqual(result['score'], 10)
    
    def test_good_passwords(self):
        """Test good passwords"""
        good_passwords = ["MyPass123", "Secure123!", "GoodPass1"]
        
        for password in good_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertIn(result['strength'], [PasswordStrength.GOOD.value, PasswordStrength.STRONG.value])
                self.assertGreaterEqual(result['score'], 20)
    
    def test_strong_passwords(self):
        """Test strong passwords"""
        strong_passwords = ["MySecure123!", "P@ssw0rd2024", "Str0ng!Pass"]
        
        for password in strong_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertIn(result['strength'], [PasswordStrength.STRONG.value, PasswordStrength.VERY_STRONG.value])
                self.assertGreaterEqual(result['score'], 30)
    
    def test_very_strong_passwords(self):
        """Test very strong passwords"""
        very_strong_passwords = ["MyV3ryS3cur3P@ssw0rd!", "C0mpl3x!P@ss2024", "Str0ng!P@ssw0rd#2024"]
        
        for password in very_strong_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertIn(result['strength'], [PasswordStrength.STRONG.value, PasswordStrength.VERY_STRONG.value])
                self.assertGreaterEqual(result['score'], 30)
    
    def test_length_scoring(self):
        """Test length-based scoring"""
        # Test different lengths
        test_cases = [
            ("short", 0),      # < 6 chars
            ("short1", 5),     # 6-7 chars
            ("password", 5),   # 8-11 chars
            ("password123", 10) # 12+ chars
        ]
        
        for password, expected_min_score in test_cases:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                # Length score should be at least the expected minimum
                self.assertGreaterEqual(result['score'], expected_min_score)
    
    def test_character_variety_scoring(self):
        """Test character variety scoring"""
        # Test different character combinations
        test_cases = [
            ("lowercase", 5),      # only lowercase
            ("UPPERCASE", 5),      # only uppercase
            ("123456789", 0),      # only digits (but sequential)
            ("lowerUPPER", 10),    # lowercase + uppercase
            ("lower123", 10),      # lowercase + digits
            ("UPPER123", 10),      # uppercase + digits
            ("lowerUPPER123", 15), # lowercase + uppercase + digits
            ("lowerUPPER123!", 20) # all types
        ]
        
        for password, expected_min_score in test_cases:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertGreaterEqual(result['score'], expected_min_score)
    
    def test_common_password_detection(self):
        """Test detection of common passwords"""
        common_passwords = ["123456", "qwerty", "admin", "letmein"]
        
        for password in common_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK.value)
                self.assertLess(result['score'], 5)
    
    def test_sequential_character_detection(self):
        """Test detection of sequential characters"""
        sequential_passwords = ["abc123", "def456", "123abc", "xyz789"]
        
        for password in sequential_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                # Should have lower score due to sequential pattern
                self.assertLess(result['score'], 20)
    
    def test_repeated_character_detection(self):
        """Test detection of repeated characters"""
        repeated_passwords = ["aaa123", "111abc", "xxx999", "mmm111"]
        
        for password in repeated_passwords:
            with self.subTest(password=password):
                result = self.checker.check_password(password)
                # Should have lower score due to repeated pattern
                self.assertLess(result['score'], 25)
    
    
    def test_feedback_generation(self):
        """Test feedback generation"""
        result = self.checker.check_password("weak")
        
        self.assertIsInstance(result['feedback'], list)
        self.assertGreater(len(result['feedback']), 0)
        
        # Check for specific feedback messages
        feedback_text = " ".join(result['feedback'])
        self.assertIn("short", feedback_text.lower())
    
    def test_strong_password_feedback(self):
        """Test feedback for strong passwords"""
        result = self.checker.check_password("MyV3ryS3cur3P@ssw0rd!")
        
        self.assertTrue(result['is_strong'])
        self.assertIn(result['strength'], [PasswordStrength.STRONG.value, PasswordStrength.VERY_STRONG.value])
        
        # Should have positive feedback
        feedback_text = " ".join(result['feedback'])
        self.assertIn("strong", feedback_text.lower())
    
    def test_unicode_password(self):
        """Test handling of unicode passwords"""
        unicode_password = "pássw0rd123!"
        result = self.checker.check_password(unicode_password)
        
        self.assertIsInstance(result, dict)
        self.assertIn('strength', result)
        self.assertIn('score', result)
        self.assertIn('feedback', result)
    
    def test_very_long_password(self):
        """Test handling of very long passwords"""
        long_password = "A" * 200  # 200 characters
        result = self.checker.check_password(long_password)
        
        self.assertIsInstance(result, dict)
        # Should still work without errors
        self.assertGreaterEqual(result['score'], 0)
    
    def test_special_characters(self):
        """Test various special characters"""
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        for char in special_chars:
            password = f"test{char}123"
            with self.subTest(char=char):
                result = self.checker.check_password(password)
                self.assertIsInstance(result, dict)
                self.assertIn('strength', result)


class TestPasswordStrengthEnum(unittest.TestCase):
    """Test cases for PasswordStrength enum"""
    
    def test_enum_values(self):
        """Test enum values"""
        self.assertEqual(PasswordStrength.VERY_WEAK.value, "Very Weak")
        self.assertEqual(PasswordStrength.WEAK.value, "Weak")
        self.assertEqual(PasswordStrength.FAIR.value, "Fair")
        self.assertEqual(PasswordStrength.GOOD.value, "Good")
        self.assertEqual(PasswordStrength.STRONG.value, "Strong")
        self.assertEqual(PasswordStrength.VERY_STRONG.value, "Very Strong")


if __name__ == "__main__":
    # Run unit tests
    unittest.main(verbosity=2)
