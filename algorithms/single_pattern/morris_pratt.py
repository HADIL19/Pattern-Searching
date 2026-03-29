# algorithms/single_pattern/morris_pratt.py

def compute_prefix(pattern):
    """
    Preprocesses the pattern to create the prefix table.
    """
    m = len(pattern)
    prefix = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k-1]
        if pattern[k] == pattern[q]:
            k += 1
        prefix[q] = k
    return prefix

def morris_pratt_search(text, pattern):
    """
    Morris-Pratt pattern searching algorithm.
    """
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix(pattern)
    q = 0  # number of characters matched

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q-1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            print(f"Pattern found at index {i - m + 1}")
            q = prefix[q-1]

# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    morris_pratt_search(text, pattern)