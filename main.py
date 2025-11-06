import sys

from stats import char_count, chars_sorted, word_count


def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    # --- Exact report format (match tests) ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")

    counts = char_count(text)
    for row in chars_sorted(counts):
        if ch.isalpha():  # print only letters
            print(f"{ch}: {row['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
