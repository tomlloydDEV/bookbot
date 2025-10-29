from stats import word_count
from stats import char_count

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def main():
  book_text = get_book_text("books/frankenstein.txt")
  num_words = word_count(book_text)
  chars = char_count(book_text)
  print(f"Found {num_words} total words")
  print(chars)

main()
