# algorithms/single_pattern/naive.py

def naive_search(text, pattern):
    """
    Naive pattern searching algorithm.
    Prints all indices where pattern occurs in the text.
    """
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i}")

# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    naive_search(text, pattern)