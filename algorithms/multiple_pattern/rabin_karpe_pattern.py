# algorithms/multiple_pattern/rabin_karp_multiple.py

def rabin_karp_multiple(text, patterns):
    """
    Rabin-Karp algorithm for multiple patterns.
    Prints all occurrences of each pattern in the text.
    """
    d = 256  # number of characters in input alphabet
    q = 101  # a prime number for modulus

    for pattern in patterns:
        n = len(text)
        m = len(pattern)
        h = pow(d, m-1, q)
        p_hash = 0
        t_hash = 0

        # initial hash values
        for i in range(m):
            p_hash = (d * p_hash + ord(pattern[i])) % q
            t_hash = (d * t_hash + ord(text[i])) % q

        # sliding window
        for i in range(n - m + 1):
            if p_hash == t_hash and text[i:i+m] == pattern:
                print(f"Pattern '{pattern}' found at index {i}")
            if i < n - m:
                t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % q
                if t_hash < 0:
                    t_hash += q

# Example usage
if __name__ == "__main__":
    text = "ACGTACGTGACG"
    patterns = ["ACG", "GAC"]
    rabin_karp_multiple(text, patterns)