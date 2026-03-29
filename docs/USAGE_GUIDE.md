# Pattern-Searching Package: Complete Usage Guide

A comprehensive guide to using the Pattern-Searching algorithms in your projects.

---

## 📦 Installation

### Option 1: Local Installation (Development)
```bash
git clone https://github.com/HADIL19/Pattern-Searching.git
cd Pattern-Searching
pip install -e .
```

### Option 2: Direct Import
Simply copy the `algorithms/` folder to your project and import directly:
```python
import sys
sys.path.append('path/to/Pattern-Searching')
```

---

## 🎯 Quick Start

### Single Pattern Search
```python
from algorithms.single_pattern import naive_search

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
naive_search(text, pattern)
# Output: Pattern found at index 10
```

### Multiple Pattern Search
```python
from algorithms.multiple_pattern import AhoCorasick

text = "ACGTACGTGACG"
patterns = ["ACG", "GAC"]
ac = AhoCorasick(patterns)
ac.search(text)
# Output:
# Pattern 'ACG' found at index 0
# Pattern 'GAC' found at index 5
# Pattern 'ACG' found at index 9
```

---

## 📖 Single-Pattern Algorithms

### 1. Naive Search (Brute Force)

**Best for:** Small texts, learning, quick prototypes  
**Time Complexity:** O((n-m+1) × m) = O(n×m)  
**Space Complexity:** O(1)

```python
from algorithms.single_pattern import naive_search

# Example 1: Simple text
text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
naive_search(text, pattern)
# Output: Pattern found at index 16

# Example 2: DNA sequence
dna_text = "ATCGATCGATCGTAGC"
dna_pattern = "ATG"
naive_search(dna_text, dna_pattern)
# Output: Pattern found at index 0, Pattern found at index 4, Pattern found at index 8

# Example 3: Finding repeated words
text = "the the the quick the fox"
pattern = "the"
naive_search(text, pattern)
```

**When to Use:**
- Educational purposes
- Small texts (< 1000 characters)
- Pattern length is similar to text length
- You need simplicity over speed

---

### 2. Morris-Pratt (KMP - Knuth-Morris-Pratt)

**Best for:** Texts with repeating patterns  
**Time Complexity:** O(n + m)  
**Space Complexity:** O(m)

```python
from algorithms.single_pattern import morris_pratt_search

# Example 1: Repeating patterns
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
morris_pratt_search(text, pattern)
# Output: Pattern found at index 10

# Example 2: DNA with repeating motifs
dna_text = "AABAABAABAACAADAABAABA"
dna_pattern = "AABA"
morris_pratt_search(dna_text, dna_pattern)
# Output: Found at multiple positions

# Example 3: Finding repeating strings
text = "ababababab"
pattern = "abab"
morris_pratt_search(text, pattern)
```

**When to Use:**
- Texts with repeating patterns
- Need linear time guarantee
- Memory is not a constraint
- Patterns have internal repeating structure

**Real-World Use Case: Finding Palindrome Repeats in DNA**
```python
# Find tandem repeats in DNA sequence
dna = "GATCGATCGATCGAT"
motif = "GATC"
morris_pratt_search(dna, motif)  # Efficient for repeating motifs
```

---

### 3. Boyer-Moore

**Best for:** Long texts, large alphabets, real-world text processing  
**Time Complexity:** O(n/m) best case, O(n×m) worst case  
**Space Complexity:** O(alphabet_size)

```python
from algorithms.single_pattern import boyer_moore_search

# Example 1: English text (most efficient)
text = "The Boyer-Moore algorithm is faster than naive search"
pattern = "algorithm"
boyer_moore_search(text, pattern)
# Output: Pattern found at index 4

# Example 2: Long genomic sequence
dna_text = "GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
dna_pattern = "AGCT"
boyer_moore_search(dna_text, dna_pattern)

# Example 3: File search
with open('document.txt', 'r') as f:
    text = f.read()
pattern = "searchterm"
boyer_moore_search(text, pattern)
```

**When to Use:**
- Large texts (> 10,000 characters)
- Long patterns (pattern length >> 1)
- Real-world text processing
- Searching in files or logs
- DNA/protein sequences with diverse characters

**Performance Tips:**
```python
# Boyer-Moore is fastest with longer patterns in diverse alphabets
long_text = "A" * 100000 + "NEEDLE" + "B" * 100000
needle = "NEEDLE"
boyer_moore_search(long_text, needle)  # Very fast - skips most chars
```

---

### 4. Rabin-Karp (Rolling Hash)

**Best for:** Multiple pattern matching, bulk searches  
**Time Complexity:** O(n + m) average, O((n-m+1)×m) worst  
**Space Complexity:** O(1)

```python
from algorithms.single_pattern import rabin_karp_search

# Example 1: Simple pattern search
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"Searching for pattern '{pattern}' in text '{text}'...")
rabin_karp_search(text, pattern)
# Output: Pattern found at index 10

# Example 2: Plagiarism detection (find duplicate text blocks)
document = "The quick brown fox jumps over the lazy dog. The quick brown fox is fast."
suspicious_phrase = "The quick brown fox"
rabin_karp_search(document, suspicious_phrase)

# Example 3: Finding repeated sequences in DNA
dna = "ATCGATCGATCGATCG"
sequence = "ATCG"
rabin_karp_search(dna, sequence)

# Example 4: Case-insensitive search (preprocess text and pattern)
text = "Hello HELLO hello"
pattern = "hello"
rabin_karp_search(text.lower(), pattern.lower())
```

**When to Use:**
- Need to prepare for multiple patterns
- Hash-based optimization is needed
- Works well with both text and binary data
- Plagiarism detection
- Duplicate block detection

---

## 📖 Multiple-Pattern Algorithms

### 1. Rabin-Karp (Multiple Patterns)

**Best for:** Searching many patterns simultaneously  
**Time Complexity:** O(n×k + z) where k = number of patterns  
**Space Complexity:** O(k)

```python
from algorithms.multiple_pattern import rabin_karp_multiple

# Example 1: Find multiple DNA motifs
text = "ACGTACGTGACGATCGATCGATCG"
patterns = ["ACG", "GAC", "ATC"]
rabin_karp_multiple(text, patterns)
# Output:
# Pattern 'ACG' found at index 0
# Pattern 'GAC' found at index 5
# Pattern 'ACG' found at index 7
# ... etc

# Example 2: Keyword search in document
text = "Python is great. Java is powerful. C++ is fast. Python is fun."
keywords = ["Python", "Java", "C++"]
rabin_karp_multiple(text, keywords)

# Example 3: Search for multiple domain names in logs
log_text = "user visited google.com then facebook.com then google.com"
domains = ["google.com", "facebook.com", "twitter.com"]
rabin_karp_multiple(log_text, domains)

# Example 4: Find restriction enzyme sites in DNA
dna = "GAATTCGAATTCAAGCTTAAGCTT"
enzymes = ["GAATTC", "AAGCTT"]  # EcoRI and HindIII restriction sites
rabin_karp_multiple(dna, enzymes)
```

**When to Use:**
- Searching 5-100 patterns
- Patterns are reasonably short
- Need simple implementation
- Hash-based approach preferred

---

### 2. Aho-Corasick (Multiple Patterns - Most Efficient)

**Best for:** Many patterns, large texts, real-world applications  
**Time Complexity:** O(n + m + z) where z = number of matches  
**Space Complexity:** O(m × alphabet_size)

```python
from algorithms.multiple_pattern import AhoCorasick

# Example 1: Basic usage
text = "ACGTACGTGACG"
patterns = ["ACG", "GAC"]
ac = AhoCorasick(patterns)
ac.search(text)
# Output:
# Pattern 'ACG' found at index 0
# Pattern 'GAC' found at index 5
# Pattern 'ACG' found at index 9

# Example 2: Find all protein motifs in a sequence
protein_sequence = "MVHLTPEEKS"
protein_patterns = ["VHL", "HLT", "PE", "EKS"]
ac = AhoCorasick(protein_patterns)
ac.search(protein_sequence)

# Example 3: Malware/virus signature detection
file_content = "MZExecute.....MZEmbedded.....MZTerminate"
virus_signatures = ["MZExecute", "MZEmbedded", "MZTerminate", "BadSignature"]
ac = AhoCorasick(virus_signatures)
ac.search(file_content)

# Example 4: Find multiple keywords in book/article
text = "Alice went to Wonderland. Alice met the Cheshire Cat."
keywords = ["Alice", "Wonderland", "Cheshire", "Cat"]
ac = AhoCorasick(keywords)
ac.search(text)

# Example 5: DNA motif discovery
gene_sequence = "AGCTAGCTATAGACTAGACTAGCTA"
binding_sites = ["TAG", "ATA", "GAC"]
ac = AhoCorasick(binding_sites)
ac.search(gene_sequence)

# Example 6: Search with returning results instead of printing
# (You can modify the class to return results instead of printing)
text = "banana"
patterns = ["ana", "nan", "banana"]
ac = AhoCorasick(patterns)
ac.search(text)
# Output:
# Pattern 'ana' found at index 1
# Pattern 'ana' found at index 3
# Pattern 'banana' found at index 0
```

**When to Use:**
- **Recommended for most cases!**
- Searching many patterns (10+)
- Large texts (> 100KB)
- Need optimal performance
- All patterns needed to be found in single pass
- Real-world applications

**Advanced Example: Creating a Gene Finder**
```python
# Find all known genes in a DNA sequence
known_genes = [
    "AATAAA",  # Polyadenylation signal
    "TATAAA",  # TATA box
    "CAAT",    # CAAT box
    "GC"       # GC content marker
]

dna_sequence = "GCTAGCTAGCTAGCTATAAA...GCTAGCTAGCTAATAAA..."
gene_finder = AhoCorasick(known_genes)
gene_finder.search(dna_sequence)
```

---

### 3. Wu-Manber

**Best for:** Very large pattern sets, block-based optimization  
**Time Complexity:** O(n/block_size + z)  
**Space Complexity:** O(pattern_count × pattern_length)

```python
from algorithms.multiple_pattern import wu_manber

# Example 1: Dictionary word lookup
text = "ACGTACGTGACGATCGATCG"
words = ["ACG", "GAC", "ATC"]
wu_manber(text, words)

# Example 2: Search multiple error-correcting codes
data = "ACGTACGTGACGATCGATCG"
error_codes = ["ACG", "GAC", "ATC"]
wu_manber(data, error_codes)

# Example 3: Content filtering
content = "badwordgoodwordneutralword"
filter_words = ["badword", "forbidden", "blocked"]
wu_manber(content, filter_words)
```

**When to Use:**
- Searching very many patterns (100+)
- Patterns are similar in length
- Block-based processing beneficial
- Memory-efficient needed

---

### 4. Commentz-Walter

**Best for:** Multiple patterns with Boyer-Moore optimization  
**Time Complexity:** O(n/m) average case  
**Space Complexity:** O(pattern_count × alphabet_size)

```python
from algorithms.multiple_pattern import commentz_walter

# Example 1: Optimized multi-pattern search
text = "ACGTACGTGACGATCGATCG"
patterns = ["ACG", "GAC", "ATC"]
commentz_walter(text, patterns)

# Example 2: Fast scanning with Boyer-Moore logic
dna = "GCTAGCTAGCTAGCTAGCTA"
motifs = ["TAG", "GCT", "CTA"]
commentz_walter(dna, motifs)

# Example 3: URL pattern detection
url_text = "https://google.com and https://facebook.com"
url_patterns = [".com", ".org", ".edu"]
commentz_walter(url_text, url_patterns)
```

**When to Use:**
- Need Boyer-Moore speed with multiple patterns
- Pattern set is moderate (10-50)
- Patterns are longer
- Fast scanning is important

---

## 🔬 Real-World Examples

### Bioinformatics: Finding Restriction Sites in DNA

```python
from algorithms.multiple_pattern import AhoCorasick

# Restriction enzyme recognition sites
restriction_sites = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC"
}

dna_sequence = """
AGCTAGCTAGCTAGAATTCTAGCTAGCTAGGATCCTAGCTAGAAGCTTGCGGCCGC
TAGCTAGCTAGCTAGCTAGAATTCTAGCT
"""

patterns = list(restriction_sites.values())
enzyme_finder = AhoCorasick(patterns)
print("Found restriction sites:")
enzyme_finder.search(dna_sequence)
```

### Text Processing: Content Filtering

```python
from algorithms.multiple_pattern import AhoCorasick

# Inappropriate words filter
inappropriate_words = ["badword1", "badword2", "badword3", "offensive"]
filter_object = AhoCorasick(inappropriate_words)

user_comment = "This is a badword1 comment with offensive content"
print("Scanning comment for inappropriate content...")
filter_object.search(user_comment)
```

### Log Analysis: Finding Error Codes

```python
from algorithms.multiple_pattern import AhoCorasick

error_codes = ["ERROR_404", "ERROR_500", "ERROR_503", "TIMEOUT", "DENIED"]
error_scanner = AhoCorasick(error_codes)

log_file = """
2024-01-15 10:23:45 User login SUCCESS
2024-01-15 10:24:01 Request to /api/data ERROR_404
2024-01-15 10:24:15 Server response ERROR_500
2024-01-15 10:25:00 Database TIMEOUT
"""

print("Errors found in log:")
error_scanner.search(log_file)
```

### Plagiarism Detection

```python
from algorithms.single_pattern import rabin_karp_search

original_text = "The quick brown fox jumps over the lazy dog"
suspicious_text = "A quick brown fox jumps very quickly"

# Extract phrases of length 5+
import re
phrases = re.findall(r'\b\w{5,}\b', original_text)

print("Checking for phrase matches:")
for phrase in phrases:
    rabin_karp_search(suspicious_text, phrase)
```

---

## 📊 Algorithm Comparison & Selection Guide

| Use Case | Recommended | Reason |
|----------|-------------|--------|
| **Single small pattern** | Naive | Simple, fast for small inputs |
| **Single pattern, repeating** | Morris-Pratt | O(n+m) guaranteed, efficient |
| **Single pattern, long text** | Boyer-Moore | Skips characters, very fast |
| **Many patterns, one pass** | Aho-Corasick | ⭐ Best choice for most real-world |
| **100+ patterns** | Wu-Manber | Block optimization advantage |
| **Multiple similar patterns** | Commentz-Walter | Boyer-Moore + multiple patterns |
| **Quick prototype** | Rabin-Karp | Simple, reliable for testing |

---

## 🚀 Performance Tips

### Tip 1: Choose the Right Algorithm
```python
# ❌ DON'T do this
for pattern in 100_patterns:
    naive_search(text, pattern)  # Slow!

# ✅ DO this
from algorithms.multiple_pattern import AhoCorasick
ac = AhoCorasick(100_patterns)
ac.search(text)  # Fast!
```

### Tip 2: Preprocess Text When Possible
```python
# ❌ Case-sensitive search each time
from algorithms.single_pattern import boyer_moore_search
boyer_moore_search(text, pattern)

# ✅ Normalize once
text_lower = text.lower()
pattern_lower = pattern.lower()
boyer_moore_search(text_lower, pattern_lower)
```

### Tip 3: Use String Objects Efficiently
```python
# ❌ Create new strings repeatedly
text = read_large_file()
for chunk in text.split():
    boyer_moore_search(chunk, pattern)

# ✅ Work with memory views when possible
import io
with io.StringIO(text) as f:
    for line in f:
        boyer_moore_search(line, pattern)
```

### Tip 4: Match Pattern to Data Size
```python
import time
from algorithms.single_pattern import naive_search, boyer_moore_search

text = "A" * 10000 + "NEEDLE" + "B" * 10000
pattern = "NEEDLE"

# Small pattern vs large text = Boyer-Moore wins
start = time.time()
boyer_moore_search(text, pattern)
print(f"Boyer-Moore: {time.time() - start:.6f}s")

start = time.time()
naive_search(text, pattern)
print(f"Naive: {time.time() - start:.6f}s")
```

---

## 📝 Common Patterns & Solutions

### Pattern 1: Find All Occurrences and Get Positions

```python
# Current implementation prints results
# To capture positions, modify like this:

def aho_corasick_with_results(text, patterns):
    from algorithms.multiple_pattern import AhoCorasick
    ac = AhoCorasick(patterns)
    results = []
    
    node = ac.root
    for i, char in enumerate(text):
        while node and char not in node.children:
            node = node.fail
        node = node.children[char] if node and char in node.children else ac.root
        for pattern in node.output:
            results.append({
                'pattern': pattern,
                'position': i - len(pattern) + 1
            })
    return results

text = "ACGTACGTGACG"
patterns = ["ACG", "GAC"]
matches = aho_corasick_with_results(text, patterns)
print(matches)
```

### Pattern 2: Case-Insensitive Search

```python
from algorithms.single_pattern import boyer_moore_search

text = "The Quick Brown Fox"
pattern = "quick"

# Convert both to same case
boyer_moore_search(text.lower(), pattern.lower())
# Or uppercase
boyer_moore_search(text.upper(), pattern.upper())
```

### Pattern 3: Search in File

```python
from algorithms.single_pattern import boyer_moore_search

def search_in_file(filename, pattern):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    boyer_moore_search(text, pattern)

search_in_file('document.txt', 'searchterm')
```

### Pattern 4: Find Overlapping Matches

```python
from algorithms.multiple_pattern import AhoCorasick

text = "banana"
patterns = ["ana"]
ac = AhoCorasick(patterns)
ac.search(text)
# Output shows both overlapping occurrences at index 1 and 3
```

---

## 🛠️ Troubleshooting

### Issue: No matches found
**Solution:** Check encoding, case sensitivity, and exact string matching
```python
# Ensure text and pattern are same type
text = text.strip()  # Remove whitespace
pattern = pattern.strip()
boyer_moore_search(text, pattern)
```

### Issue: Getting duplicate results
**Solution:** Some algorithms may find overlapping patterns
```python
# Use set to deduplicate if needed
results = set()
# ... run search and collect results ...
```

### Issue: Memory usage too high
**Solution:** Process file in chunks
```python
def search_large_file(filename, patterns, chunk_size=10000):
    from algorithms.multiple_pattern import AhoCorasick
    ac = AhoCorasick(patterns)
    
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            ac.search(chunk)
```

---

## 📚 References & Further Learning

- [GeeksforGeeks Pattern Searching](https://www.geeksforgeeks.org/dsa/pattern-searching/)
- [Boyer-Moore Algorithm Visualization](https://www-igm.univ-mlv.fr/~lecroq/string/node14.html)
- [Aho-Corasick Algorithm Explained](https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-matching/)
- [Bioinformatics and DNA Sequence Analysis](https://en.wikipedia.org/wiki/Sequence_analysis)

---

## 💡 Contributing

Found a bug or improvement? Open an issue or PR at:
https://github.com/HADIL19/Pattern-Searching

Happy searching! 🎯
