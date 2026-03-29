# Pattern-Searching Quick Reference Card

Quick copy-paste examples for common use cases.

---

## ⚡ 30-Second Setup

```python
# Install
pip install -e .

# Import what you need
from algorithms.single_pattern import naive_search, boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick, rabin_karp_multiple
```

---

## 🎯 Copy-Paste Examples

### Example 1: Find One Pattern (Simple)
```python
from algorithms.single_pattern import naive_search

text = "Hello World Hello"
pattern = "Hello"
naive_search(text, pattern)
# Output: Pattern found at index 0
#         Pattern found at index 12
```

### Example 2: Find One Pattern (Fast)
```python
from algorithms.single_pattern import boyer_moore_search

text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
boyer_moore_search(text, pattern)
# Output: Pattern found at index 16
```

### Example 3: Find Multiple Patterns
```python
from algorithms.multiple_pattern import AhoCorasick

text = "apple banana apple cherry banana"
patterns = ["apple", "banana", "cherry"]
searcher = AhoCorasick(patterns)
searcher.search(text)
# Output: Pattern 'apple' found at index 0
#         Pattern 'banana' found at index 6
#         Pattern 'apple' found at index 13
#         Pattern 'cherry' found at index 20
#         Pattern 'banana' found at index 27
```

### Example 4: Search DNA
```python
from algorithms.multiple_pattern import AhoCorasick

dna = "ATCGATCGATCGATCGATCG"
genes = ["ATG", "TCG", "ATC"]
searcher = AhoCorasick(genes)
searcher.search(dna)
```

### Example 5: Check if Pattern Exists
```python
from algorithms.single_pattern import boyer_moore_search

text = "Python is awesome"
pattern = "awesome"
boyer_moore_search(text, pattern)  # If no output, pattern not found
```

### Example 6: Count Pattern Occurrences
```python
from algorithms.single_pattern import naive_search
import io
from contextlib import redirect_stdout

text = "banana"
pattern = "ana"

# Capture output
f = io.StringIO()
with redirect_stdout(f):
    naive_search(text, pattern)
output = f.getvalue()
count = output.count("Pattern found")
print(f"Pattern found {count} times")
```

### Example 7: Process Multiple Texts
```python
from algorithms.single_pattern import boyer_moore_search

texts = [
    "Hello World",
    "Hello Python",
    "Hello Universe"
]
pattern = "Hello"

for text in texts:
    print(f"Searching in: {text}")
    boyer_moore_search(text, pattern)
```

### Example 8: Read from File and Search
```python
from algorithms.single_pattern import boyer_moore_search

with open('document.txt', 'r') as f:
    text = f.read()

boyer_moore_search(text, "searchterm")
```

---

## 🎮 Which Algorithm to Choose?

```python
# For learning or small texts
from algorithms.single_pattern import naive_search

# For long text + one pattern (FASTEST)
from algorithms.single_pattern import boyer_moore_search

# For repeating patterns
from algorithms.single_pattern import morris_pratt_search

# For hash-based matching
from algorithms.single_pattern import rabin_karp_search

# For many patterns (RECOMMENDED) ⭐
from algorithms.multiple_pattern import AhoCorasick

# For many patterns (alternative)
from algorithms.multiple_pattern import rabin_karp_multiple

# For advanced optimization
from algorithms.multiple_pattern import wu_manber
from algorithms.multiple_pattern import commentz_walter
```

---

## 🧬 Bioinformatics Examples

### Find Restriction Enzyme Sites
```python
from algorithms.multiple_pattern import AhoCorasick

dna = "GAATTCGGATCCAAGCTTGCGGCCGCTAGCTA"
restriction_sites = ["GAATTC", "GGATCC", "AAGCTT", "GCGGCCGC"]
finder = AhoCorasick(restriction_sites)
finder.search(dna)
```

### Find Protein Motifs
```python
from algorithms.multiple_pattern import AhoCorasick

protein = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGR"
motifs = ["VHL", "ALW", "GKV"]
finder = AhoCorasick(motifs)
finder.search(protein)
```

### Find Tandem Repeats
```python
from algorithms.single_pattern import morris_pratt_search

dna = "AABAABAABAACAADAABAABA"
repeat = "AABA"
morris_pratt_search(dna, repeat)
```

---

## 📝 Real-World Applications

### Content Filtering
```python
from algorithms.multiple_pattern import AhoCorasick

forbidden_words = ["spam", "abuse", "harmful"]
filter_obj = AhoCorasick(forbidden_words)

user_input = "This is spam and harmful content"
filter_obj.search(user_input)
# Detects forbidden words
```

### Plagiarism Detection
```python
from algorithms.single_pattern import rabin_karp_search

original = "The quick brown fox jumps over"
suspicious = "The quick brown fox jumps over the lazy dog"

phrases = original.split()
for phrase in phrases:
    if len(phrase) > 3:  # Check phrases longer than 3 chars
        rabin_karp_search(suspicious, phrase)
```

### Log Analysis
```python
from algorithms.multiple_pattern import AhoCorasick

error_codes = ["ERROR", "FATAL", "CRITICAL", "TIMEOUT"]
analyzer = AhoCorasick(error_codes)

with open('app.log', 'r') as f:
    log_content = f.read()

analyzer.search(log_content)
```

### Keyword Extraction
```python
from algorithms.multiple_pattern import AhoCorasick

keywords = ["python", "programming", "algorithm", "data"]
extractor = AhoCorasick(keywords)

text = "Python programming is about algorithms and data structures"
extractor.search(text)
```

---

## ⚙️ Performance Tips

### Tip 1: Use Right Algorithm
```python
# ❌ SLOW: Single pattern search 100 times
for p in patterns:
    naive_search(text, p)

# ✅ FAST: Multi-pattern search once
searcher = AhoCorasick(patterns)
searcher.search(text)
```

### Tip 2: Preprocessing
```python
# ❌ Search case-insensitive each time
boyer_moore_search(text, pattern)

# ✅ Normalize once
text = text.lower()
pattern = pattern.lower()
boyer_moore_search(text, pattern)
```

### Tip 3: Large Files
```python
from algorithms.multiple_pattern import AhoCorasick

patterns = ["pattern1", "pattern2"]
searcher = AhoCorasick(patterns)

# Process in chunks for large files
with open('large_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        searcher.search(line)
```

### Tip 4: Batch Operations
```python
from algorithms.multiple_pattern import AhoCorasick

# Search once for all patterns
searcher = AhoCorasick(all_patterns)
searcher.search(big_text)

# Instead of searching multiple times
```

---

## 🐛 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| **No matches found** | Check encoding, case sensitivity: `text.lower()` |
| **Slow performance** | Use `AhoCorasick` for multiple patterns |
| **Pattern not found** | Use `strip()` to remove whitespace |
| **Memory issues** | Process files in chunks instead of loading all |
| **Overlapping matches** | Expected behavior - some algorithms find overlaps |

---

## 📊 Algorithm Speed Comparison

```
Text Size: 100KB | Pattern Size: 50 chars

Naive Search        ████████████████████ (slowest)
Morris-Pratt        ████████████ 
Rabin-Karp          ██████████
Boyer-Moore         ███ (fastest for single pattern)
AhoCorasick         ███ (fastest for multiple patterns) ⭐
```

**For multiple patterns, AhoCorasick is almost always best!**

---

## 🔧 Integration Examples

### With Regular Expressions
```python
import re
from algorithms.single_pattern import boyer_moore_search

text = "email@example.com another@test.com"
# Find email pattern positions using Boyer-Moore
boyer_moore_search(text, "@example")
```

### With Pandas DataFrames
```python
import pandas as pd
from algorithms.single_pattern import boyer_moore_search

df = pd.read_csv('data.csv')
for index, row in df.iterrows():
    boyer_moore_search(str(row['text']), 'keyword')
```

### With Database Queries
```python
from algorithms.multiple_pattern import AhoCorasick
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

keywords = ["urgent", "important", "critical"]
searcher = AhoCorasick(keywords)

for row in cursor.execute("SELECT content FROM messages"):
    searcher.search(row[0])
```

---

## 📚 More Examples

Find more examples in the `/examples` folder of the repository!

```bash
# Run example
python algorithms/single_pattern/naive.py
python algorithms/multiple_pattern/aho_corasick.py
```

---

## ❓ Need Help?

- **Check the full guide:** `USAGE_GUIDE.md`
- **Read the code:** Each algorithm has comments
- **Run examples:** `python algorithms/*/` 
- **Open an issue:** github.com/HADIL19/Pattern-Searching/issues

---

**Happy Searching! 🎯**
