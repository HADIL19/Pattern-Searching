# How to Make Your Package Installable via pip

Complete guide to make your Pattern-Searching package installable with `pip install`

---

## 📦 What You Need

Your repo structure should look like this:

```
Pattern-Searching/
├── README.md
├── LICENSE
├── setup.py                    # ← Configuration for pip
├── pyproject.toml             # ← Modern alternative
├── algorithms/
│   ├── __init__.py
│   ├── single_pattern/
│   │   ├── __init__.py
│   │   ├── naive.py
│   │   ├── boyer_moore.py
│   │   ├── morris_pratt.py
│   │   └── rabin_karp.py
│   └── multiple_pattern/
│       ├── __init__.py
│       ├── aho_corasick.py
│       ├── rabin_karpe_pattern.py
│       ├── wu_manber.py
│       └── commentz_walter.py
```

---

## ✅ Step 1: Create Proper __init__.py Files

### algorithms/__init__.py
```python
"""Pattern Searching Algorithms Package"""

__version__ = "1.0.0"
__author__ = "HADIL19"

from . import single_pattern
from . import multiple_pattern

__all__ = ['single_pattern', 'multiple_pattern']
```

### algorithms/single_pattern/__init__.py
```python
"""Single Pattern Searching Algorithms"""

from .naive import naive_search
from .morris_pratt import morris_pratt_search
from .boyer_moore import boyer_moore_search
from .rabin_karp import rabin_karp_search

__all__ = [
    'naive_search',
    'morris_pratt_search',
    'boyer_moore_search',
    'rabin_karp_search'
]
```

### algorithms/multiple_pattern/__init__.py
```python
"""Multiple Pattern Searching Algorithms"""

from .aho_corasick import AhoCorasick
from .rabin_karpe_pattern import rabin_karp_multiple
from .wu_manber import wu_manber
from .commentz_walter import commentz_walter

__all__ = [
    'AhoCorasick',
    'rabin_karp_multiple',
    'wu_manber',
    'commentz_walter'
]
```

---

## ✅ Step 2: Use One of the Config Files

### Option A: setup.py (Traditional)

Already provided in setup.py file. Just add it to your repo root.

**Edit these lines:**
```python
author="HADIL19",
author_email="your.email@example.com",  # ← Update with your email
```

### Option B: pyproject.toml (Modern)

Already provided in pyproject.toml file. Just add it to your repo root.

**Edit this line:**
```toml
authors = [
    {name = "HADIL19", email = "your.email@example.com"}  # ← Update
]
```

---

## ✅ Step 3: Test Locally (Before Publishing)

### Test Installation from GitHub

```bash
# Install directly from your GitHub repo
pip install git+https://github.com/HADIL19/Pattern-Searching.git

# In your script, use it like this:
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick
```

### Test Installation in Development Mode

```bash
# Clone your repo
git clone https://github.com/HADIL19/Pattern-Searching.git
cd Pattern-Searching

# Install in editable mode (for development)
pip install -e .

# Now you can import it from anywhere
python
>>> from algorithms.single_pattern import boyer_moore_search
>>> boyer_moore_search("hello world", "world")
Pattern found at index 6
```

---

## ✅ Step 4: Prepare for PyPI (Python Package Index)

### What is PyPI?
PyPI is the official repository for Python packages. When you upload there, anyone can do:
```bash
pip install pattern-searching
```

### Requirements

1. **PyPI Account** (free)
   - Go to https://pypi.org/account/register/
   - Create an account
   - Create an API token (under Account Settings)

2. **Install build tools**
   ```bash
   pip install build twine
   ```

3. **Update setup.py/pyproject.toml** with correct info
   - Your email
   - Project description
   - Links to GitHub

---

## ✅ Step 5: Build Distribution Files

```bash
# Navigate to your repo
cd Pattern-Searching

# Build the distribution
python -m build

# This creates a 'dist/' folder with:
# - pattern_searching-1.0.0-py3-none-any.whl
# - pattern_searching-1.0.0.tar.gz
```

---

## ✅ Step 6: Upload to PyPI

### For Testing (Test PyPI first!)

```bash
# Create ~/.pypirc file with your credentials
# Then upload to test PyPI
twine upload --repository testpypi dist/*

# Test install from test PyPI
pip install -i https://test.pypi.org/simple/ pattern-searching
```

### For Production (Real PyPI)

```bash
# Upload to real PyPI
twine upload dist/*

# Or provide username/password when prompted
twine upload dist/ -u __token__ -p pypi_your_token_here
```

---

## 🎉 After Publishing

Once published to PyPI, users can simply do:

```bash
pip install pattern-searching
```

Then in any Python script:

```python
# script.py
from algorithms.single_pattern import boyer_moore_search, naive_search
from algorithms.multiple_pattern import AhoCorasick

# Use it!
text = "The quick brown fox"
pattern = "fox"
boyer_moore_search(text, pattern)

# Or use multiple patterns
searcher = AhoCorasick(["quick", "fox"])
searcher.search(text)
```

---

## 📋 Complete Checklist

- [ ] Create proper `algorithms/__init__.py` files
- [ ] Add `setup.py` to repo root
- [ ] Add `pyproject.toml` to repo root (optional but recommended)
- [ ] Update email/author info
- [ ] Create PyPI account (https://pypi.org/account/register/)
- [ ] Create API token in PyPI account settings
- [ ] Install build tools: `pip install build twine`
- [ ] Test locally: `pip install -e .`
- [ ] Build: `python -m build`
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Test install: `pip install pattern-searching`

---

## 🚀 Quick Start Commands

```bash
# 1. Setup
pip install build twine

# 2. Test locally
pip install -e .

# 3. Build
python -m build

# 4. Upload (requires PyPI account)
twine upload dist/*

# 5. Anyone can now install with:
pip install pattern-searching
```

---

## 📝 Version Management

Each time you want to update your package:

1. Update version in `setup.py` or `pyproject.toml`:
   ```python
   version="1.0.1"  # Change from 1.0.0
   ```

2. Build again:
   ```bash
   python -m build
   ```

3. Upload:
   ```bash
   twine upload dist/*
   ```

---

## 🎯 Example Usage After Publishing

### Installation
```bash
pip install pattern-searching
```

### Basic Usage
```python
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick

# Single pattern
boyer_moore_search("Hello World", "World")
# Output: Pattern found at index 6

# Multiple patterns
ac = AhoCorasick(["Hello", "World"])
ac.search("Hello World")
# Output: Pattern 'Hello' found at index 0
#         Pattern 'World' found at index 6
```

---

## 🔗 Important Links

- **PyPI Main:** https://pypi.org
- **Test PyPI:** https://test.pypi.org
- **Build Docs:** https://packaging.python.org/
- **Twine Docs:** https://twine.readthedocs.io/

---

## ❓ FAQ

### Q: Can I test without publishing?
**A:** Yes! Use `pip install -e .` locally to test

### Q: How often can I update?
**A:** As often as you want, just increment the version number

### Q: Can I delete a version?
**A:** Not recommended, but you can "yank" versions on PyPI

### Q: Do I need both setup.py and pyproject.toml?
**A:** No, choose one. `pyproject.toml` is more modern, but `setup.py` is more compatible

### Q: How long until it's live?
**A:** Instant! Available on PyPI within seconds of upload

---

## 🎉 Final Result

After following these steps, anyone in the world can do:

```bash
pip install pattern-searching
```

And then use your package in their code!

```python
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick

# Your algorithms are now available to the world! 🌍
```

---

**Happy packaging! 🚀**
