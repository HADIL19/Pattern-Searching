# algorithms/single_pattern/boyer_moore.py

def bad_char_table(pattern):
    """
    Creates bad character shift table.
    """
    bad_char = {}
    length = len(pattern)
    for i in range(length):
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore_search(text, pattern):
    """
    Boyer-Moore pattern searching algorithm (bad character heuristic).
    """
    n = len(text)
    m = len(pattern)
    bad_char = bad_char_table(pattern)
    s = 0  # shift of the pattern over text

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    boyer_moore_search(text, pattern)