"""
Practical Examples: Pattern-Searching Package
Real-world use cases with runnable code
"""

# ============================================================================
# EXAMPLE 1: Basic Text Search
# ============================================================================

def example_1_basic_text_search():
    """Find a word in a sentence using different algorithms"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Text Search")
    print("="*70)
    
    from algorithms.single_pattern import naive_search, boyer_moore_search
    
    text = "The quick brown fox jumps over the lazy dog"
    pattern = "fox"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}\n")
    
    print("Using Naive Search:")
    naive_search(text, pattern)
    
    print("\nUsing Boyer-Moore Search:")
    boyer_moore_search(text, pattern)


# ============================================================================
# EXAMPLE 2: Find Multiple Patterns in Text
# ============================================================================

def example_2_multiple_patterns():
    """Find multiple keywords in a document"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Multiple Pattern Search")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    document = """
    Python is a great programming language.
    Java is powerful. C++ is fast.
    Python is also used for data science.
    """
    
    keywords = ["Python", "Java", "C++", "programming"]
    
    print(f"Document:\n{document}")
    print(f"Keywords: {keywords}\n")
    print("Results:")
    
    searcher = AhoCorasick(keywords)
    searcher.search(document)


# ============================================================================
# EXAMPLE 3: DNA Sequence Analysis
# ============================================================================

def example_3_dna_sequence():
    """Find genes and motifs in DNA sequences"""
    print("\n" + "="*70)
    print("EXAMPLE 3: DNA Sequence Analysis")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # A simple DNA sequence
    dna = "AGCTAGCTAGCTAGAATTCTAGCTAGGATCCTAGAAGCTT"
    
    # Restriction enzyme recognition sites
    restriction_sites = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC", 
        "HindIII": "AAGCTT"
    }
    
    print(f"DNA Sequence: {dna}\n")
    print("Restriction Enzyme Sites to Find:")
    for enzyme, site in restriction_sites.items():
        print(f"  {enzyme}: {site}")
    
    print("\nResults:")
    patterns = list(restriction_sites.values())
    searcher = AhoCorasick(patterns)
    searcher.search(dna)


# ============================================================================
# EXAMPLE 4: Content Filtering
# ============================================================================

def example_4_content_filtering():
    """Filter inappropriate content from user input"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Content Filtering")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # Forbidden words (simplified example)
    forbidden_words = ["spam", "abuse", "inappropriate"]
    
    comments = [
        "This is a great product!",
        "This contains spam content",
        "Very inappropriate comment here",
        "Normal and clean comment"
    ]
    
    print("Filtering Comments:\n")
    
    filter_obj = AhoCorasick(forbidden_words)
    
    for comment in comments:
        print(f"Comment: {comment}")
        filter_obj.search(comment)
        print()


# ============================================================================
# EXAMPLE 5: Log File Analysis
# ============================================================================

def example_5_log_analysis():
    """Find errors and warnings in log files"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Log File Analysis")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # Sample log content
    log_content = """
    2024-01-15 10:00:00 INFO Application started
    2024-01-15 10:01:00 DEBUG Loading configuration
    2024-01-15 10:02:00 ERROR Database connection failed
    2024-01-15 10:03:00 INFO Retrying connection
    2024-01-15 10:04:00 CRITICAL Server crash detected
    2024-01-15 10:05:00 WARNING Memory usage high
    2024-01-15 10:06:00 ERROR Connection timeout
    """
    
    error_keywords = ["ERROR", "CRITICAL", "WARNING", "FATAL"]
    
    print("Log File Content:")
    print(log_content)
    print("\nSearching for error levels:")
    
    analyzer = AhoCorasick(error_keywords)
    analyzer.search(log_content)


# ============================================================================
# EXAMPLE 6: Protein Motif Discovery
# ============================================================================

def example_6_protein_motif():
    """Find known motifs in protein sequences"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Protein Motif Discovery")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # Protein sequence (simplified)
    protein = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGR"
    
    # Known motifs
    motifs = ["VHL", "ALW", "GKV", "ALG"]
    
    print(f"Protein Sequence: {protein}")
    print(f"Known Motifs: {motifs}\n")
    print("Motif Locations:")
    
    finder = AhoCorasick(motifs)
    finder.search(protein)


# ============================================================================
# EXAMPLE 7: Word Frequency (Using Pattern Search)
# ============================================================================

def example_7_word_frequency():
    """Count word occurrences using pattern search"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Word Frequency Analysis")
    print("="*70)
    
    from algorithms.single_pattern import naive_search
    import io
    from contextlib import redirect_stdout
    
    text = "apple banana apple cherry apple banana"
    words = ["apple", "banana", "cherry"]
    
    print(f"Text: {text}\n")
    
    word_counts = {}
    
    for word in words:
        # Capture output to count matches
        f = io.StringIO()
        with redirect_stdout(f):
            naive_search(text, word)
        output = f.getvalue()
        count = output.count("Pattern found")
        word_counts[word] = count
    
    print("Word Frequency:")
    for word, count in word_counts.items():
        print(f"  {word}: {count} occurrences")


# ============================================================================
# EXAMPLE 8: Plagiarism Detection
# ============================================================================

def example_8_plagiarism_detection():
    """Detect copied phrases between documents"""
    print("\n" + "="*70)
    print("EXAMPLE 8: Plagiarism Detection")
    print("="*70)
    
    from algorithms.single_pattern import boyer_moore_search
    
    original = "The quick brown fox jumps over the lazy dog"
    suspicious = "The quick brown fox jumps very high over the lazy dog"
    
    print(f"Original: {original}")
    print(f"Suspicious: {suspicious}\n")
    
    # Extract significant phrases
    phrases = ["quick brown fox", "lazy dog", "jumps over"]
    
    print("Checking for phrase matches:")
    for phrase in phrases:
        print(f"\nSearching for: '{phrase}'")
        boyer_moore_search(suspicious, phrase)


# ============================================================================
# EXAMPLE 9: DNA Tandem Repeats
# ============================================================================

def example_9_tandem_repeats():
    """Find repeating sequences in DNA"""
    print("\n" + "="*70)
    print("EXAMPLE 9: Finding Tandem Repeats")
    print("="*70)
    
    from algorithms.single_pattern import morris_pratt_search
    
    dna = "AABAABAABAACAADAABAABA"
    repeat = "AABA"
    
    print(f"DNA Sequence: {dna}")
    print(f"Repeat Motif: {repeat}\n")
    print("Found repeats at:")
    
    morris_pratt_search(dna, repeat)


# ============================================================================
# EXAMPLE 10: Case-Insensitive Search
# ============================================================================

def example_10_case_insensitive():
    """Search regardless of text case"""
    print("\n" + "="*70)
    print("EXAMPLE 10: Case-Insensitive Search")
    print("="*70)
    
    from algorithms.single_pattern import boyer_moore_search
    
    text = "Python PYTHON python PyThOn"
    pattern = "python"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern} (case-insensitive)\n")
    
    # Convert both to lowercase
    text_lower = text.lower()
    
    print("Results:")
    boyer_moore_search(text_lower, pattern)


# ============================================================================
# EXAMPLE 11: URL/Email Detection
# ============================================================================

def example_11_url_detection():
    """Find URLs and email patterns in text"""
    print("\n" + "="*70)
    print("EXAMPLE 11: URL/Email Detection")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    text = """
    Contact us at support@example.com
    Visit our website at https://example.com
    Email john@test.org for more info
    Check out facebook.com and twitter.com
    """
    
    patterns = [".com", ".org", "@", "https://"]
    
    print(f"Text:{text}")
    print("\nSearching for URL/Email patterns:")
    
    finder = AhoCorasick(patterns)
    finder.search(text)


# ============================================================================
# EXAMPLE 12: Performance Comparison
# ============================================================================

def example_12_performance_comparison():
    """Compare performance of different algorithms"""
    print("\n" + "="*70)
    print("EXAMPLE 12: Performance Comparison")
    print("="*70)
    
    import time
    from algorithms.single_pattern import naive_search, boyer_moore_search
    
    # Create a large text
    text = "A" * 10000 + "NEEDLE" + "B" * 10000
    pattern = "NEEDLE"
    
    print(f"Text size: {len(text)} characters")
    print(f"Pattern: {pattern}\n")
    
    # Benchmark Naive
    start = time.time()
    naive_search(text, pattern)
    naive_time = time.time() - start
    
    # Benchmark Boyer-Moore
    start = time.time()
    boyer_moore_search(text, pattern)
    boyer_time = time.time() - start
    
    print(f"\nNaive Search time: {naive_time:.6f}s")
    print(f"Boyer-Moore time: {boyer_time:.6f}s")
    
    if boyer_time > 0:
        speedup = naive_time / boyer_time
        print(f"Boyer-Moore is {speedup:.1f}x faster")


# ============================================================================
# EXAMPLE 13: Multiple Pattern Types
# ============================================================================

def example_13_multiple_algorithms():
    """Compare different multi-pattern algorithms"""
    print("\n" + "="*70)
    print("EXAMPLE 13: Multiple Pattern Search Algorithms")
    print("="*70)
    
    from algorithms.multiple_pattern import (
        AhoCorasick, 
        rabin_karp_multiple,
        wu_manber,
        commentz_walter
    )
    
    text = "ACGTACGTGACGATCGATCG"
    patterns = ["ACG", "GAC", "ATC"]
    
    print(f"Text: {text}")
    print(f"Patterns: {patterns}\n")
    
    print("Method 1: Rabin-Karp (Multiple)")
    print("-" * 40)
    rabin_karp_multiple(text, patterns)
    
    print("\nMethod 2: Aho-Corasick")
    print("-" * 40)
    ac = AhoCorasick(patterns)
    ac.search(text)
    
    print("\nMethod 3: Wu-Manber")
    print("-" * 40)
    wu_manber(text, patterns)
    
    print("\nMethod 4: Commentz-Walter")
    print("-" * 40)
    commentz_walter(text, patterns)


# ============================================================================
# EXAMPLE 14: Real-World: Search in Book Text
# ============================================================================

def example_14_book_search():
    """Search for character names in book chapters"""
    print("\n" + "="*70)
    print("EXAMPLE 14: Character Search in Book")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # Sample book text
    book_chapter = """
    Alice was walking through the forest when she met the Cheshire Cat.
    "Hello Alice!" said the Cheshire Cat with a wide grin.
    Alice replied, "Do you know where the White Rabbit is?"
    The Cheshire Cat smiled. "Everywhere and nowhere," it said.
    Alice continued her journey, looking for the White Rabbit.
    """
    
    character_names = ["Alice", "Cheshire Cat", "White Rabbit"]
    
    print("Book Excerpt:")
    print(book_chapter)
    print(f"\nCharacter Names: {character_names}")
    print("\nCharacter Appearances:")
    
    finder = AhoCorasick(character_names)
    finder.search(book_chapter)


# ============================================================================
# EXAMPLE 15: Data Validation
# ============================================================================

def example_15_data_validation():
    """Validate data by searching for invalid patterns"""
    print("\n" + "="*70)
    print("EXAMPLE 15: Data Validation")
    print("="*70)
    
    from algorithms.multiple_pattern import AhoCorasick
    
    # Invalid patterns that shouldn't be in data
    invalid_patterns = ["NULL", "undefined", "error", "fail", "invalid"]
    
    data_samples = [
        "user_id: 123, name: John",
        "user_id: undefined, name: Jane",
        "user_id: 456, name: Bob, status: error",
        "user_id: 789, name: Alice"
    ]
    
    validator = AhoCorasick(invalid_patterns)
    
    for i, data in enumerate(data_samples, 1):
        print(f"Validating entry {i}: {data}")
        validator.search(data)
        print()


# ============================================================================
# Main - Run All Examples
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + " "*15 + "Pattern-Searching Practical Examples" + " "*19 + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    
    examples = [
        example_1_basic_text_search,
        example_2_multiple_patterns,
        example_3_dna_sequence,
        example_4_content_filtering,
        example_5_log_analysis,
        example_6_protein_motif,
        example_7_word_frequency,
        example_8_plagiarism_detection,
        example_9_tandem_repeats,
        example_10_case_insensitive,
        example_11_url_detection,
        example_12_performance_comparison,
        example_13_multiple_algorithms,
        example_14_book_search,
        example_15_data_validation,
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\nError in {example_func.__name__}: {e}")
    
    print("\n" + "="*70)
    print("All examples completed!")
    print("="*70)
    print("\nFor more information, check USAGE_GUIDE.md and QUICK_REFERENCE.md")
