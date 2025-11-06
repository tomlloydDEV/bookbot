import sys

from stats import char_count, chars_sorted, word_count


def get_book_text(filepath: str) -> str:
    # UTF-8 so extended letters (æ, â, etc.) read correctly
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    # --- Exact report format (match tests) ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")

    counts = char_count(text)
    for row in chars_sorted(counts):  # already sorted desc by 'num'
        ch = row["char"]
        if ch.isalpha():  # print only letters
            print(f"{ch}: {row['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
