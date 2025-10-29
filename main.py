def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def main():
  book_text = get_book_text("books/frankenstein.txt")
  from stats import word_count
  num_words = word_count(book_text)
  print(f"Found {num_words} total words")
