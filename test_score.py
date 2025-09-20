from password_checker import PasswordChecker

checker = PasswordChecker()

# Test passwords to find one that gets 50/50
test_passwords = [
    "MyV3ryS3cur3P@ssw0rd!",
    "C0mpl3x!P@ss2024",
    "Str0ng!P@ssw0rd#2024",
    "P@ssw0rd123!",
    "MySecure123!",
    "VeryLongPassword123!@#",
    "SuperLongPassword123!@#$%",
    "UltraLongPassword123!@#$%^&*",
    "MegaLongPassword123!@#$%^&*()",
    "SuperMegaLongPassword123!@#$%^&*()_+",
    "UltraMegaSuperLongPassword123!@#$%^&*()_+-=",
    "TheUltimateLongPassword123!@#$%^&*()_+-=[]{}|;:,.<>?"
]

print("Testing passwords to find 50/50 score:")
print("=" * 50)

for password in test_passwords:
    result = checker.check_password(password)
    print(f"Password: {password}")
    print(f"Score: {result['score']}/50")
    print(f"Strength: {result['strength']}")
    print(f"Length: {len(password)}")
    print("-" * 30)
