# Pattern Searching Algorithms

This package provides **single-pattern and multiple-pattern string searching algorithms** in Python.  
It is useful for students, programmers, and bioinformatics enthusiasts to **learn, practice, and experiment with text and DNA/protein sequence analysis**.

---

## 🎯 Relevance to Bioinformatics

Pattern searching is crucial for:

- Finding **motifs in DNA sequences** (e.g., promoters, binding sites)  
- Identifying **repeated sequences** or mutations in genomes  
- Searching multiple motifs efficiently in large genomic datasets  

These algorithms are foundational for **sequence analysis, text processing, and bioinformatics data mining**.

---

## 🧩 Single-Pattern Algorithms (Recherche d’un seul motif)

| Algorithm     | Description                                               |
|---------------|-----------------------------------------------------------|
| Naive         | Simple brute-force search for a single pattern.          |
| Morris-Pratt  | Optimized for repeated patterns using prefix preprocessing. |
| Boyer-Moore   | Skips unmatched characters using bad character heuristic. |
| Rabin-Karp    | Uses hashing for pattern search.                          |

**Example:**

```python
from algorithms.single_pattern.naive import naive_search

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
naive_search(text, pattern)
```
## 🧩 Multiple-Pattern Algorithms (Recherche de plusieurs motifs)

| Algorithm           | Description                                               |
|--------------------|-----------------------------------------------------------|
| Rabin-Karp (Multiple) | Hash-based search for multiple patterns at once.       |
| Aho-Corasick        | Builds a finite automaton for all patterns; very efficient. |
| Wu-Manber           | Optimized multiple-pattern search using block shifts.   |
| Commentz-Walter     | Combines Boyer-Moore logic with multiple-pattern optimization. |

**Example:**

```python
from algorithms.multiple_pattern.aho_corasick import AhoCorasick

text = "ACGTACGTGACG"
patterns = ["ACG", "GAC"]
ac = AhoCorasick(patterns)
ac.search(text)
```
---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/HADIL19/Pattern-Searching.git
cd Pattern-Searching
```
Install the package locally:
```bash
pip install -e .
```
Run any algorithm:
```bash
python algorithms/single_pattern/naive.py
python algorithms/multiple_pattern/aho_corasick.py
```
## 📚 Resources

Check `resources/pattern_searching_links.md` for tutorials and detailed explanations:

- [Pattern Searching on GeeksforGeeks](https://www.geeksforgeeks.org/dsa/pattern-searching/)  
- KMP, Rabin-Karp, Boyer-Moore, Aho-Corasick tutorials  
- Wu-Manber and Commentz-Walter references  

---

## ⚖️ License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

You are free to **use, copy, modify, merge, publish, distribute, subl