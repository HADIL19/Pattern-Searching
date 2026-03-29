# Integration Guide: Using Pattern-Searching in Your Projects

Complete guide for integrating the Pattern-Searching package into your own applications.

---

## 🚀 Integration Methods

### Method 1: Local Installation (Recommended)

Best for: Projects that use pattern searching regularly

```bash
# Clone the repository
git clone https://github.com/HADIL19/Pattern-Searching.git

# Install in development mode
cd Pattern-Searching
pip install -e .

# Now use in any project
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick
```

### Method 2: Direct Import

Best for: Quick prototypes or single-file scripts

```bash
# Copy the algorithms folder to your project
your_project/
├── your_script.py
└── algorithms/
    ├── single_pattern/
    └── multiple_pattern/
```

```python
# In your_script.py
from algorithms.single_pattern import boyer_moore_search

# Use directly
boyer_moore_search(text, pattern)
```

### Method 3: Add to requirements.txt

Best for: Team projects with dependencies

```bash
# Add to your requirements.txt (after pip install available)
-e git+https://github.com/HADIL19/Pattern-Searching.git#egg=pattern-searching
```

```bash
pip install -r requirements.txt
```

### Method 4: Import Specific Functions

Best for: Minimal dependencies

```python
# Import only what you need
from algorithms.single_pattern.boyer_moore import boyer_moore_search
from algorithms.multiple_pattern.aho_corasick import AhoCorasick

# Reduces memory footprint
```

---

## 📁 Project Structure Examples

### Example 1: Web Application

```
web_app/
├── requirements.txt
├── app.py
├── main.py
├── search_service.py
└── algorithms/  (copy from Pattern-Searching)
    ├── single_pattern/
    └── multiple_pattern/

# search_service.py
from algorithms.multiple_pattern import AhoCorasick

class SearchService:
    def __init__(self, patterns):
        self.searcher = AhoCorasick(patterns)
    
    def find_keywords(self, text):
        return self.searcher.search(text)
```

### Example 2: Data Analysis Project

```
data_analysis/
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── processor.py
│   └── algorithms/  (copy from Pattern-Searching)
└── data/
    ├── raw/
    └── processed/

# processor.py
from algorithms.single_pattern import boyer_moore_search

def process_text_data(df):
    results = []
    for text in df['content']:
        boyer_moore_search(text, 'keyword')
        results.append(text)
    return results
```

### Example 3: Bioinformatics Pipeline

```
bioinformatics/
├── requirements.txt
├── genome_analyzer.py
├── dna_processor.py
└── algorithms/  (copy from Pattern-Searching)
    ├── single_pattern/
    └── multiple_pattern/

# genome_analyzer.py
from algorithms.multiple_pattern import AhoCorasick

def find_genes(dna_sequence, gene_patterns):
    analyzer = AhoCorasick(gene_patterns)
    analyzer.search(dna_sequence)
```

---

## 🔧 Using in Different Contexts

### Flask/Django Web Application

```python
# app.py - Flask example
from flask import Flask, request, jsonify
from algorithms.multiple_pattern import AhoCorasick

app = Flask(__name__)

# Initialize searcher once
keyword_searcher = AhoCorasick(['keyword1', 'keyword2', 'keyword3'])

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    text = data.get('text', '')
    
    results = []
    import io
    from contextlib import redirect_stdout
    
    # Capture search results
    f = io.StringIO()
    with redirect_stdout(f):
        keyword_searcher.search(text)
    
    response = {
        'text': text,
        'matches': f.getvalue().split('\n')
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
```

### Jupyter Notebook

```python
# In a Jupyter notebook cell
%cd /path/to/Pattern-Searching
import sys
sys.path.append('.')

from algorithms.multiple_pattern import AhoCorasick

# Load data
import pandas as pd
df = pd.read_csv('your_data.csv')

# Search patterns
patterns = ['pattern1', 'pattern2']
searcher = AhoCorasick(patterns)

# Apply to dataframe
df['text'].apply(lambda x: searcher.search(x))
```

### Command Line Script

```python
# cli_search.py
#!/usr/bin/env python3

import argparse
import sys
from algorithms.single_pattern import boyer_moore_search

def main():
    parser = argparse.ArgumentParser(description='Search for pattern in text')
    parser.add_argument('text', help='Text to search in')
    parser.add_argument('pattern', help='Pattern to search for')
    parser.add_argument('--algorithm', choices=['naive', 'boyer_moore', 'kmp', 'rk'],
                       default='boyer_moore', help='Algorithm to use')
    
    args = parser.parse_args()
    
    boyer_moore_search(args.text, args.pattern)

if __name__ == '__main__':
    main()

# Usage: python cli_search.py "Hello World" "World"
```

### Background Task/Celery

```python
# tasks.py - Celery example
from celery import Celery
from algorithms.multiple_pattern import AhoCorasick

app = Celery('tasks')

@app.task
def analyze_document(doc_id, patterns):
    """Analyze document in background"""
    # Load document from database
    document = load_document(doc_id)
    
    # Search patterns
    searcher = AhoCorasick(patterns)
    searcher.search(document.text)
    
    # Store results
    save_analysis_results(doc_id)
    
    return {'status': 'completed', 'doc_id': doc_id}
```

### API Endpoint

```python
# api.py - FastAPI example
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from algorithms.single_pattern import boyer_moore_search

app = FastAPI()

class SearchRequest(BaseModel):
    text: str
    pattern: str

@app.post("/api/search")
def search_pattern(request: SearchRequest):
    try:
        results = boyer_moore_search(request.text, request.pattern)
        return {
            "status": "success",
            "text": request.text,
            "pattern": request.pattern
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## 🛠️ Creating Wrapper Classes

### Reusable Searcher Class

```python
# searcher.py
from algorithms.multiple_pattern import AhoCorasick
from algorithms.single_pattern import boyer_moore_search
import io
from contextlib import redirect_stdout

class PatternSearcher:
    def __init__(self, patterns=None, algorithm='aho_corasick'):
        self.patterns = patterns or []
        self.algorithm = algorithm
        self.results = []
        
        if algorithm == 'aho_corasick' and patterns:
            self.searcher = AhoCorasick(patterns)
    
    def search(self, text):
        """Search and return results"""
        self.results = []
        
        f = io.StringIO()
        with redirect_stdout(f):
            if self.algorithm == 'aho_corasick':
                self.searcher.search(text)
            elif self.algorithm == 'boyer_moore':
                for pattern in self.patterns:
                    boyer_moore_search(text, pattern)
        
        output = f.getvalue()
        self.results = output.strip().split('\n')
        return self.results
    
    def count_matches(self):
        """Count total matches"""
        return len([r for r in self.results if 'found' in r])

# Usage
searcher = PatternSearcher(['python', 'java', 'c++'], 'aho_corasick')
results = searcher.search("Python and Java are great")
print(f"Found {searcher.count_matches()} matches")
```

### Context-Specific Searcher

```python
# dna_searcher.py
from algorithms.multiple_pattern import AhoCorasick

class DNASequenceAnalyzer:
    """Specialized for DNA analysis"""
    
    RESTRICTION_ENZYMES = {
        'EcoRI': 'GAATTC',
        'BamHI': 'GGATCC',
        'HindIII': 'AAGCTT'
    }
    
    def __init__(self):
        self.searcher = AhoCorasick(list(self.RESTRICTION_ENZYMES.values()))
    
    def find_restriction_sites(self, dna_sequence):
        """Find all restriction enzyme sites"""
        self.searcher.search(dna_sequence)
    
    def find_open_reading_frames(self, dna_sequence):
        """Find ORFs"""
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]
        self.searcher.search(dna_sequence)

# Usage
analyzer = DNASequenceAnalyzer()
analyzer.find_restriction_sites("AGCTAGAATTCTAGCTAGATCCTA")
```

---

## 🐍 Python Version Compatibility

### Python 3.8+

```python
# Should work fine
from algorithms.single_pattern import naive_search
naive_search(text, pattern)
```

### With Type Hints

```python
from typing import List, Tuple
from algorithms.multiple_pattern import AhoCorasick

def search_multiple(text: str, patterns: List[str]) -> List[Tuple[str, int]]:
    """Type-safe wrapper"""
    searcher = AhoCorasick(patterns)
    searcher.search(text)
    return []  # Return structured results

# Usage
results = search_multiple("test text", ["test"])
```

---

## 📦 Adding to Your Package

### If you're building a library using Pattern-Searching

```python
# your_package/search.py
from algorithms.multiple_pattern import AhoCorasick as _AhoCorasick

class AhoCorasick(_AhoCorasick):
    """Wrapper with additional features"""
    
    def __init__(self, patterns):
        super().__init__(patterns)
        self.match_count = 0
    
    def search(self, text):
        """Enhanced search with counting"""
        self.match_count = 0
        # Call parent search
        super().search(text)

# your_package/__init__.py
from .search import AhoCorasick

__all__ = ['AhoCorasick']
```

---

## ✅ Testing Integration

### Unit Tests

```python
# tests/test_integration.py
import unittest
from algorithms.single_pattern import boyer_moore_search
from algorithms.multiple_pattern import AhoCorasick

class TestIntegration(unittest.TestCase):
    def test_boyer_moore(self):
        text = "HELLO WORLD"
        pattern = "WORLD"
        # Add assertions to capture results
        boyer_moore_search(text, pattern)
    
    def test_aho_corasick(self):
        text = "test text test"
        patterns = ["test", "text"]
        searcher = AhoCorasick(patterns)
        searcher.search(text)

if __name__ == '__main__':
    unittest.main()
```

### Integration Testing

```python
# tests/test_full_workflow.py
def test_full_workflow():
    """Test complete workflow"""
    from algorithms.multiple_pattern import AhoCorasick
    
    # Simulate real usage
    text = open('sample.txt').read()
    patterns = ['keyword1', 'keyword2']
    
    searcher = AhoCorasick(patterns)
    searcher.search(text)
    
    # Verify it completes without error
    assert True
```

---

## 🚀 Performance Optimization Tips

### Reuse Searcher Objects

```python
# ❌ SLOW: Create new searcher each time
for text in documents:
    searcher = AhoCorasick(patterns)
    searcher.search(text)

# ✅ FAST: Create once, reuse
searcher = AhoCorasick(patterns)
for text in documents:
    searcher.search(text)
```

### Batch Processing

```python
# ❌ SLOW: Process one by one
for document in documents:
    searcher.search(document.text)

# ✅ FAST: Batch if possible
large_text = '\n'.join([d.text for d in documents])
searcher.search(large_text)
```

### Memory Management

```python
# For very large files
def search_large_file(filename, patterns, chunk_size=8192):
    searcher = AhoCorasick(patterns)
    
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size).decode('utf-8', errors='ignore')
            if not chunk:
                break
            searcher.search(chunk)
```

---

## 🐛 Debugging Integration Issues

### Capture Output for Debugging

```python
import io
from contextlib import redirect_stdout

# Capture printed output
f = io.StringIO()
with redirect_stdout(f):
    searcher.search(text)
output = f.getvalue()

# Parse and debug
lines = output.strip().split('\n')
print(f"Found {len(lines)} matches")
```

### Logging Integration

```python
import logging
from algorithms.multiple_pattern import AhoCorasick

logger = logging.getLogger(__name__)

def search_with_logging(text, patterns):
    try:
        searcher = AhoCorasick(patterns)
        logger.info(f"Starting search with {len(patterns)} patterns")
        searcher.search(text)
        logger.info("Search completed successfully")
    except Exception as e:
        logger.error(f"Search error: {e}")
```

---

## 📚 Common Integration Patterns

### Pattern 1: Configuration-Based Searching

```python
# config.py
SEARCH_CONFIG = {
    'patterns': ['word1', 'word2', 'word3'],
    'algorithm': 'aho_corasick'
}

# search.py
from config import SEARCH_CONFIG
from algorithms.multiple_pattern import AhoCorasick

searcher = AhoCorasick(SEARCH_CONFIG['patterns'])
searcher.search(text)
```

### Pattern 2: Factory Pattern

```python
class SearcherFactory:
    @staticmethod
    def create(algorithm_type, patterns):
        if algorithm_type == 'single':
            from algorithms.single_pattern import boyer_moore_search
            return boyer_moore_search
        elif algorithm_type == 'multiple':
            from algorithms.multiple_pattern import AhoCorasick
            return AhoCorasick(patterns)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm_type}")

# Usage
searcher = SearcherFactory.create('multiple', patterns)
```

### Pattern 3: Caching Results

```python
from functools import lru_cache
from algorithms.single_pattern import boyer_moore_search

@lru_cache(maxsize=128)
def cached_search(text, pattern):
    # Cache search results
    boyer_moore_search(text, pattern)
    return True
```

---

## 🔗 Integration Checklist

- [ ] Installation method chosen (local/direct/requirements)
- [ ] Import statements added to project
- [ ] Project structure updated if needed
- [ ] Dependencies documented
- [ ] Tests written for integration
- [ ] Performance verified for your use case
- [ ] Error handling implemented
- [ ] Documentation updated
- [ ] Code review completed
- [ ] Deployment tested

---

## ❓ Troubleshooting Integration

| Problem | Solution |
|---------|----------|
| **Import error** | Ensure path is correct: `sys.path.append()` |
| **No results** | Check encoding, use `.lower()` for case-insensitive |
| **Memory issues** | Process large files in chunks |
| **Slow performance** | Use AhoCorasick for multiple patterns |
| **Character encoding** | Decode with proper encoding |

---

## 📞 Getting Help

- **Issues:** https://github.com/HADIL19/Pattern-Searching/issues
- **Discussions:** Check GitHub discussions
- **Documentation:** See USAGE_GUIDE.md

Happy integrating! 🚀
