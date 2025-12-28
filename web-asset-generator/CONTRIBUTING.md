# Contributing to Web Asset Generator

Thank you for your interest in contributing to Web Asset Generator! This document provides guidelines and instructions for contributing.

## 🌟 How to Contribute

We welcome contributions of all kinds:
- 🐛 Bug reports and fixes
- ✨ New features
- 📖 Documentation improvements
- 🎨 Design enhancements
- 🧪 Tests and validation
- 💡 Ideas and suggestions

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## 📜 Code of Conduct

### Our Standards

- **Be respectful**: Treat everyone with respect and kindness
- **Be inclusive**: Welcome contributors of all backgrounds and skill levels
- **Be constructive**: Provide helpful feedback and suggestions
- **Be patient**: Remember that everyone was a beginner once

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or insulting/derogatory comments
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Git
- Basic understanding of image processing (helpful but not required)

### Finding Issues to Work On

1. Check the [issue tracker](https://github.com/alonw0/web-asset-generator/issues)
2. Look for issues labeled `good first issue` or `help wanted`
3. Comment on the issue to let others know you're working on it
4. If you have a new idea, create an issue first to discuss it

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/web-asset-generator.git
cd web-asset-generator
```

### 2. Install Dependencies

```bash
# Core dependencies
pip install Pillow

# Optional dependencies (for emoji support)
pip install pilmoji 'emoji<2.0.0'
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests

## 🔨 Making Changes

### Project Structure

```
scripts/
├── generate_favicons.py    # Favicon generation logic
├── generate_og_images.py   # Social image generation logic
├── emoji_utils.py          # Emoji utilities
└── lib/
    └── validators.py       # Validation functions
```

### Key Files to Understand

1. **SKILL.md**: Claude Skill definition with workflows and question patterns
2. **CLAUDE.md**: Development guidance and architecture notes
3. **scripts/lib/validators.py**: Validation logic for file sizes, dimensions, etc.
4. **scripts/emoji_utils.py**: Emoji suggestion and rendering engine

### Common Development Tasks

#### Adding a New Platform

1. Update `PLATFORM_REQUIREMENTS` in `scripts/lib/validators.py`:
   ```python
   'newplatform': {
       'max_file_size': 5 * 1024 * 1024,  # 5MB
       'recommended_size': (1200, 600),
       'min_size': (600, 300),
       'aspect_ratio': 2.0,
       'formats': ['png', 'jpg', 'jpeg'],
   }
   ```

2. Update documentation in `references/specifications.md`
3. Add platform to validation logic
4. Update SKILL.md with new platform option

#### Adding New Emoji Categories

1. Update `EMOJI_DATABASE` in `scripts/emoji_utils.py`:
   ```python
   "🎸": ("guitar", ["music", "guitar", "rock", "band"], "music"),
   ```

2. Add category to suggestion engine
3. Test with `--suggest` flag

#### Improving Validation

1. Add new validation function to `scripts/lib/validators.py`
2. Integrate into `generate_og_images.py` or `generate_favicons.py`
3. Add tests and examples
4. Document in SKILL.md

## 📤 Submitting Changes

### Before Submitting

1. **Test your changes**:
   ```bash
   # Test favicon generation
   python scripts/generate_favicons.py test_logo.png output/ all --validate

   # Test social images
   python scripts/generate_og_images.py output/ --text "Test" --validate

   # Test emoji features
   python scripts/generate_favicons.py --suggest "test" output/ all
   python scripts/generate_favicons.py --emoji "🚀" output/ all
   ```

2. **Check code quality**:
   - Follow PEP 8 style guidelines
   - Add docstrings to functions
   - Keep functions focused and modular
   - Use type hints where appropriate

3. **Update documentation**:
   - Update README.md if adding features
   - Update SKILL.md for Claude Skill changes
   - Add comments for complex logic

### Creating a Pull Request

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add support for Pinterest images"
   ```

   **Commit message format**:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes (formatting, etc.)
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance tasks

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request on GitHub**:
   - Provide a clear title and description
   - Reference any related issues (e.g., "Fixes #123")
   - Include screenshots for visual changes
   - List testing steps

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Related Issues
Fixes #(issue number)

## Testing
- [ ] Tested favicon generation
- [ ] Tested social image generation
- [ ] Tested emoji features
- [ ] Tested validation
- [ ] All examples work correctly

## Screenshots (if applicable)
Add screenshots of generated assets

## Checklist
- [ ] Code follows project style guidelines
- [ ] Documentation updated
- [ ] All tests pass
- [ ] Commit messages are clear
```

## 📐 Coding Standards

### Python Style

Follow [PEP 8](https://pep8.org/) guidelines:

```python
# Good
def calculate_font_size(text: str, base_size: int = 120) -> int:
    """
    Calculate optimal font size based on text length.

    Args:
        text: The text to be displayed
        base_size: Base font size in pixels

    Returns:
        Calculated font size in pixels
    """
    text_length = len(text)
    if text_length <= 20:
        return int(base_size * 1.2)
    return base_size
```

### Validation Results

Use the `ValidationResult` class for consistent output:

```python
from lib.validators import ValidationResult

# Success
result = ValidationResult(
    True,
    "File size 0.5MB is within limits",
    'success'
)

# Warning
result = ValidationResult(
    True,
    "File size is close to limit",
    'warning'
)

# Error
result = ValidationResult(
    False,
    "File size exceeds maximum",
    'error'
)
```

### Error Handling

Always provide helpful error messages:

```python
# Good
if not source_path.exists():
    raise FileNotFoundError(
        f"Source image not found: {source_path}\n"
        f"Please check the file path and try again."
    )

# Bad
if not source_path.exists():
    raise Exception("File not found")
```

## 🧪 Testing

### Manual Testing Checklist

Before submitting, test these scenarios:

**Favicons:**
- [ ] Generate from image file
- [ ] Generate from emoji
- [ ] Generate with custom background
- [ ] Validate output files
- [ ] Check all sizes are correct
- [ ] Verify HTML tags are correct

**Social Images:**
- [ ] Generate from text
- [ ] Generate from image
- [ ] Generate with logo
- [ ] Test custom colors
- [ ] Validate dimensions and file sizes
- [ ] Check contrast ratios

**Emoji Features:**
- [ ] Test emoji suggestions
- [ ] Test emoji rendering
- [ ] Test with different backgrounds
- [ ] Verify emoji database matches

**Validation:**
- [ ] File size checks work
- [ ] Dimension validation works
- [ ] Format validation works
- [ ] Contrast validation works
- [ ] Error messages are clear

### Test with Different Inputs

```bash
# Test with various text lengths
python scripts/generate_og_images.py output/ --text "Hi"
python scripts/generate_og_images.py output/ --text "Medium length text here"
python scripts/generate_og_images.py output/ --text "This is a very long text that should automatically adjust font size to fit properly"

# Test with different colors
python scripts/generate_og_images.py output/ --text "Test" --bg-color "#FF5733"
python scripts/generate_og_images.py output/ --text "Test" --bg-color "white" --text-color "black"

# Test emoji edge cases
python scripts/generate_favicons.py --suggest "xyz abc def"
python scripts/generate_favicons.py --emoji "🎨" output/ favicon
```

## 📚 Documentation

### Docstring Format

Use Google-style docstrings:

```python
def validate_dimensions(file_path: str, platform: str = 'facebook') -> ValidationResult:
    """
    Validate image dimensions against platform requirements.

    Args:
        file_path: Path to the image file
        platform: Platform name (facebook, twitter, linkedin)

    Returns:
        ValidationResult with pass/fail status and descriptive message

    Raises:
        FileNotFoundError: If the image file doesn't exist

    Example:
        >>> result = validate_dimensions('og-image.png', 'facebook')
        >>> print(result.message)
        'Dimensions 1200x630 match Facebook recommended size'
    """
```

### Documentation Files to Update

When making changes, update relevant documentation:

- **README.md**: User-facing features and examples
- **SKILL.md**: Claude Skill workflows and patterns
- **CLAUDE.md**: Development notes and architecture
- **specifications.md**: Platform requirements
- **Inline comments**: Complex logic explanations

## 🎯 Priority Areas

We're especially looking for contributions in these areas:

### High Priority
- 🔴 Unit tests for validation functions
- 🔴 Integration tests for end-to-end workflows
- 🔴 Error handling improvements
- 🔴 Performance optimizations

### Medium Priority
- 🟡 Additional platform support (Pinterest, Instagram)
- 🟡 WebP and AVIF format support
- 🟡 PWA manifest.json generation
- 🟡 Batch processing capabilities

### Nice to Have
- 🟢 Additional emoji categories
- 🟢 Preview HTML generation
- 🟢 Dark mode variants
- 🟢 Custom font support

## 💬 Getting Help

- **Questions**: Open a [discussion](https://github.com/alonw0/web-asset-generator/discussions)
- **Bugs**: Create an [issue](https://github.com/alonw0/web-asset-generator/issues)
- **Ideas**: Start a discussion or create a feature request issue

## 🏆 Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Mentioned in the project documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Web Asset Generator!** 🎉

Your contributions help make web development easier for everyone.
