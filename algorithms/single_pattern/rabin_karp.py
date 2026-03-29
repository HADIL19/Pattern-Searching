# algorithms/single_pattern/rabin_karp.py

def rabin_karp_search(text, pattern):
    """
    Rabin-Karp algorithm for single-pattern search.
    Prints all indices where the pattern occurs in the text.
    """
    n = len(text)
    m = len(pattern)
    d = 256         # Number of characters in the input alphabet
    q = 101         # A prime number for modulus (for hashing)
    
    p_hash = 0      # Hash value for pattern
    t_hash = 0      # Hash value for current window in text
    h = 1           # d^(m-1) % q

    # Precompute h = pow(d, m-1) % q
    for i in range(m-1):
        h = (h * d) % q

    # Compute initial hash values for pattern and first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):
        # Check the hash values
        if p_hash == t_hash:
            # If hashes match, check characters one by one
            if text[i:i+m] == pattern:
                print(f"Pattern found at index {i}")

        # Compute hash for next window
        if i < n - m:
            t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % q
            # Make sure hash is positive
            if t_hash < 0:
                t_hash += q

# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    print(f"Searching for pattern '{pattern}' in text '{text}'...")
    rabin_karp_search(text, pattern)