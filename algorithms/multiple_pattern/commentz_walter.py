# algorithms/multiple_pattern/commentz_walter.py

def commentz_walter(text, patterns):
    """
    Simplified Commentz-Walter multiple-pattern search
    Combines Boyer-Moore logic for multiple patterns
    """
    max_len = max(len(p) for p in patterns)
    bad_char = {}

    # Build bad character table for all patterns
    for p in patterns:
        for i, c in enumerate(p):
            bad_char[c] = i

    n = len(text)
    i = 0
    while i <= n - max_len:
        for p in patterns:
            m = len(p)
            j = m - 1
            while j >= 0 and i+j < n and p[j] == text[i+j]:
                j -= 1
            if j < 0:
                print(f"Pattern '{p}' found at index {i}")
        i += 1  # simplified shift

# Example usage
if __name__ == "__main__":
    text = "ACGTACGTGACG"
    patterns = ["ACG", "GAC"]
    commentz_walter(text, patterns)