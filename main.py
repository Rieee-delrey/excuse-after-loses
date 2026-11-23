import os

LINE = "I lost. On the bright side, my loss function has never been more accurate."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Byte-exact read-back: the file on disk must be exactly the winning line.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "entry bytes do not match the winning line"
    written = raw.decode("utf-8")
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip() != "", "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"

if __name__ == "__main__":
    main()
