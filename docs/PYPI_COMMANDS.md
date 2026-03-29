# Step-by-Step: Publish Your Package to PyPI

Complete commands to follow in order.

---

## 🚀 QUICK START (5 Steps)

### Step 1: Clone Your Repo
```bash
git clone https://github.com/HADIL19/Pattern-Searching.git
cd Pattern-Searching
```

### Step 2: Add setup.py and pyproject.toml
Copy the provided `setup.py` and `pyproject.toml` files to your repo root.

### Step 3: Create __init__.py Files (if missing)

**Create: algorithms/__init__.py**
```python
"""Pattern Searching Algorithms Package"""
__version__ = "1.0.0"
__author__ = "HADIL19"
```

**Create: algorithms/single_pattern/__init__.py**
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

**Create: algorithms/multiple_pattern/__init__.py**
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

### Step 4: Install Build Tools
```bash
pip install build twine
```

### Step 5: Build Distribution
```bash
python -m build
```

This creates a `dist/` folder with your package ready to share.

---

## 📤 PUBLISH TO PyPI (2 Options)

### OPTION A: Publish to Real PyPI (Everyone can install)

1. **Create PyPI Account**
   - Go to https://pypi.org/account/register/
   - Create account
   - Create API token in account settings
   - Copy your token

2. **Upload to PyPI**
   ```bash
   twine upload dist/*
   ```
   When asked for username, type: `__token__`
   When asked for password, paste your token

3. **Done!** Anyone can now install:
   ```bash
   pip install pattern-searching
   ```

### OPTION B: Test First with Test PyPI (Recommended)

1. **Create Test PyPI Account**
   - Go to https://test.pypi.org/account/register/
   - Create account
   - Create API token

2. **Upload to Test PyPI**
   ```bash
   twine upload -r testpypi dist/*
   ```

3. **Test Installation**
   ```bash
   pip install -i https://test.pypi.org/simple/ pattern-searching
   ```

4. **If it works, upload to real PyPI**
   ```bash
   twine upload dist/*
   ```

---

## 🔄 WORKFLOW

### Initial Setup (Do Once)
```bash
# 1. Install tools
pip install build twine

# 2. Navigate to repo
cd Pattern-Searching

# 3. Test locally
pip install -e .

# 4. Verify imports work
python -c "from algorithms.single_pattern import boyer_moore_search; print('✓ Import works')"

# 5. Build distribution
python -m build

# 6. Upload to PyPI
twine upload dist/*
```

### Updates (For Future Versions)
```bash
# 1. Update version in setup.py or pyproject.toml
# Change: version="1.0.0" to version="1.0.1"

# 2. Rebuild
python -m build

# 3. Upload
twine upload dist/*
```

---

## ✅ VERIFY IT WORKS

After uploading, test it in a fresh environment:

```bash
# Create new folder
mkdir test_install
cd test_install

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install your package
pip install pattern-searching

# Test it
python << 'EOF'
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick

# Test 1
boyer_moore_search("Hello World", "World")

# Test 2
ac = AhoCorasick(["Hello", "World"])
ac.search("Hello World")

print("\n✅ Everything works!")
EOF
```

---

## 🎯 FINAL RESULT

Your package is now available to everyone:

```bash
# Anywhere in the world, users can install it
pip install pattern-searching

# And use it in their code
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick

boyer_moore_search("text", "pattern")
```

---

## 🐛 TROUBLESHOOTING

### Error: "twine: command not found"
```bash
pip install twine
```

### Error: "No module named 'build'"
```bash
pip install build
```

### Error: "Invalid authentication"
- Make sure you created a PyPI account at https://pypi.org
- Created an API token
- Used correct token

### Error: "File already exists"
- You already published this version
- Increment version number in setup.py: `1.0.1` → `1.0.2`
- Rebuild: `python -m build`
- Upload again

---

## 📋 CHECKLIST

- [ ] Have GitHub repo with your code
- [ ] Add setup.py to root
- [ ] Add pyproject.toml to root
- [ ] Create __init__.py files
- [ ] Update email in setup.py
- [ ] Create PyPI account
- [ ] Install build and twine
- [ ] Test locally: `pip install -e .`
- [ ] Build: `python -m build`
- [ ] Upload: `twine upload dist/*`
- [ ] Test in clean environment
- [ ] Share the command: `pip install pattern-searching`

---

## 🎉 YOU'RE DONE!

Your package is now published and installable via pip.

Share with the world:
> "Install my pattern searching package: `pip install pattern-searching`"

---

**Questions? Check:**
- https://packaging.python.org/
- https://pypi.org/help/
- https://twine.readthedocs.io/
