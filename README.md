# Password Complexity Checker

A comprehensive Python tool for assessing password strength and complexity. This project provides both a command-line interface and a modern GUI application to help users create and evaluate strong passwords.

## Features

###  Password Analysis
- **Length Assessment**: Evaluates password length (minimum 8 characters recommended)
- **Character Variety**: Checks for uppercase, lowercase, numbers, and special characters
- **Pattern Detection**: Identifies common weak patterns (sequential, repeated, keyboard patterns)
- **Entropy Calculation**: Measures password randomness and complexity
- **Common Password Detection**: Flags known weak passwords

###  Strength Levels
- **Very Weak**: Score < 10
- **Weak**: Score 10-19
- **Fair**: Score 20-34
- **Good**: Score 35-49
- **Strong**: Score 50-69
- **Very Strong**: Score 70+

### 🖥️ User Interfaces
- **Command Line Interface**: Simple text-based interface
- **GUI Application**: Modern tkinter-based graphical interface with real-time feedback
- **Password Generator**: Built-in strong password generator

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd password-complexity-checker
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package (optional)**
   ```bash
   pip install -e .
   ```

## Usage

### Command Line Interface

Run the command-line version:
```bash
python password_checker.py
```

Or use the installed command:
```bash
password-checker
```

### GUI Application

Launch the graphical interface:
```bash
python password_gui.py
```

Or use the installed command:
```bash
password-checker-gui
```

### Programmatic Usage

```python
from password_checker import PasswordChecker

# Create checker instance
checker = PasswordChecker()

# Check a password
result = checker.check_password("MySecure123!")

print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}/100")
print(f"Strong: {result['is_strong']}")
print("Feedback:")
for item in result['feedback']:
    print(f"  • {item}")
```

## Project Structure

```
password-complexity-checker/
├── password_checker.py      # Main password checking logic
├── password_gui.py          # GUI application
├── test_password_checker.py # Comprehensive test suite
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
├── pyproject.toml          # Modern Python project configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=password_checker

# Run specific test file
python test_password_checker.py
```

### Test Coverage
The test suite includes:
- Unit tests for all password checking functions
- Edge case testing (empty passwords, very long passwords, unicode)
- Performance testing
- Integration testing
- Pattern detection testing

## Development

### Code Quality Tools

The project includes several code quality tools:

```bash
# Format code with Black
black .

# Lint with flake8
flake8 .

# Type checking with mypy
mypy password_checker.py

# Run all quality checks
python -m pytest --cov=password_checker --flake8 --mypy
```

### Adding New Features

1. **Password Rules**: Add new validation rules in `PasswordChecker` class
2. **GUI Features**: Extend `PasswordCheckerGUI` class
3. **Tests**: Add corresponding tests in `test_password_checker.py`

## Password Strength Criteria

### Scoring System (0-100 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Length | 0-20 | 6+ chars (5pts), 8+ chars (10pts), 12+ chars (15pts), 16+ chars (20pts) |
| Character Variety | 0-25 | Lowercase (5pts), Uppercase (5pts), Digits (5pts), Special (10pts) |
| Pattern Analysis | 0-20 | Penalties for weak patterns, bonuses for good patterns |
| Entropy | 0-20 | Calculated based on character set size and length |

### Weak Pattern Detection

- **Common Passwords**: Dictionary of known weak passwords
- **Sequential Characters**: abc, 123, etc.
- **Repeated Characters**: aaa, 111, etc.
- **Keyboard Patterns**: qwerty, asdf, etc.
- **Personal Info**: Basic pattern detection

## Security Considerations

⚠️ **Important Security Notes**:

1. **Local Processing**: All password analysis is done locally - passwords are never transmitted
2. **No Storage**: Passwords are not stored or logged
3. **Educational Purpose**: This tool is for educational and personal use
4. **Real Security**: For production systems, use established security libraries

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Inspired by modern password security best practices
- Built with Python standard library and tkinter
- Tested with pytest and coverage tools

## Changelog

### Version 1.0.0
- Initial release
- Core password checking functionality
- GUI application
- Comprehensive test suite
- Command-line interface
- Password generator

## Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the documentation
- Review the test cases for usage examples

---

**Remember**: Always use strong, unique passwords for your accounts and consider using a reputable password manager for better security!
