import os

LINE = "I lost. On the bright side, my loss function has never been more accurate."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the entry must be 1-200 chars, one line, non-blank.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry text does not match the winning line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip() != "", "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"

if __name__ == "__main__":
    main()
