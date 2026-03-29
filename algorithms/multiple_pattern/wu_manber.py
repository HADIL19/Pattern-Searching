# algorithms/multiple_pattern/wu_manber.py

def wu_manber(text, patterns):
    """
    Simplified Wu-Manber multiple pattern search
    Uses fixed block size = 2 for demonstration
    """
    block_size = 2
    shift_table = {}
    min_len = min(len(p) for p in patterns)

    # Build shift table
    for p in patterns:
        for i in range(len(p) - block_size + 1):
            block = p[i:i+block_size]
            shift_table[block] = min(shift_table.get(block, len(p) - i), len(p) - i)

    n = len(text)
    i = min_len - 1
    while i < n:
        match_found = False
        for p in patterns:
            if text[i-len(p)+1:i+1] == p:
                print(f"Pattern '{p}' found at index {i-len(p)+1}")
                match_found = True
        i += 1 if match_found else 1  # simplified shift

# Example usage
if __name__ == "__main__":
    text = "ACGTACGTGACG"
    patterns = ["ACG", "GAC"]
    wu_manber(text, patterns)